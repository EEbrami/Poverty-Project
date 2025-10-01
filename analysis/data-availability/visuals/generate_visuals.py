#!/usr/bin/env python3
"""
Generate data availability visualizations for country-by-year CSV data.

Produces text/md outputs with selectable grid styles and/or professional PNG/PDF
image heatmaps.
"""

import argparse
import os
import re
from typing import List, Tuple, Optional

import numpy as np
import pandas as pd

# New imports for image generation (must be installed via workflow)
import matplotlib.pyplot as plt
import seaborn as sns


def parse_args():
    """Parse command-line arguments, including new visualization options."""
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
        default="#", # Using '#' for safety, as configured in the YAML
        help="Character to render for available data (default: #)",
    )
    parser.add_argument(
        "--include-universal",
        type=str,
        default="true",
        help="Include Universal row showing full availability (default: true)",
    )
    
    # NEW ARGUMENTS FOR VISUALIZATION CONTROL
    parser.add_argument(
        "--visualization-mode",
        type=str,
        default="vertical-grid-5yr",
        help="Defines the grid style for text/md output (e.g., minimal-ticks, vertical-grid-5yr, vertical-grid-1yr)",
    )
    parser.add_argument(
        "--output-format",
        type=str,
        # UPDATED DEFAULT: Ensures image formats are generated on push trigger.
        default="text,md,png,pdf", 
        help="Comma-separated list of output formats (e.g., text, md, png, pdf, svg)",
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


def generate_availability_data(
    df: pd.DataFrame,
    years: List[int],
    entity_col: str,
    include_universal: bool,
    start_year: Optional[int] = None,
    end_year: Optional[int] = None,
) -> Tuple[List[str], pd.DataFrame]:
    """
    Generate the sorted entity list and the binary availability matrix (1=available, 0=missing).
    
    Returns:
        entity_names: List of entity names (including Universal, if present), sorted by longest streak.
        availability_matrix: Pandas DataFrame (Entities x Years) with 0/1 values.
    """
    filtered_years = years
    if start_year is not None:
        filtered_years = [y for y in filtered_years if y >= start_year]
    if end_year is not None:
        filtered_years = [y for y in filtered_years if y <= end_year]
    
    if not filtered_years:
        raise ValueError("No years remain after filtering")
    
    year_cols = [str(y) for y in filtered_years]
    
    data = []
    entity_data = [] # Stores (entity, longest_streak) for sorting
    
    for _, row in df.iterrows():
        entity = str(row[entity_col])
        availability = []
        for year_str in year_cols:
            if year_str in df.columns:
                val = row[year_str]
                availability.append(1 if pd.notna(val) else 0)
            else:
                availability.append(0)
        
        availability_array = np.array(availability)
        longest_streak = compute_longest_streak(availability_array)
        
        data.append(availability)
        entity_data.append((entity, longest_streak))

    matrix = pd.DataFrame(data, index=[e[0] for e in entity_data], columns=filtered_years)
    
    # Sort matrix rows by longest streak (ascending)
    entity_data.sort(key=lambda x: x[1])
    sorted_entities = [e[0] for e in entity_data]
    matrix = matrix.loc[sorted_entities]
    
    # Add Universal row if requested
    if include_universal:
        matrix.loc["Universal"] = 1
        sorted_entities.append("Universal")
        
    return sorted_entities, matrix


def generate_text_grid(
    entity_names: List[str],
    matrix: pd.DataFrame,
    args,
) -> Tuple[List[str], str]:
    """Generate the list of text grid lines and the final tick line, incorporating grid modes."""
    
    min_year, max_year = matrix.columns.min(), matrix.columns.max()
    num_years = len(matrix.columns)
    
    # Using '█' (U+2588) for the text grid
    glyph = args.glyph if args.glyph != "#" else "█"
    
    grid_lines = []
    for entity in entity_names:
        row = matrix.loc[entity].values
        longest_streak = compute_longest_streak(row) if entity != "Universal" else num_years
        
        grid_chars = []
        for i, val in enumerate(row):
            char = glyph if val == 1 else " "
            
            # Apply vertical grid lines based on mode
            if args.visualization_mode == "vertical-grid-5yr":
                if (i % args.tick_interval == 0) and i != 0:
                    grid_chars.append("|")
            elif args.visualization_mode == "vertical-grid-1yr":
                if i != 0:
                    grid_chars.append("|")
            
            # Apply row shading/alternating glyphs
            if args.visualization_mode == "alt-row-shading":
                 if entity_names.index(entity) % 2 == 1:
                     char = char.replace(glyph, "#") # Simple way to shade using a different glyph
            
            grid_chars.append(char)
        
        grid_line_content = "".join(grid_chars).strip()

        # Format: "{entity:<15} | {longest_streak:2d} | {grid_line_content}"
        grid_lines.append(f"{entity:<15} | {longest_streak:2d} | {grid_line_content}")
    
    # --- Generate Tick Line (Aligned with Grid) ---
    tick_line_content = ""
    for i, year in enumerate(matrix.columns):
        if args.visualization_mode == "vertical-grid-5yr":
            if (i % args.tick_interval == 0) and i != 0:
                tick_line_content += " " # Spacing for the | grid character
        elif args.visualization_mode == "vertical-grid-1yr":
            if i != 0:
                tick_line_content += " "
                
        # Simple year marker every tick_interval
        if year % args.tick_interval == 0 or i == 0:
            tick_line_content += str(year)
            # Add spacing only after the year label to align the next mark
            if i + 1 < num_years:
                tick_line_content += " " * (args.tick_interval - len(str(year)))
        else:
            tick_line_content += " "
            
    # Final tick line construction
    # Pad for Entity (15 chars) + ' | ' (3 chars) + LS (2 chars) + ' | ' (3 chars)
    # Pad length = 15 + 3 + 2 + 3 = 23 chars
    tick_line = " " * 23 + tick_line_content
    
    return grid_lines, tick_line


def write_text_outputs(
    grid_lines: List[str],
    tick_line: str,
    matrix: pd.DataFrame,
    output_dir: str,
    slug: str,
    args,
):
    """Write the .txt and .md output files."""
    
    min_year, max_year = matrix.columns.min(), matrix.columns.max()
    num_years = len(matrix.columns)
    num_entities = len(matrix) - (1 if "Universal" in matrix.index else 0)
    
    # Use the block glyph for clear legend, regardless of the argparse glyph
    legend_glyph = "█"
    
    # --- Write .txt file ---
    if "text" in args.output_format.lower().split(","):
        txt_path = os.path.join(output_dir, f"{slug}-availability.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("Data Availability Visualization\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Source: {args.csv_path}\n")
            f.write(f"Year range: {min_year}-{max_year} ({num_years} years)\n")
            f.write(f"Number of entities: {num_entities}\n\n")
            f.write("Legend:\n")
            f.write(f"  {legend_glyph} = Data available for that year\n")
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
            if "Universal" in matrix.index:
                f.write("The 'Universal' row shows full availability across all years.\n")
        
        print(f"Generated text output: {txt_path}")

    # --- Write .md file ---
    if "md" in args.output_format.lower().split(","):
        md_path = os.path.join(output_dir, f"{slug}-availability.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("# Data Availability Visualization\n\n")
            f.write(f"This visualization shows data availability across years {min_year}-{max_year} ")
            f.write(f"for entities in the source file `{args.csv_path}`. ")
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
            f.write(f"- **Tick interval**: {args.tick_interval} years\n")
            f.write(f"- **Sorting**: Entities are sorted by shortest longest-streak first\n\n")
            f.write(f"**Legend**: `{legend_glyph}` = data available, ` ` (space) = data not available\n")
            f.write("**LS** = Longest Streak (maximum consecutive years with data)\n\n")
            if "Universal" in matrix.index:
                f.write("The **Universal** row shows complete availability across all years.\n")
        
        print(f"Generated Markdown output: {md_path}")


def write_image_outputs(
    matrix: pd.DataFrame,
    output_dir: str,
    slug: str,
    args,
):
    """Generate image outputs (PNG/PDF) using Matplotlib/Seaborn."""
    
    # Use the binary matrix for the heatmap directly.
    # The original matrix has 1 for Available and 0 for Missing.
    # The 'binary' cmap maps high values (1) to black and low values (0) to white.
    image_matrix = matrix.copy() # CRITICAL FIX: Removed the incorrect inversion line.
    
    # Heatmap visualization is ideal for professional data availability grids
    plt.figure(figsize=(12, max(6, len(image_matrix) * 0.3)))
    
    # Generate the heatmap
    ax = sns.heatmap(
        image_matrix,
        cmap="binary", # Binary map: High (1/Available) -> Black. Low (0/Missing) -> White.
        linewidths=0.5, # CRITICAL: Adds definite grid lines between cells
        linecolor="gray",
        cbar=False, # No color bar needed
        xticklabels=matrix.columns.values,
        yticklabels=matrix.index.values,
        square=True,
    )
    
    # Make the X-axis year ticks more visible
    if args.tick_interval > 1:
        # Only show labels at the tick interval positions
        xtick_labels = [
            label if year % args.tick_interval == 0 else ""
            for year, label in zip(matrix.columns, ax.get_xticklabels())
        ]
        ax.set_xticklabels(xtick_labels)

    ax.set_title(f"Data Availability for {slug} ({matrix.columns.min()}-{matrix.columns.max()})", fontsize=14)
    ax.set_ylabel("Entities (Sorted by Shortest Streak)", fontsize=12)
    ax.set_xlabel("Year", fontsize=12)
    
    plt.tight_layout()

    # Save outputs based on requested formats
    formats = [f.strip() for f in args.output_format.lower().split(",")]
    
    for fmt in formats:
        if fmt in ("png", "pdf", "svg"):
            output_path = os.path.join(output_dir, f"{slug}-availability.{fmt}")
            plt.savefig(output_path)
            print(f"Generated image output: {output_path}")

    plt.close()


def main():
    """Main entry point."""
    args = parse_args()
    
    # Parse include_universal boolean
    include_universal = args.include_universal.lower() in ("true", "1", "yes", "y")
    
    # Load CSV
    df, years, entity_col = load_csv_with_years(args.csv_path)
    
    # Generate core availability data (sorted entities and binary matrix)
    entity_names, availability_matrix = generate_availability_data(
        df,
        years,
        entity_col,
        include_universal,
        args.start_year,
        args.end_year,
    )
    
    # Extract slug from CSV filename
    csv_filename = os.path.basename(args.csv_path)
    slug = os.path.splitext(csv_filename)[0]
    
    # Define output directory
    output_dir = os.path.join(
        os.path.dirname(__file__),
        ""
    )
    os.makedirs(output_dir, exist_ok=True)

    formats = [f.strip() for f in args.output_format.lower().split(",")]

    # --- Generate Text/MD Outputs (If requested) ---
    if "text" in formats or "md" in formats:
        grid_lines, tick_line = generate_text_grid(entity_names, availability_matrix, args)
        write_text_outputs(grid_lines, tick_line, availability_matrix, output_dir, slug, args)
    
    # --- Generate Image Outputs (If requested) ---
    if "png" in formats or "pdf" in formats or "svg" in formats:
        # Note: Image generation uses the raw matrix data (Entity x Year)
        write_image_outputs(availability_matrix, output_dir, slug, args)
        

if __name__ == "__main__":
    main()
