#!/usr/bin/env python3
"""
Median Income Moving Average (MIMA) Computation Workflow

This script computes three Moving Average variants (Centered, Trailing, Weighted)
for median income data, with robust handling of missing values and edge cases.

Author: GitHub Copilot
"""
import argparse
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Compute Moving Average (MA) variants for median income data.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "--ma-number",
        type=int,
        required=True,
        help="MA window size (N). Must be an integer between 2 and 7 inclusive."
    )
    
    parser.add_argument(
        "--countries",
        type=str,
        required=True,
        help="Comma-separated list of country names as they appear in the input CSV (e.g., 'Canada,Germany,Luxembourg')."
    )
    
    parser.add_argument(
        "--start-year",
        type=int,
        required=True,
        help="Start year of the time period (inclusive)."
    )
    
    parser.add_argument(
        "--end-year",
        type=int,
        required=True,
        help="End year of the time period (inclusive)."
    )
    
    parser.add_argument(
        "--input-path",
        type=str,
        required=True,
        help="Full path to the source CSV file."
    )
    
    parser.add_argument(
        "--output-path",
        type=str,
        required=True,
        help="Directory path where the root output folder will be created (e.g., 'DART' -> outputs to 'DART/MIMA/')."
    )
    
    return parser.parse_args()


def validate_args(args):
    """Validate command-line arguments."""
    errors = []
    
    # Validate MA window size
    if not (2 <= args.ma_number <= 7):
        errors.append(f"MA window size must be between 2 and 7 (got {args.ma_number})")
    
    # Validate year range
    if args.start_year >= args.end_year:
        errors.append(f"Start year ({args.start_year}) must be less than end year ({args.end_year})")
    
    # Validate input file exists
    if not os.path.exists(args.input_path):
        errors.append(f"Input file not found: {args.input_path}")
    
    if errors:
        for error in errors:
            print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


def load_and_filter_data(
    csv_path: str,
    countries: List[str],
    start_year: int,
    end_year: int
) -> Tuple[pd.DataFrame, List[int]]:
    """
    Load CSV and filter for specified countries and years.
    
    Returns:
        Tuple of (filtered DataFrame, list of year columns)
    """
    df = pd.read_csv(csv_path)
    
    # Detect entity column
    if "countries" in df.columns:
        entity_col = "countries"
    else:
        entity_col = df.columns[0]
    
    # Detect year columns
    year_cols = []
    for col in df.columns:
        if col == entity_col:
            continue
        try:
            year = int(str(col).strip())
            if start_year <= year <= end_year:
                year_cols.append(str(col).strip())
        except (ValueError, AttributeError):
            continue
    
    if not year_cols:
        raise ValueError(f"No year columns found in range {start_year}-{end_year}")
    
    years = sorted([int(y) for y in year_cols])
    year_cols_str = [str(y) for y in years]
    
    # Filter countries
    df_filtered = df[df[entity_col].isin(countries)].copy()
    
    if df_filtered.empty:
        raise ValueError(f"No data found for specified countries: {countries}")
    
    # Select only entity column and year columns
    cols_to_keep = [entity_col] + year_cols_str
    df_filtered = df_filtered[cols_to_keep]
    
    return df_filtered, years


def interpolate_missing_values(df: pd.DataFrame, entity_col: str, years: List[int], limit: int = 2) -> pd.DataFrame:
    """
    Apply linear interpolation for data gaps <= limit years.
    Gaps at endpoints or > limit years remain NaN.
    
    Args:
        df: DataFrame with entity column and year columns
        entity_col: Name of the entity (country) column
        years: List of year integers
        limit: Maximum gap size to interpolate (default 2)
    
    Returns:
        DataFrame with interpolated values
    """
    df_interp = df.copy()
    year_cols = [str(y) for y in years]
    
    # Interpolate row by row
    for idx in df_interp.index:
        values = df_interp.loc[idx, year_cols].values.astype(float)
        
        # Use pandas Series for interpolation
        series = pd.Series(values)
        interpolated = series.interpolate(method='linear', limit=limit, limit_area='inside')
        
        df_interp.loc[idx, year_cols] = interpolated.values
    
    return df_interp


def triangular_weights(n: int) -> np.ndarray:
    """
    Generate triangular weights for odd window size n.
    For n=5: [1, 2, 3, 2, 1]
    
    Args:
        n: Window size (must be odd)
    
    Returns:
        Array of triangular weights
    """
    if n % 2 == 0:
        raise ValueError("Triangular weights only defined for odd window sizes")
    
    half = n // 2
    weights = np.concatenate([
        np.arange(1, half + 1),
        [half + 1],
        np.arange(half, 0, -1)
    ])
    return weights


def compute_centered_ma(series: pd.Series, n: int, min_periods: int = 3) -> pd.Series:
    """
    Compute centered moving average.
    
    Args:
        series: Time series data
        n: Window size
        min_periods: Minimum number of non-NaN values required
    
    Returns:
        Series with centered MA values
    """
    return series.rolling(window=n, center=True, min_periods=min_periods).mean()


def compute_trailing_ma(series: pd.Series, n: int, min_periods: int = 3) -> pd.Series:
    """
    Compute trailing (backward-looking) moving average.
    
    Args:
        series: Time series data
        n: Window size
        min_periods: Minimum number of non-NaN values required
    
    Returns:
        Series with trailing MA values
    """
    return series.rolling(window=n, center=False, min_periods=min_periods).mean()


def compute_weighted_ma(series: pd.Series, n: int, min_periods: int = 3) -> pd.Series:
    """
    Compute weighted moving average with triangular weights.
    Only works for odd n. Uses centered window.
    At boundaries, proportionally adjusts weights for available data.
    
    Args:
        series: Time series data
        n: Window size (must be odd)
        min_periods: Minimum number of non-NaN values required
    
    Returns:
        Series with weighted MA values, or None if n is even
    """
    if n % 2 == 0:
        return None  # Skip for even n
    
    weights = triangular_weights(n)
    half = n // 2
    
    result = pd.Series(index=series.index, dtype=float)
    
    for i in range(len(series)):
        # Define window boundaries
        start_idx = max(0, i - half)
        end_idx = min(len(series), i + half + 1)
        
        # Extract window data and corresponding weights
        window_data = series.iloc[start_idx:end_idx].values
        
        # Calculate which weights to use based on actual window position
        weight_start = half - (i - start_idx)
        weight_end = weight_start + (end_idx - start_idx)
        window_weights = weights[weight_start:weight_end]
        
        # Filter out NaN values and their corresponding weights
        valid_mask = ~np.isnan(window_data)
        valid_data = window_data[valid_mask]
        valid_weights = window_weights[valid_mask]
        
        # Check minimum periods requirement
        if len(valid_data) >= min_periods:
            # Compute weighted average
            result.iloc[i] = np.sum(valid_data * valid_weights) / np.sum(valid_weights)
        else:
            result.iloc[i] = np.nan
    
    return result


def compute_all_ma_variants(
    df: pd.DataFrame,
    entity_col: str,
    years: List[int],
    n: int
) -> Dict[str, pd.DataFrame]:
    """
    Compute all three MA variants for the dataset.
    
    Args:
        df: DataFrame with entity column and year columns
        entity_col: Name of the entity column
        years: List of year integers
        n: MA window size
    
    Returns:
        Dictionary with keys 'centered', 'trailing', 'weighted' mapping to DataFrames
    """
    year_cols = [str(y) for y in years]
    results = {}
    
    # Centered MA
    df_centered = df.copy()
    for idx in df.index:
        series = df.loc[idx, year_cols].astype(float)
        df_centered.loc[idx, year_cols] = compute_centered_ma(series, n)
    results['centered'] = df_centered
    
    # Trailing MA
    df_trailing = df.copy()
    for idx in df.index:
        series = df.loc[idx, year_cols].astype(float)
        df_trailing.loc[idx, year_cols] = compute_trailing_ma(series, n)
    results['trailing'] = df_trailing
    
    # Weighted MA (only for odd n)
    if n % 2 == 1:
        df_weighted = df.copy()
        for idx in df.index:
            series = df.loc[idx, year_cols].astype(float)
            df_weighted.loc[idx, year_cols] = compute_weighted_ma(series, n)
        results['weighted'] = df_weighted
    else:
        results['weighted'] = None
    
    return results


def count_nans(df: pd.DataFrame, entity_col: str, years: List[int]) -> int:
    """Count total NaN values in year columns."""
    year_cols = [str(y) for y in years]
    return df[year_cols].isna().sum().sum()


def create_metadata_log(
    metadata_path: str,
    args,
    years: List[int],
    countries: List[str],
    initial_nans: int,
    post_interp_nans: int,
    results: Dict[str, pd.DataFrame],
    entity_col: str
) -> None:
    """Create comprehensive metadata log file."""
    
    with open(metadata_path, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("MIMA COMPUTATION METADATA\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("INPUT PARAMETERS:\n")
        f.write("-" * 80 + "\n")
        f.write(f"MA Window Size (N): {args.ma_number}\n")
        f.write(f"Countries: {', '.join(countries)}\n")
        f.write(f"Time Period: {args.start_year} - {args.end_year} ({len(years)} years)\n")
        f.write(f"Input File: {args.input_path}\n")
        f.write(f"Output Path: {args.output_path}\n")
        f.write(f"Interpolation Limit: 2 years\n")
        f.write(f"Minimum Required Values per Window: 3\n\n")
        
        f.write("DATA PREPROCESSING:\n")
        f.write("-" * 80 + "\n")
        f.write(f"Initial NaN count: {initial_nans}\n")
        f.write(f"Post-interpolation NaN count: {post_interp_nans}\n")
        f.write(f"Values filled by interpolation: {initial_nans - post_interp_nans}\n\n")
        
        # Centered MA
        f.write("=" * 80 + "\n")
        f.write("CENTERED MA COMPUTATION\n")
        f.write("=" * 80 + "\n")
        f.write(f"Method: Simple arithmetic mean of symmetric window centered on year t\n")
        f.write(f"Window: t-{args.ma_number//2} to t+{args.ma_number//2}\n")
        year_cols = [str(y) for y in years]
        final_nans_centered = count_nans(results['centered'], entity_col, years)
        f.write(f"Final NaN count: {final_nans_centered}\n")
        f.write(f"Values computed: {len(countries) * len(years) - final_nans_centered}\n\n")
        
        # Trailing MA
        f.write("=" * 80 + "\n")
        f.write("TRAILING MA COMPUTATION\n")
        f.write("=" * 80 + "\n")
        f.write(f"Method: Simple arithmetic mean of backward-looking window\n")
        f.write(f"Window: t-{args.ma_number-1} to t\n")
        final_nans_trailing = count_nans(results['trailing'], entity_col, years)
        f.write(f"Final NaN count: {final_nans_trailing}\n")
        f.write(f"Values computed: {len(countries) * len(years) - final_nans_trailing}\n\n")
        
        # Weighted MA
        f.write("=" * 80 + "\n")
        f.write("WEIGHTED MA COMPUTATION\n")
        f.write("=" * 80 + "\n")
        if results['weighted'] is not None:
            f.write(f"Method: Centered window with triangular weights\n")
            weights = triangular_weights(args.ma_number)
            f.write(f"Weights: {[int(w) for w in weights]}\n")
            f.write(f"Window: t-{args.ma_number//2} to t+{args.ma_number//2}\n")
            f.write(f"Boundary handling: Proportional weight adjustment for partial windows\n")
            final_nans_weighted = count_nans(results['weighted'], entity_col, years)
            f.write(f"Final NaN count: {final_nans_weighted}\n")
            f.write(f"Values computed: {len(countries) * len(years) - final_nans_weighted}\n\n")
        else:
            f.write(f"SKIPPED: N={args.ma_number} is even. Weighted MA only computed for odd N.\n\n")
        
        f.write("=" * 80 + "\n")
        f.write("END OF METADATA\n")
        f.write("=" * 80 + "\n")


def generate_visualizations(
    results: Dict[str, pd.DataFrame],
    entity_col: str,
    years: List[int],
    output_dir: str,
    input_stem: str,
    n: int,
    start_year: int,
    end_year: int
) -> None:
    """Generate PNG and PDF visualizations for each MA variant."""
    
    year_cols = [str(y) for y in years]
    
    for method, df in results.items():
        if df is None:
            continue
        
        # Create figure
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Plot each country
        for idx in df.index:
            country = df.loc[idx, entity_col]
            values = df.loc[idx, year_cols].astype(float)
            ax.plot(years, values, marker='o', label=country, linewidth=2, markersize=4)
        
        # Formatting
        ax.set_xlabel('Year', fontsize=12, fontweight='bold')
        ax.set_ylabel('Median Income (MA-adjusted)', fontsize=12, fontweight='bold')
        ax.set_title(f'{method.capitalize()} MA({n}): {start_year}-{end_year}', 
                     fontsize=14, fontweight='bold')
        ax.legend(loc='best', fontsize=10)
        ax.grid(True, alpha=0.3)
        
        # Save as PNG
        png_filename = f"{input_stem}_{method}_MA{n}_{start_year}-{end_year}.png"
        png_path = os.path.join(output_dir, png_filename)
        plt.savefig(png_path, dpi=300, bbox_inches='tight')
        print(f"  Generated: {png_path}")
        
        # Save as PDF
        pdf_filename = f"{input_stem}_{method}_MA{n}_{start_year}-{end_year}.pdf"
        pdf_path = os.path.join(output_dir, pdf_filename)
        plt.savefig(pdf_path, bbox_inches='tight')
        print(f"  Generated: {pdf_path}")
        
        plt.close(fig)


def main():
    """Main execution function."""
    args = parse_args()
    validate_args(args)
    
    # Parse countries list
    countries = [c.strip() for c in args.countries.split(',')]
    
    # Extract input file stem
    input_path = Path(args.input_path)
    input_stem = input_path.stem
    
    print(f"=" * 80)
    print(f"MIMA COMPUTATION WORKFLOW")
    print(f"=" * 80)
    print(f"MA Window Size: {args.ma_number}")
    print(f"Countries: {', '.join(countries)}")
    print(f"Time Period: {args.start_year} - {args.end_year}")
    print(f"Input File: {args.input_path}")
    print(f"Output Base: {args.output_path}")
    print(f"=" * 80)
    print()
    
    # Create output directories
    output_base = Path(args.output_path) / "MIMA"
    csv_dir = output_base / "csv"
    viz_dir = output_base / "visualizations"
    
    csv_dir.mkdir(parents=True, exist_ok=True)
    viz_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Step 1: Loading and filtering data...")
    df, years = load_and_filter_data(args.input_path, countries, args.start_year, args.end_year)
    entity_col = "countries" if "countries" in df.columns else df.columns[0]
    initial_nans = count_nans(df, entity_col, years)
    print(f"  Loaded {len(df)} countries, {len(years)} years")
    print(f"  Initial NaN count: {initial_nans}")
    
    print(f"\nStep 2: Applying linear interpolation (limit=2 years)...")
    df_interp = interpolate_missing_values(df, entity_col, years, limit=2)
    post_interp_nans = count_nans(df_interp, entity_col, years)
    print(f"  Post-interpolation NaN count: {post_interp_nans}")
    print(f"  Values filled: {initial_nans - post_interp_nans}")
    
    print(f"\nStep 3: Computing MA variants...")
    results = compute_all_ma_variants(df_interp, entity_col, years, args.ma_number)
    print(f"  Computed: Centered MA({args.ma_number})")
    print(f"  Computed: Trailing MA({args.ma_number})")
    if results['weighted'] is not None:
        print(f"  Computed: Weighted MA({args.ma_number})")
    else:
        print(f"  Skipped: Weighted MA (N={args.ma_number} is even)")
    
    print(f"\nStep 4: Saving CSV outputs...")
    for method, df_result in results.items():
        if df_result is None:
            continue
        
        csv_filename = f"{input_stem}_{method}_MA{args.ma_number}_{args.start_year}-{args.end_year}.csv"
        csv_path = csv_dir / csv_filename
        df_result.to_csv(csv_path, index=False)
        print(f"  Saved: {csv_path}")
    
    print(f"\nStep 5: Creating metadata log...")
    metadata_filename = f"{input_stem}_MA{args.ma_number}_metadata.txt"
    metadata_path = csv_dir / metadata_filename
    create_metadata_log(str(metadata_path), args, years, countries, 
                       initial_nans, post_interp_nans, results, entity_col)
    print(f"  Saved: {metadata_path}")
    
    print(f"\nStep 6: Generating visualizations...")
    generate_visualizations(results, entity_col, years, str(viz_dir), 
                          input_stem, args.ma_number, args.start_year, args.end_year)
    
    print(f"\n" + "=" * 80)
    print(f"✓ MIMA computation completed successfully!")
    print(f"✓ Outputs saved to: {output_base}")
    print(f"=" * 80)


if __name__ == "__main__":
    main()
