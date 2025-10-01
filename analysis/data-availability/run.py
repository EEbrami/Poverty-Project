#!/usr/bin/env python3
"""
Runner for availability submatrix analysis.

This script runs the Coverage-based pivot shrink algorithm (A1b)
for a configurable number of phases on a specified income CSV.
The output consolidated Markdown file replaces the previous one.
"""
import argparse
import os
import sys
from pathlib import Path
from typing import Dict

from availability_submatrix import run_all


def main():
    parser = argparse.ArgumentParser(
        description="Run the Availability Submatrix analysis for cross-national data.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Define default paths relative to the repository root
    REPO_ROOT = Path(__file__).resolve().parents[2]
    DEFAULT_CSV_PATH = REPO_ROOT / "xlsxConverted" / "csvFiles" / "dart-med-pop_decomp-dhi.csv"
    DEFAULT_OUT_DIR = REPO_ROOT / "analysis" / "data-availability" / "results"
    
    # Argument for CSV File Path
    parser.add_argument(
        "--csv-path",
        type=str,
        default=str(DEFAULT_CSV_PATH),
        help=(
            "Path to the input OECD income CSV file.\n"
            f"Default: {DEFAULT_CSV_PATH}"
        )
    )
    # Argument for Number of Phases
    parser.add_argument(
        "--num-phases",
        type=int,
        default=15,
        help="The number of sequential exclusion phases to run (integer). Default: 15"
    )

    args = parser.parse_args()
    
    # Use arguments
    csv_path = Path(args.csv_path)
    out_dir = DEFAULT_OUT_DIR
    num_phases = args.num_phases

    if not csv_path.exists():
        print(f"Error: CSV not found at {csv_path}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Running analysis on: {csv_path}")
    print(f"Number of phases: {num_phases}")
    
    # Run analysis. The output path is now dynamically generated inside run_all.
    results_map = run_all(str(csv_path), str(out_dir), num_phases=num_phases)
    
    # Print results
    # MODIFIED: Retrieve the path dynamically from the dictionary's single value.
    output_file = None
    if results_map and len(results_map) == 1:
        # Get the path (value) from the single item in the map, 
        # as the key is now the dynamic filename
        output_file = list(results_map.values())[0]
    
    if output_file:
        print(f"✓ Analysis complete!")
        print(f"✓ Generated: {output_file}")
    else:
        print("⚠ No output generated")


if __name__ == "__main__":
    main()
