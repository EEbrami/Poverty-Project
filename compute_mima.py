#!/usr/bin/env python3
"""
Compute Moving Average (MIMA) Indicators for Income Data

This script computes three types of moving averages (Centered, Trailing, and Weighted)
on income time-series data with configurable window sizes and parameters.
"""

import argparse
import os
import sys
from pathlib import Path
from typing import List, Tuple, Optional, Dict
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Compute Moving Average (MIMA) indicators for income data.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "--ma-number",
        type=int,
        required=True,
        help="Moving average window size (integer between 2 and 7 inclusive)"
    )
    
    parser.add_argument(
        "--countries",
        type=str,
        required=True,
        help="Comma-separated list of ISO country codes (e.g., 'CAN,DEU,LUX')"
    )
    
    parser.add_argument(
        "--start-year",
        type=int,
        required=True,
        help="Start year for analysis (inclusive)"
    )
    
    parser.add_argument(
        "--end-year",
        type=int,
        required=True,
        help="End year for analysis (inclusive)"
    )
    
    parser.add_argument(
        "--input-path",
        type=str,
        required=True,
        help="Full path to the input CSV file"
    )
    
    parser.add_argument(
        "--output-path",
        type=str,
        required=True,
        help="Base directory path for output (outputs will be under OUTPUT_PATH/MIMA/)"
    )
    
    return parser.parse_args()


def validate_arguments(args):
    """Validate command-line arguments."""
    errors = []
    
    # Validate MA window size
    if not (2 <= args.ma_number <= 7):
        errors.append(f"MA window size must be between 2 and 7, got {args.ma_number}")
    
    # Validate year range
    if args.start_year > args.end_year:
        errors.append(f"Start year ({args.start_year}) must be <= end year ({args.end_year})")
    
    # Validate input file exists
    if not os.path.exists(args.input_path):
        errors.append(f"Input file not found: {args.input_path}")
    
    # Validate output path parent exists
    output_parent = Path(args.output_path).parent
    if not output_parent.exists():
        errors.append(f"Output parent directory does not exist: {output_parent}")
    
    if errors:
        for error in errors:
            print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


def load_and_filter_data(input_path: str, countries: List[str], start_year: int, end_year: int) -> pd.DataFrame:
    """
    Load CSV data and filter by countries and years.
    
    Args:
        input_path: Path to input CSV file
        countries: List of country codes to filter
        start_year: Start year (inclusive)
        end_year: End year (inclusive)
    
    Returns:
        Filtered DataFrame with countries as rows and years as columns
    """
    # Load the CSV
    df = pd.read_csv(input_path)
    
    # Get the country column name (first column)
    country_col = df.columns[0]
    
    # Filter by countries
    df_filtered = df[df[country_col].isin(countries)].copy()
    
    if df_filtered.empty:
        print(f"Error: No data found for specified countries: {countries}", file=sys.stderr)
        sys.exit(1)
    
    # Get year columns in the specified range
    all_cols = df.columns.tolist()
    year_cols = [col for col in all_cols[1:] if col.isdigit() and start_year <= int(col) <= end_year]
    
    if not year_cols:
        print(f"Error: No year columns found in range {start_year}-{end_year}", file=sys.stderr)
        sys.exit(1)
    
    # Keep only country column and filtered year columns
    df_result = df_filtered[[country_col] + year_cols].copy()
    df_result = df_result.set_index(country_col)
    
    # Convert columns to numeric, handling any non-numeric values
    for col in df_result.columns:
        df_result[col] = pd.to_numeric(df_result[col], errors='coerce')
    
    return df_result


def interpolate_missing_values(df: pd.DataFrame, limit: int = 2) -> Tuple[pd.DataFrame, int, int]:
    """
    Apply linear interpolation for missing values with gap limit.
    
    Args:
        df: DataFrame with years as columns
        limit: Maximum consecutive NaN values to interpolate
    
    Returns:
        Tuple of (interpolated DataFrame, initial NaN count, final NaN count)
    """
    initial_nan_count = df.isna().sum().sum()
    
    # Apply linear interpolation row-wise (for each country)
    df_interpolated = df.copy()
    for idx in df_interpolated.index:
        df_interpolated.loc[idx] = df_interpolated.loc[idx].interpolate(
            method='linear', 
            limit=limit, 
            limit_area='inside'
        )
    
    final_nan_count = df_interpolated.isna().sum().sum()
    
    return df_interpolated, initial_nan_count, final_nan_count


def compute_centered_ma(df: pd.DataFrame, window: int, min_periods: int = 3) -> pd.DataFrame:
    """
    Compute centered moving average.
    
    Args:
        df: DataFrame with years as columns
        window: Window size
        min_periods: Minimum non-NaN values required
    
    Returns:
        DataFrame with centered MA values
    """
    df_ma = df.copy()
    
    # Adjust min_periods if it exceeds window size
    effective_min_periods = min(min_periods, window)
    
    for idx in df_ma.index:
        series = df_ma.loc[idx]
        # Use pandas rolling with center=True
        ma_series = series.rolling(window=window, center=True, min_periods=effective_min_periods).mean()
        df_ma.loc[idx] = ma_series
    
    return df_ma


def compute_trailing_ma(df: pd.DataFrame, window: int, min_periods: int = 3) -> pd.DataFrame:
    """
    Compute trailing (backward-looking) moving average.
    
    Args:
        df: DataFrame with years as columns
        window: Window size
        min_periods: Minimum non-NaN values required
    
    Returns:
        DataFrame with trailing MA values
    """
    df_ma = df.copy()
    
    # Adjust min_periods if it exceeds window size
    effective_min_periods = min(min_periods, window)
    
    for idx in df_ma.index:
        series = df_ma.loc[idx]
        # Use pandas rolling with center=False (default)
        ma_series = series.rolling(window=window, center=False, min_periods=effective_min_periods).mean()
        df_ma.loc[idx] = ma_series
    
    return df_ma


def compute_weighted_ma(df: pd.DataFrame, window: int, min_periods: int = 3) -> Optional[pd.DataFrame]:
    """
    Compute weighted moving average with triangular weights (odd window only).
    
    Args:
        df: DataFrame with years as columns
        window: Window size (must be odd)
        min_periods: Minimum non-NaN values required
    
    Returns:
        DataFrame with weighted MA values, or None if window is even
    """
    if window % 2 == 0:
        return None
    
    # Create triangular weights
    half = window // 2
    weights = list(range(1, half + 2)) + list(range(half, 0, -1))
    weights = np.array(weights, dtype=float)
    
    df_ma = df.copy()
    
    for idx in df_ma.index:
        series = df_ma.loc[idx].values
        result = np.full_like(series, np.nan, dtype=float)
        
        for i in range(len(series)):
            # Determine window bounds (centered)
            start = max(0, i - half)
            end = min(len(series), i + half + 1)
            
            # Get window data
            window_data = series[start:end]
            
            # Determine which weights to use
            weight_start = max(0, half - i)
            weight_end = weight_start + len(window_data)
            window_weights = weights[weight_start:weight_end]
            
            # Filter out NaN values and corresponding weights
            valid_mask = ~np.isnan(window_data)
            valid_data = window_data[valid_mask]
            valid_weights = window_weights[valid_mask]
            
            # Check if we have enough non-NaN values
            if len(valid_data) >= min_periods:
                # Compute weighted average
                result[i] = np.sum(valid_data * valid_weights) / np.sum(valid_weights)
        
        df_ma.loc[idx] = result
    
    return df_ma


def create_output_directories(base_path: str) -> Tuple[str, str]:
    """
    Create output directory structure.
    
    Args:
        base_path: Base output path
    
    Returns:
        Tuple of (csv_dir, viz_dir)
    """
    csv_dir = os.path.join(base_path, "MIMA", "csv")
    viz_dir = os.path.join(base_path, "MIMA", "visualizations")
    
    os.makedirs(csv_dir, exist_ok=True)
    os.makedirs(viz_dir, exist_ok=True)
    
    return csv_dir, viz_dir


def get_output_filename(input_path: str, method: str, window: int, start_year: int, end_year: int, ext: str) -> str:
    """
    Generate dynamic output filename.
    
    Args:
        input_path: Path to input file
        method: MA method name
        window: MA window size
        start_year: Start year
        end_year: End year
        ext: File extension (without dot)
    
    Returns:
        Formatted filename
    """
    stem = Path(input_path).stem
    return f"{stem}_{method}_MA{window}_{start_year}-{end_year}.{ext}"


def save_csv_output(df: pd.DataFrame, output_path: str):
    """Save DataFrame to CSV without metadata comments."""
    df.to_csv(output_path)


def create_visualization(df: pd.DataFrame, method: str, window: int, output_path: str, fmt: str = 'png'):
    """
    Create visualization for MA results.
    
    Args:
        df: DataFrame with MA results
        method: MA method name
        window: MA window size
        output_path: Output file path
        fmt: Output format ('png' or 'pdf')
    """
    plt.figure(figsize=(14, 8))
    
    for country in df.index:
        years = [int(col) for col in df.columns]
        values = df.loc[country].values
        plt.plot(years, values, marker='o', label=country, linewidth=2, markersize=4)
    
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Income', fontsize=12)
    plt.title(f'{method} Moving Average (MA{window})', fontsize=14, fontweight='bold')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()


def save_metadata(
    metadata_path: str,
    args,
    input_path: str,
    window: int,
    interpolation_limit: int,
    initial_nan: int,
    final_nan: int,
    logs: Dict[str, List[str]]
):
    """
    Save metadata file with execution information.
    
    Args:
        metadata_path: Path to metadata file
        args: Parsed arguments
        input_path: Input file path
        window: MA window size
        interpolation_limit: Interpolation limit used
        initial_nan: Initial NaN count
        final_nan: Final NaN count
        logs: Dictionary of logs for each method
    """
    with open(metadata_path, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("MOVING AVERAGE (MIMA) COMPUTATION METADATA\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("INPUT PARAMETERS\n")
        f.write("-" * 80 + "\n")
        f.write(f"Input File: {input_path}\n")
        f.write(f"MA Window Size (N): {window}\n")
        f.write(f"Countries: {args.countries}\n")
        f.write(f"Time Period: {args.start_year} - {args.end_year}\n")
        f.write(f"Output Path: {args.output_path}\n")
        f.write(f"Interpolation Limit: {interpolation_limit} years\n")
        f.write(f"Minimum Required Values: 3 non-NaN per window\n")
        f.write("\n")
        
        f.write("DATA PREPROCESSING\n")
        f.write("-" * 80 + "\n")
        f.write(f"Initial NaN count: {initial_nan}\n")
        f.write(f"Final NaN count (after interpolation): {final_nan}\n")
        f.write(f"NaN values filled: {initial_nan - final_nan}\n")
        f.write("\n")
        
        # Write logs for each method
        for method, method_logs in logs.items():
            f.write("=" * 80 + "\n")
            f.write(f"{method.upper()} MOVING AVERAGE\n")
            f.write("=" * 80 + "\n")
            for log in method_logs:
                f.write(f"{log}\n")
            f.write("\n")


def main():
    """Main execution function."""
    # Parse and validate arguments
    args = parse_arguments()
    validate_arguments(args)
    
    # Parse countries list
    countries = [c.strip() for c in args.countries.split(',')]
    
    print(f"Starting MIMA computation...")
    print(f"  Input: {args.input_path}")
    print(f"  Countries: {countries}")
    print(f"  Years: {args.start_year}-{args.end_year}")
    print(f"  MA Window: {args.ma_number}")
    print(f"  Output: {args.output_path}/MIMA/")
    print()
    
    # Load and filter data
    print("Loading and filtering data...")
    df = load_and_filter_data(args.input_path, countries, args.start_year, args.end_year)
    print(f"  Loaded {len(df)} countries, {len(df.columns)} years")
    
    # Interpolate missing values
    print("Interpolating missing values (limit: 2 years)...")
    df_interpolated, initial_nan, final_nan = interpolate_missing_values(df, limit=2)
    print(f"  Initial NaN: {initial_nan}, Final NaN: {final_nan}, Filled: {initial_nan - final_nan}")
    
    # Create output directories
    csv_dir, viz_dir = create_output_directories(args.output_path)
    
    # Initialize logs
    logs = {}
    
    # Compute Centered MA
    print("\nComputing Centered MA...")
    effective_min_centered = min(3, args.ma_number)
    logs['centered'] = [f"Execution started", f"Window size: {args.ma_number}", f"Minimum periods: {effective_min_centered}"]
    df_centered = compute_centered_ma(df_interpolated, args.ma_number, min_periods=3)
    centered_nan = df_centered.isna().sum().sum()
    logs['centered'].append(f"Result NaN count: {centered_nan}")
    
    # Save Centered MA
    centered_csv = os.path.join(csv_dir, get_output_filename(args.input_path, 'centered', args.ma_number, args.start_year, args.end_year, 'csv'))
    save_csv_output(df_centered, centered_csv)
    logs['centered'].append(f"CSV saved: {centered_csv}")
    
    # Visualize Centered MA
    centered_png = os.path.join(viz_dir, get_output_filename(args.input_path, 'centered', args.ma_number, args.start_year, args.end_year, 'png'))
    centered_pdf = os.path.join(viz_dir, get_output_filename(args.input_path, 'centered', args.ma_number, args.start_year, args.end_year, 'pdf'))
    create_visualization(df_centered, 'Centered', args.ma_number, centered_png, 'png')
    create_visualization(df_centered, 'Centered', args.ma_number, centered_pdf, 'pdf')
    logs['centered'].append(f"Visualizations saved: PNG and PDF")
    print(f"  ✓ Saved: {centered_csv}")
    
    # Compute Trailing MA
    print("Computing Trailing MA...")
    effective_min_trailing = min(3, args.ma_number)
    logs['trailing'] = [f"Execution started", f"Window size: {args.ma_number}", f"Minimum periods: {effective_min_trailing}"]
    df_trailing = compute_trailing_ma(df_interpolated, args.ma_number, min_periods=3)
    trailing_nan = df_trailing.isna().sum().sum()
    logs['trailing'].append(f"Result NaN count: {trailing_nan}")
    
    # Save Trailing MA
    trailing_csv = os.path.join(csv_dir, get_output_filename(args.input_path, 'trailing', args.ma_number, args.start_year, args.end_year, 'csv'))
    save_csv_output(df_trailing, trailing_csv)
    logs['trailing'].append(f"CSV saved: {trailing_csv}")
    
    # Visualize Trailing MA
    trailing_png = os.path.join(viz_dir, get_output_filename(args.input_path, 'trailing', args.ma_number, args.start_year, args.end_year, 'png'))
    trailing_pdf = os.path.join(viz_dir, get_output_filename(args.input_path, 'trailing', args.ma_number, args.start_year, args.end_year, 'pdf'))
    create_visualization(df_trailing, 'Trailing', args.ma_number, trailing_png, 'png')
    create_visualization(df_trailing, 'Trailing', args.ma_number, trailing_pdf, 'pdf')
    logs['trailing'].append(f"Visualizations saved: PNG and PDF")
    print(f"  ✓ Saved: {trailing_csv}")
    
    # Compute Weighted MA
    print("Computing Weighted MA...")
    logs['weighted'] = [f"Execution started", f"Window size: {args.ma_number}"]
    
    if args.ma_number % 2 == 0:
        logs['weighted'].append(f"WARNING: Skipped - Weighted MA requires odd window size (N={args.ma_number} is even)")
        print(f"  ⚠ Skipped (even window size)")
    else:
        effective_min_weighted = min(3, args.ma_number)
        logs['weighted'].append(f"Minimum periods: {effective_min_weighted}")
        logs['weighted'].append(f"Using triangular weights for centered window")
        df_weighted = compute_weighted_ma(df_interpolated, args.ma_number, min_periods=3)
        weighted_nan = df_weighted.isna().sum().sum()
        logs['weighted'].append(f"Result NaN count: {weighted_nan}")
        
        # Save Weighted MA
        weighted_csv = os.path.join(csv_dir, get_output_filename(args.input_path, 'weighted', args.ma_number, args.start_year, args.end_year, 'csv'))
        save_csv_output(df_weighted, weighted_csv)
        logs['weighted'].append(f"CSV saved: {weighted_csv}")
        
        # Visualize Weighted MA
        weighted_png = os.path.join(viz_dir, get_output_filename(args.input_path, 'weighted', args.ma_number, args.start_year, args.end_year, 'png'))
        weighted_pdf = os.path.join(viz_dir, get_output_filename(args.input_path, 'weighted', args.ma_number, args.start_year, args.end_year, 'pdf'))
        create_visualization(df_weighted, 'Weighted', args.ma_number, weighted_png, 'png')
        create_visualization(df_weighted, 'Weighted', args.ma_number, weighted_pdf, 'pdf')
        logs['weighted'].append(f"Visualizations saved: PNG and PDF")
        print(f"  ✓ Saved: {weighted_csv}")
    
    # Save metadata
    metadata_path = os.path.join(csv_dir, get_output_filename(args.input_path, '', args.ma_number, args.start_year, args.end_year, 'txt').replace('__', '_').replace('_MA', '_metadata_MA').replace('.txt', '_metadata.txt'))
    metadata_path = os.path.join(csv_dir, f"{Path(args.input_path).stem}_MA{args.ma_number}_metadata.txt")
    save_metadata(metadata_path, args, args.input_path, args.ma_number, 2, initial_nan, final_nan, logs)
    print(f"\n✓ Metadata saved: {metadata_path}")
    
    print("\n" + "=" * 80)
    print("MIMA COMPUTATION COMPLETE")
    print("=" * 80)
    print(f"All outputs saved to: {args.output_path}/MIMA/")
    print(f"  CSV files: {csv_dir}")
    print(f"  Visualizations: {viz_dir}")


if __name__ == "__main__":
    main()
