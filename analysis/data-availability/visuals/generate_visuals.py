#!/usr/bin/env python3
"""
Generate data availability visualizations for country-by-year CSV data.

Produces two outputs:
1. A plain text file (.txt) with a grid visualization
2. A Markdown file (.md) with the same grid in a code fence plus summary

The grid shows data availability across years for each country/entity,
with rows sorted by ascending longest streak length.
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional

import numpy as np
import pandas as pd


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate data availability visualizations from CSV"
    )
    parser.add_argument(
        "--csv-path",
        required=True,
        help="Path to the input CSV file (relative to repo root)",
    )
    parser.add_argument(
        "--start-year",
        type=int,
        default=None,
        help="Clip to years >= start_year (optional)",
    )
    parser.add_argument(
        "--end-year",
        type=int,
        default=None,
        help="Clip to years <= end_year (optional)",
    )
    parser.add_argument(
        "--tick-interval",
        type=int,
        default=5,
        help="Tick mark spacing for x-axis (default: 5)",
    )
    parser.add_argument(
        "--glyph",
        type=str,
        default="█",
        help="Character to render for available data (default: █)",
    )
    parser.add_argument(
        "--include-universal",
        type=str,
        default="true",
        help="Include Universal row showing full availability (default: true)",
    )
    return parser.parse_args()


def load_csv_with_years(csv_path: str) -> Tuple[pd.DataFrame, List[int], str]:
    """
    Load CSV and detect entity column and year columns.
    
    Returns:
        df: DataFrame with the data
        years: List of year integers (sorted)
        entity_col: Name of the entity column
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    
    df = pd.read_csv(csv_path)
    
    # Detect entity column: prefer "countries", else use first column
    if "countries" in df.columns:
        entity_col = "countries"
    else:
        entity_col = df.columns[0]
    
    # Detect year columns: purely numeric column names
    year_cols = []
    for col in df.columns:
        if col == entity_col:
            continue
        # Check if column name is all digits
        if isinstance(col, str) and re.fullmatch(r"\d+", col.strip()):
            year_cols.append(col.strip())
        elif isinstance(col, (int, np.integer)):
            year_cols.append(str(col))
    
    if not year_cols:
        raise ValueError("No year columns detected (columns with purely numeric names)")
    
    # Convert to integers and sort
    years = sorted([int(y) for y in year_cols])
    
    return df, years, entity_col


def compute_partitions(availability_row: np.ndarray, years: List[int]) -> str:
    """
    Compute partition string for a row.
    
    Returns string like "1987-1992;2004-2007" for streaks of available data.
    """
    partitions = []
    in_streak = False
    start_idx = None
    
    for i, val in enumerate(availability_row):
        if val == 1 and not in_streak:
            start_idx = i
            in_streak = True
        elif val == 0 and in_streak:
            partitions.append(f"{years[start_idx]}-{years[i-1]}")
            in_streak = False
    
    if in_streak:
        partitions.append(f"{years[start_idx]}-{years[len(availability_row)-1]}")
    
    return ";".join(partitions) if partitions else ""


def compute_longest_streak(availability_row: np.ndarray) -> int:
    """Compute the longest contiguous streak of available data."""
    max_streak = 0
    current_streak = 0
    
    for val in availability_row:
        if val == 1:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
    
    return max_streak


def generate_grid(
    df: pd.DataFrame,
    years: List[int],
    entity_col: str,
    glyph: str,
    include_universal: bool,
    start_year: Optional[int] = None,
    end_year: Optional[int] = None,
) -> Tuple[List[Tuple[str, int, str]], List[int]]:
    """
    Generate the grid data for visualization.
    
    Returns:
        rows: List of (entity_name, longest_streak, grid_line) tuples
        filtered_years: The years after filtering
    """
    # Filter years if needed
    filtered_years = years
    if start_year is not None:
        filtered_years = [y for y in filtered_years if y >= start_year]
    if end_year is not None:
        filtered_years = [y for y in filtered_years if y <= end_year]
    
    if not filtered_years:
        raise ValueError("No years remain after filtering")
    
    # Get year column names as strings
    year_cols = [str(y) for y in filtered_years]
    
    # Build availability matrix
    rows = []
    for _, row in df.iterrows():
        entity = str(row[entity_col])
        
        # Check availability for each year
        availability = []
        for year_str in year_cols:
            if year_str in df.columns:
                val = row[year_str]
                availability.append(1 if pd.notna(val) else 0)
            else:
                availability.append(0)
        
        availability_array = np.array(availability)
        longest_streak = compute_longest_streak(availability_array)
        
        # Generate grid line
        grid_chars = [glyph if av == 1 else " " for av in availability]
        grid_line = "".join(grid_chars)
        
        rows.append((entity, longest_streak, grid_line))
    
    # Sort by longest streak (ascending)
    rows.sort(key=lambda x: x[1])
    
    # Add Universal row if requested
    if include_universal:
        universal_grid = glyph * len(filtered_years)
        rows.append(("Universal", len(filtered_years), universal_grid))
    
    return rows, filtered_years


def generate_tick_line(years: List[int], tick_interval: int) -> str:
    """Generate x-axis tick line with year labels at intervals."""
    if not years:
        return ""
    
    # Build tick line
    tick_chars = []
    tick_labels = []
    
    for i, year in enumerate(years):
        if i == 0 or (year % tick_interval == 0):
            # This is a tick position
            tick_labels.append((i, str(year)))
    
    # Create the tick line with proper spacing
    # We need to align the year labels with their positions
    tick_line_parts = [" "] * len(years)
    
    # For each tick, place its label
    label_positions = []
    for pos, label in tick_labels:
        label_positions.append((pos, label))
    
    # Build a line with years at tick positions
    # We'll create multiple lines if needed to avoid overlap
    tick_line = " " * 18  # Padding for entity name and longest_streak columns
    
    # Simple approach: show years every tick_interval
    for i, year in enumerate(years):
        if (year % tick_interval == 0):
            # Mark this position
            tick_line += str(year)
            # Add spacing to next tick
            remaining = tick_interval - len(str(year))
            if i + remaining < len(years):
                tick_line += " " * remaining
        # else:
        #     tick_line += " "
    
    return tick_line


def write_outputs(
    rows: List[Tuple[str, int, str]],
    years: List[int],
    tick_interval: int,
    output_dir: str,
    slug: str,
    csv_path: str,
):
    """Write the .txt and .md output files."""
    os.makedirs(output_dir, exist_ok=True)
    
    txt_path = os.path.join(output_dir, f"{slug}-availability.txt")
    md_path = os.path.join(output_dir, f"{slug}-availability.md")
    
    # Generate header
    min_year = min(years)
    max_year = max(years)
    num_years = len(years)
    num_entities = len(rows) - (1 if rows and rows[-1][0] == "Universal" else 0)
    
    # Generate the grid content
    grid_lines = []
    for entity, longest_streak, grid_line in rows:
        # Format: "{entity:<15} | {longest_streak:2d} | {grid_line}"
        grid_lines.append(f"{entity:<15} | {longest_streak:2d} | {grid_line}")
    
    # Generate tick line
    tick_line = " " * 18 + "| " + " " * 3 + "| "
    for i, year in enumerate(years):
        if year % tick_interval == 0:
            year_str = str(year)
            tick_line += year_str
            # Add spacing to align with next tick
            spacing = tick_interval - 1  # One character already used by this year's last digit
            if i + spacing < len(years):
                tick_line += " " * spacing
    
    # Write .txt file
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("Data Availability Visualization\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Source: {csv_path}\n")
        f.write(f"Year range: {min_year}-{max_year} ({num_years} years)\n")
        f.write(f"Number of entities: {num_entities}\n\n")
        f.write("Legend:\n")
        f.write("  █ = Data available for that year\n")
        f.write("    = Data not available\n\n")
        f.write("Entity          | LS | Availability by Year\n")
        f.write("-" * 60 + "\n")
        for line in grid_lines:
            f.write(line + "\n")
        f.write("\n")
        f.write(tick_line + "\n")
        f.write("\n")
        f.write("Note: LS = Longest Streak (max consecutive years with data)\n")
        f.write("Entities are sorted by ascending longest streak.\n")
        if rows and rows[-1][0] == "Universal":
            f.write("The 'Universal' row shows full availability across all years.\n")
    
    # Write .md file
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Data Availability Visualization\n\n")
        f.write(f"This visualization shows data availability across years {min_year}-{max_year} ")
        f.write(f"for entities in the source file `{csv_path}`. ")
        f.write(f"The grid displays {num_entities} entities with their availability patterns.\n\n")
        f.write("```\n")
        f.write("Entity          | LS | Availability by Year\n")
        f.write("-" * 60 + "\n")
        for line in grid_lines:
            f.write(line + "\n")
        f.write("\n")
        f.write(tick_line + "\n")
        f.write("```\n\n")
        f.write("## Summary\n\n")
        f.write(f"- **Number of entities**: {num_entities}\n")
        f.write(f"- **Year range**: {min_year}-{max_year}\n")
        f.write(f"- **Total years**: {num_years}\n")
        f.write(f"- **Tick interval**: {tick_interval} years\n")
        f.write(f"- **Sorting**: Entities are sorted by shortest longest-streak first\n\n")
        f.write("**Legend**: `█` = data available, ` ` (space) = data not available\n")
        f.write("**LS** = Longest Streak (maximum consecutive years with data)\n\n")
        if rows and rows[-1][0] == "Universal":
            f.write("The **Universal** row shows complete availability across all years.\n")
    
    print(f"Generated: {txt_path}")
    print(f"Generated: {md_path}")


def main():
    """Main entry point."""
    args = parse_args()
    
    # Parse include_universal boolean
    include_universal = args.include_universal.lower() in ("true", "1", "yes", "y")
    
    # Load CSV
    df, years, entity_col = load_csv_with_years(args.csv_path)
    
    # Generate grid
    rows, filtered_years = generate_grid(
        df,
        years,
        entity_col,
        args.glyph,
        include_universal,
        args.start_year,
        args.end_year,
    )
    
    # Extract slug from CSV filename
    csv_filename = os.path.basename(args.csv_path)
    slug = os.path.splitext(csv_filename)[0]
    
    # Write outputs
    output_dir = os.path.join(
        os.path.dirname(__file__),
        ""  # Current directory (analysis/data-availability/visuals/)
    )
    write_outputs(
        rows,
        filtered_years,
        args.tick_interval,
        output_dir,
        slug,
        args.csv_path,
    )


if __name__ == "__main__":
    main()
