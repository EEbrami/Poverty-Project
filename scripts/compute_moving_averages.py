#!/usr/bin/env python3
"""
Compute 5-year moving averages for median income data from LIS DART.

This script processes equivalised disposable household income medians for
Canada, Germany, Luxembourg, United Kingdom, and United States from 1985-2021.
It computes three variants of MA(5): centered, trailing, and weighted.
"""

import os
import sys
import numpy as np
import pandas as pd
from typing import List, Dict, Optional, Tuple


# Constants
TARGET_COUNTRIES = ["Canada", "Germany", "Luxembourg", "United Kingdom", "United States"]
START_YEAR = 1985
END_YEAR = 2021
INPUT_FILE = "xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv"
OUTPUT_DIR = "poverty-project/DART/MIMA"


def load_and_filter_data(input_path: str) -> pd.DataFrame:
    """
    Load CSV data and filter to target countries and years.
    
    Args:
        input_path: Path to input CSV file
        
    Returns:
        DataFrame with countries as rows and years as columns
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Load the CSV
    df = pd.read_csv(input_path)
    
    # Filter to target countries
    df = df[df['countries'].isin(TARGET_COUNTRIES)]
    
    if len(df) == 0:
        raise ValueError(f"No data found for target countries: {TARGET_COUNTRIES}")
    
    # Extract year columns for the target range
    year_cols = [str(y) for y in range(START_YEAR, END_YEAR + 1)]
    available_year_cols = [col for col in year_cols if col in df.columns]
    
    if not available_year_cols:
        raise ValueError(f"No year columns found in range {START_YEAR}-{END_YEAR}")
    
    # Select only country column and year columns
    result_df = df[['countries'] + available_year_cols].copy()
    
    # Convert year columns to numeric, replacing any non-numeric values with NaN
    for col in available_year_cols:
        result_df[col] = pd.to_numeric(result_df[col], errors='coerce')
    
    return result_df


def interpolate_gaps(series: pd.Series, max_gap: int = 2) -> Tuple[pd.Series, List[str]]:
    """
    Interpolate missing values for gaps of up to max_gap years.
    
    Args:
        series: Time series data
        max_gap: Maximum gap size to interpolate (default: 2)
        
    Returns:
        Tuple of (interpolated series, list of metadata messages)
    """
    metadata = []
    result = series.copy()
    
    # Find consecutive NaN runs
    is_nan = result.isna()
    nan_groups = []
    start = None
    
    for idx, val in enumerate(is_nan):
        if val and start is None:
            start = idx
        elif not val and start is not None:
            nan_groups.append((start, idx - 1))
            start = None
    if start is not None:
        nan_groups.append((start, len(is_nan) - 1))
    
    # Interpolate gaps that are within max_gap and not at endpoints
    for start_idx, end_idx in nan_groups:
        gap_size = end_idx - start_idx + 1
        
        # Check if gap is at endpoint
        is_at_start = start_idx == 0
        is_at_end = end_idx == len(result) - 1
        
        if gap_size <= max_gap and not is_at_start and not is_at_end:
            # Perform linear interpolation
            result = result.interpolate(method='linear', limit_area='inside')
            year_start = START_YEAR + start_idx
            year_end = START_YEAR + end_idx
            metadata.append(f"Interpolated {gap_size} years: {year_start}-{year_end}")
        elif is_at_start or is_at_end:
            year_start = START_YEAR + start_idx
            year_end = START_YEAR + end_idx
            metadata.append(f"Endpoint gap not interpolated: {year_start}-{year_end}")
        else:
            year_start = START_YEAR + start_idx
            year_end = START_YEAR + end_idx
            metadata.append(f"Gap exceeds max ({gap_size} > {max_gap}), not interpolated: {year_start}-{year_end}")
    
    return result, metadata


def compute_centered_ma5(series: pd.Series) -> Tuple[pd.Series, List[str]]:
    """
    Compute centered 5-year moving average with window t-2 to t+2.
    
    Args:
        series: Time series data
        
    Returns:
        Tuple of (MA series, list of metadata messages)
    """
    metadata = []
    result = pd.Series(index=series.index, dtype=float)
    
    for i in range(len(series)):
        # Define window: t-2 to t+2
        start = max(0, i - 2)
        end = min(len(series), i + 3)  # +3 because end is exclusive
        
        window_values = series.iloc[start:end]
        valid_values = window_values.dropna()
        
        if len(valid_values) >= 3:
            result.iloc[i] = valid_values.mean()
        else:
            result.iloc[i] = np.nan
            year = START_YEAR + i
            metadata.append(f"Year {year}: Insufficient data in window (< 3 values)")
    
    return result, metadata


def compute_trailing_ma5(series: pd.Series) -> Tuple[pd.Series, List[str]]:
    """
    Compute trailing 5-year moving average with window t-4 to t.
    
    Args:
        series: Time series data
        
    Returns:
        Tuple of (MA series, list of metadata messages)
    """
    metadata = []
    result = pd.Series(index=series.index, dtype=float)
    
    for i in range(len(series)):
        # Define window: t-4 to t
        start = max(0, i - 4)
        end = i + 1
        
        window_values = series.iloc[start:end]
        valid_values = window_values.dropna()
        
        if len(valid_values) >= 3:
            result.iloc[i] = valid_values.mean()
        else:
            result.iloc[i] = np.nan
            year = START_YEAR + i
            metadata.append(f"Year {year}: Insufficient data in window (< 3 values)")
    
    return result, metadata


def compute_weighted_ma5(series: pd.Series) -> Tuple[pd.Series, List[str]]:
    """
    Compute weighted 5-year moving average with triangular weights [1,2,3,2,1].
    
    Args:
        series: Time series data
        
    Returns:
        Tuple of (MA series, list of metadata messages)
    """
    metadata = []
    result = pd.Series(index=series.index, dtype=float)
    base_weights = np.array([1, 2, 3, 2, 1])
    
    for i in range(len(series)):
        # Define window: t-2 to t+2
        start = max(0, i - 2)
        end = min(len(series), i + 3)
        
        window_values = series.iloc[start:end]
        
        # Determine which weights to use based on window position
        offset_start = max(0, 2 - i)  # How many positions from ideal start
        offset_end = max(0, (i + 3) - len(series))  # How many positions from ideal end
        
        weights = base_weights[offset_start:len(base_weights) - offset_end]
        
        # Apply weights only to non-NaN values
        valid_mask = ~window_values.isna()
        valid_values = window_values[valid_mask].values
        valid_weights = weights[valid_mask.values]
        
        if len(valid_values) >= 3:
            weighted_sum = np.sum(valid_values * valid_weights)
            weight_sum = np.sum(valid_weights)
            result.iloc[i] = weighted_sum / weight_sum
        else:
            result.iloc[i] = np.nan
            year = START_YEAR + i
            metadata.append(f"Year {year}: Insufficient weighted values (< 3 values)")
    
    return result, metadata


def format_dataframe_for_output(ma_data: Dict[str, pd.Series]) -> pd.DataFrame:
    """
    Format moving average data into a DataFrame with years as rows and countries as columns.
    
    Args:
        ma_data: Dictionary mapping country names to MA series
        
    Returns:
        DataFrame with year column and country columns
    """
    years = list(range(START_YEAR, END_YEAR + 1))
    result_df = pd.DataFrame({'year': years})
    
    for country in TARGET_COUNTRIES:
        if country in ma_data:
            result_df[country] = ma_data[country].values
    
    # Round to 2 decimal places
    for country in TARGET_COUNTRIES:
        if country in result_df.columns:
            result_df[country] = result_df[country].round(2)
    
    return result_df


def save_results_with_metadata(
    df: pd.DataFrame,
    output_path: str,
    method_name: str,
    all_metadata: Dict[str, List[str]]
) -> None:
    """
    Save results to CSV with metadata footer.
    
    Args:
        df: DataFrame to save
        output_path: Path for output CSV
        method_name: Name of the MA method
        all_metadata: Dictionary mapping country names to metadata messages
    """
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save main data
    df.to_csv(output_path, index=False)
    
    # Append metadata as comments
    if any(all_metadata.values()):
        with open(output_path, 'a') as f:
            f.write('\n# Metadata\n')
            f.write(f'# Method: {method_name}\n')
            f.write(f'# Year range: {START_YEAR}-{END_YEAR}\n')
            f.write(f'# Countries: {", ".join(TARGET_COUNTRIES)}\n')
            f.write('#\n')
            
            for country, messages in all_metadata.items():
                if messages:
                    f.write(f'# {country}:\n')
                    for msg in messages:
                        f.write(f'#   {msg}\n')
    
    print(f"Saved: {output_path}")


def main():
    """Main execution function."""
    print("="*60)
    print("LIS DART Median Income Moving Averages Computation")
    print("="*60)
    
    # Determine base path (repository root)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    
    input_path = os.path.join(repo_root, INPUT_FILE)
    output_dir = os.path.join(repo_root, OUTPUT_DIR)
    
    print(f"\nInput file: {input_path}")
    print(f"Output directory: {output_dir}")
    print(f"Target countries: {', '.join(TARGET_COUNTRIES)}")
    print(f"Year range: {START_YEAR}-{END_YEAR}")
    
    # Load and filter data
    print("\nLoading and filtering data...")
    df = load_and_filter_data(input_path)
    print(f"Loaded {len(df)} countries")
    
    # Process each country
    print("\nProcessing countries...")
    interpolated_data = {}
    interpolation_metadata = {}
    
    for _, row in df.iterrows():
        country = row['countries']
        print(f"  {country}...")
        
        # Extract time series
        year_cols = [str(y) for y in range(START_YEAR, END_YEAR + 1) if str(y) in df.columns]
        series = row[year_cols]
        
        # Interpolate gaps
        interp_series, interp_meta = interpolate_gaps(series, max_gap=2)
        interpolated_data[country] = interp_series
        interpolation_metadata[country] = interp_meta
    
    # Compute three MA variants
    print("\nComputing moving averages...")
    
    # 1. Centered MA(5)
    print("  1. Centered MA(5)...")
    centered_ma = {}
    centered_metadata = {}
    for country, series in interpolated_data.items():
        ma_series, ma_meta = compute_centered_ma5(series)
        centered_ma[country] = ma_series
        centered_metadata[country] = interpolation_metadata[country] + ma_meta
    
    centered_df = format_dataframe_for_output(centered_ma)
    centered_output = os.path.join(output_dir, "centered_ma5_1985-2021.csv")
    save_results_with_metadata(
        centered_df,
        centered_output,
        "Centered 5-Year Moving Average (t-2 to t+2)",
        centered_metadata
    )
    
    # 2. Trailing MA(5)
    print("  2. Trailing MA(5)...")
    trailing_ma = {}
    trailing_metadata = {}
    for country, series in interpolated_data.items():
        ma_series, ma_meta = compute_trailing_ma5(series)
        trailing_ma[country] = ma_series
        trailing_metadata[country] = interpolation_metadata[country] + ma_meta
    
    trailing_df = format_dataframe_for_output(trailing_ma)
    trailing_output = os.path.join(output_dir, "trailing_ma5_1985-2021.csv")
    save_results_with_metadata(
        trailing_df,
        trailing_output,
        "Trailing 5-Year Moving Average (t-4 to t)",
        trailing_metadata
    )
    
    # 3. Weighted MA(5)
    print("  3. Weighted MA(5)...")
    weighted_ma = {}
    weighted_metadata = {}
    for country, series in interpolated_data.items():
        ma_series, ma_meta = compute_weighted_ma5(series)
        weighted_ma[country] = ma_series
        weighted_metadata[country] = interpolation_metadata[country] + ma_meta
    
    weighted_df = format_dataframe_for_output(weighted_ma)
    weighted_output = os.path.join(output_dir, "weighted_ma5_1985-2021.csv")
    save_results_with_metadata(
        weighted_df,
        weighted_output,
        "Weighted 5-Year Moving Average with triangular weights [1,2,3,2,1]",
        weighted_metadata
    )
    
    print("\n" + "="*60)
    print("Computation completed successfully!")
    print("="*60)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
