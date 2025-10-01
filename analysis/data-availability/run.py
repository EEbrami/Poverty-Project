#!/usr/bin/env python3
"""
Runner for availability submatrix analysis.

- Reads OECD income CSV from: xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv
- Runs 15 phases of Coverage-based pivot shrink algorithm (A1b)
- Writes single consolidated Markdown file to: analysis/data-availability/results/greedy_algorithm/all_phases_summary.md
"""
import os
from pathlib import Path
from typing import Dict

from availability_submatrix import run_all


REPO_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = REPO_ROOT / "xlsxConverted" / "csvFiles" / "dart-med-pop_decomp-dhi.csv"
OUT_DIR = REPO_ROOT / "analysis" / "data-availability" / "results"


def main():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"CSV not found at {CSV_PATH}")
    
    # Run 15 phases and get output path
    results_map = run_all(str(CSV_PATH), str(OUT_DIR), num_phases=15)
    
    # Print results
    output_file = results_map.get("all_phases_summary")
    if output_file:
        print(f"✓ Analysis complete!")
        print(f"✓ Generated: {output_file}")
    else:
        print("⚠ No output generated")


if __name__ == "__main__":
    main()
