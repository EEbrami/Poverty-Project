#!/usr/bin/env python3
"""
Compute 5-year Moving Averages (MA(5)) for Median Income Data.

This script processes median income data from the Luxembourg Income Study (LIS) 
DART tool and computes three variants of 5-year moving averages:
1. Centered MA(5): symmetric window (t-2 to t+2)
2. Trailing MA(5): backward-looking window (t-4 to t)
3. Weighted MA(5): centered window with triangular weights [1, 2, 3, 2, 1]

Input: dart-med-pop_decomp-dhi.csv
Output: Three CSV files with computed moving averages and visualizations
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

# Configuration
INPUT_FILE = "/home/runner/work/Poverty-Project/Poverty-Project/xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv"
OUTPUT_DIR = "/home/runner/work/Poverty-Project/Poverty-Project/DART/MIMA"
COUNTRIES = ["Canada", "Germany", "Luxembourg", "United Kingdom", "United States"]
START_YEAR = 1985
END_YEAR = 2021
MIN_VALUES_REQUIRED = 3  # Minimum values required in a window


def load_and_filter_data(csv_path: str) -> pd.DataFrame:
    """
    Load CSV file and filter for specified countries and years.
    
    Args:
        csv_path: Path to input CSV file
        
    Returns:
        Filtered DataFrame with countries as rows and years as columns
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Input file not found: {csv_path}")
    
    print(f"Loading data from: {csv_path}")
    df = pd.read_csv(csv_path)
    
    # Filter for specified countries
    df = df[df['countries'].isin(COUNTRIES)]
    
    if len(df) != len(COUNTRIES):
        found = df['countries'].tolist()
        missing = set(COUNTRIES) - set(found)
        print(f"Warning: Some countries not found in data: {missing}")
    
    # Select year columns
    year_cols = [str(year) for year in range(START_YEAR, END_YEAR + 1)]
    available_cols = [col for col in year_cols if col in df.columns]
    
    # Create filtered DataFrame
    result = df[['countries'] + available_cols].copy()
    result = result.set_index('countries')
    
    # Convert year columns to numeric
    for col in available_cols:
        result[col] = pd.to_numeric(result[col], errors='coerce')
    
    print(f"Loaded data for {len(result)} countries, years {START_YEAR}-{END_YEAR}")
    return result


def interpolate_missing_values(series: pd.Series, max_gap: int = 2) -> Tuple[pd.Series, List[str]]:
    """
    Interpolate missing values with linear interpolation for gaps <= max_gap years.
    
    Args:
        series: Time series with missing values
        max_gap: Maximum gap size (in years) to interpolate
        
    Returns:
        Tuple of (interpolated series, list of interpolation notes)
    """
    notes = []
    result = series.copy()
    
    # Find gaps
    missing_mask = result.isna()
    if not missing_mask.any():
        return result, notes
    
    # Identify contiguous missing segments
    missing_indices = missing_mask[missing_mask].index.tolist()
    
    # Group consecutive missing values
    gaps = []
    if missing_indices:
        current_gap = [missing_indices[0]]
        for i in range(1, len(missing_indices)):
            # Check if years are consecutive (considering they might be strings)
            prev_year = int(missing_indices[i-1])
            curr_year = int(missing_indices[i])
            if curr_year == prev_year + 1:
                current_gap.append(missing_indices[i])
            else:
                gaps.append(current_gap)
                current_gap = [missing_indices[i]]
        gaps.append(current_gap)
    
    # Interpolate small gaps
    for gap in gaps:
        gap_size = len(gap)
        if gap_size <= max_gap:
            # Check if there are values before and after the gap for interpolation
            gap_start_year = int(gap[0])
            gap_end_year = int(gap[-1])
            
            # Get indices in the series
            all_years = [int(y) for y in series.index]
            gap_start_idx = all_years.index(gap_start_year)
            gap_end_idx = all_years.index(gap_end_year)
            
            # Check for values before and after
            has_before = gap_start_idx > 0 and not pd.isna(result.iloc[gap_start_idx - 1])
            has_after = gap_end_idx < len(result) - 1 and not pd.isna(result.iloc[gap_end_idx + 1])
            
            if has_before and has_after:
                # Perform linear interpolation
                result = result.interpolate(method='linear', limit=max_gap, limit_area='inside')
                notes.append(f"Interpolated {gap_size}-year gap: {gap[0]}-{gap[-1]}")
    
    return result, notes


def centered_ma5(series: pd.Series, min_values: int = 3) -> Tuple[pd.Series, List[str]]:
    """
    Compute centered 5-year moving average (t-2 to t+2).
    
    Args:
        series: Time series data
        min_values: Minimum number of values required in window
        
    Returns:
        Tuple of (MA series, list of computation notes)
    """
    notes = []
    result = pd.Series(index=series.index, dtype=float)
    years = [int(y) for y in series.index]
    
    for i, year in enumerate(years):
        # Define window: t-2 to t+2
        window_start = max(0, i - 2)
        window_end = min(len(years), i + 3)  # +3 because slice is exclusive
        
        window_values = series.iloc[window_start:window_end].dropna()
        
        if len(window_values) >= min_values:
            result.iloc[i] = window_values.mean()
        else:
            result.iloc[i] = np.nan
            notes.append(f"Year {year}: Insufficient data ({len(window_values)} values, need {min_values})")
    
    return result, notes


def trailing_ma5(series: pd.Series, min_values: int = 3) -> Tuple[pd.Series, List[str]]:
    """
    Compute trailing 5-year moving average (t-4 to t).
    
    Args:
        series: Time series data
        min_values: Minimum number of values required in window
        
    Returns:
        Tuple of (MA series, list of computation notes)
    """
    notes = []
    result = pd.Series(index=series.index, dtype=float)
    years = [int(y) for y in series.index]
    
    for i, year in enumerate(years):
        # Define window: t-4 to t
        window_start = max(0, i - 4)
        window_end = i + 1
        
        window_values = series.iloc[window_start:window_end].dropna()
        
        if len(window_values) >= min_values:
            result.iloc[i] = window_values.mean()
        else:
            result.iloc[i] = np.nan
            notes.append(f"Year {year}: Insufficient data ({len(window_values)} values, need {min_values})")
    
    return result, notes


def weighted_ma5(series: pd.Series, min_values: int = 3) -> Tuple[pd.Series, List[str]]:
    """
    Compute weighted 5-year moving average with triangular weights [1, 2, 3, 2, 1].
    
    Args:
        series: Time series data
        min_values: Minimum number of values required in window
        
    Returns:
        Tuple of (MA series, list of computation notes)
    """
    notes = []
    result = pd.Series(index=series.index, dtype=float)
    years = [int(y) for y in series.index]
    base_weights = [1, 2, 3, 2, 1]
    
    for i, year in enumerate(years):
        # Define window: t-2 to t+2
        window_start = max(0, i - 2)
        window_end = min(len(years), i + 3)
        
        window_data = series.iloc[window_start:window_end]
        
        # Determine actual window position relative to the ideal window
        offset_start = max(0, 2 - i)  # How many positions we're short at the start
        offset_end = max(0, (i + 3) - len(years))  # How many positions we're short at the end
        
        # Extract appropriate weights for this window
        weight_start = offset_start
        weight_end = 5 - offset_end
        window_weights = base_weights[weight_start:weight_end]
        
        # Filter out NaN values and corresponding weights
        valid_mask = ~window_data.isna()
        valid_values = window_data[valid_mask].values
        valid_weights = [w for w, m in zip(window_weights, valid_mask) if m]
        
        if len(valid_values) >= min_values:
            weighted_sum = sum(v * w for v, w in zip(valid_values, valid_weights))
            weight_sum = sum(valid_weights)
            result.iloc[i] = weighted_sum / weight_sum
        else:
            result.iloc[i] = np.nan
            notes.append(f"Year {year}: Insufficient data ({len(valid_values)} values, need {min_values})")
    
    return result, notes


def save_results(df: pd.DataFrame, filename: str, metadata: Dict[str, List[str]]):
    """
    Save results to CSV with metadata footer.
    
    Args:
        df: DataFrame with results
        filename: Output filename
        metadata: Dictionary of metadata notes by country
    """
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    # Save main data
    df.to_csv(output_path, float_format='%.2f')
    
    # Append metadata as comments
    with open(output_path, 'a') as f:
        f.write('\n# Metadata\n')
        for country, notes in metadata.items():
            if notes:
                f.write(f'# {country}:\n')
                for note in notes:
                    f.write(f'#   {note}\n')
    
    print(f"Saved: {output_path}")


def create_visualizations(df: pd.DataFrame, filename_base: str, title: str):
    """
    Create PNG and PDF visualizations of the moving averages.
    
    Args:
        df: DataFrame with results
        filename_base: Base filename without extension
        title: Chart title
    """
    plt.figure(figsize=(14, 8))
    
    for country in df.columns:
        years = [int(y) for y in df.index]
        values = df[country].values
        plt.plot(years, values, marker='o', linewidth=2, label=country, alpha=0.8)
    
    plt.title(f'MIMA: {title}', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Median Income (National Currency)', fontsize=12)
    plt.legend(loc='best', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save as PNG
    png_path = os.path.join(OUTPUT_DIR, f"{filename_base}.png")
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {png_path}")
    
    # Save as PDF
    pdf_path = os.path.join(OUTPUT_DIR, f"{filename_base}.pdf")
    plt.savefig(pdf_path, bbox_inches='tight')
    print(f"Saved: {pdf_path}")
    
    plt.close()


def main():
    """Main execution function."""
    print("=" * 80)
    print("MIMA: Median Income Moving Average Computation")
    print("=" * 80)
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")
    
    # Load and filter data
    data = load_and_filter_data(INPUT_FILE)
    
    # Process each country and compute moving averages
    all_metadata = {
        'centered': {},
        'trailing': {},
        'weighted': {}
    }
    
    centered_results = pd.DataFrame(index=data.columns)
    trailing_results = pd.DataFrame(index=data.columns)
    weighted_results = pd.DataFrame(index=data.columns)
    
    for country in data.index:
        print(f"\nProcessing: {country}")
        series = data.loc[country]
        
        # Interpolate missing values
        interpolated, interp_notes = interpolate_missing_values(series)
        if interp_notes:
            print(f"  Interpolation notes: {len(interp_notes)} gaps interpolated")
        
        # Compute centered MA(5)
        centered, centered_notes = centered_ma5(interpolated)
        centered_results[country] = centered
        all_metadata['centered'][country] = interp_notes + centered_notes
        
        # Compute trailing MA(5)
        trailing, trailing_notes = trailing_ma5(interpolated)
        trailing_results[country] = trailing
        all_metadata['trailing'][country] = interp_notes + trailing_notes
        
        # Compute weighted MA(5)
        weighted, weighted_notes = weighted_ma5(interpolated)
        weighted_results[country] = weighted
        all_metadata['weighted'][country] = interp_notes + weighted_notes
    
    # Rename index to 'year'
    centered_results.index.name = 'year'
    trailing_results.index.name = 'year'
    weighted_results.index.name = 'year'
    
    # Save results
    print("\n" + "=" * 80)
    print("Saving results...")
    print("=" * 80)
    
    save_results(centered_results, "centered_ma5_1985-2021.csv", all_metadata['centered'])
    save_results(trailing_results, "trailing_ma5_1985-2021.csv", all_metadata['trailing'])
    save_results(weighted_results, "weighted_ma5_1985-2021.csv", all_metadata['weighted'])
    
    # Create visualizations
    print("\n" + "=" * 80)
    print("Creating visualizations...")
    print("=" * 80)
    
    create_visualizations(centered_results, "centered_ma5_1985-2021", 
                         "Centered 5-Year Moving Average (1985-2021)")
    create_visualizations(trailing_results, "trailing_ma5_1985-2021",
                         "Trailing 5-Year Moving Average (1985-2021)")
    create_visualizations(weighted_results, "weighted_ma5_1985-2021",
                         "Weighted 5-Year Moving Average (1985-2021)")
    
    print("\n" + "=" * 80)
    print("Processing complete!")
    print("=" * 80)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
