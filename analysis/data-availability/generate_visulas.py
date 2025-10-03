#!/usr/bin/env python3
"""
Generate data availability visualizations for country-by-year CSV data.

This script now exclusively generates professional-grade PNG and PDF heatmaps.
It includes special handling for the LIS documentation matrix format and
options for combined variable analysis and country filtering.
"""

import argparse
import os
import re
from typing import List, Tuple, Optional, Dict

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pycountry


def parse_args():
    """Parse command-line arguments, including visualization options."""
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
        default="#",
        help="Character to render for available data (default: #)",
    )
    parser.add_argument(
        "--include-universal",
        type=str,
        default="true",
        help="Include Universal row showing full availability (default: true)",
    )
    parser.add_argument(
        "--visualization-mode",
        type=str,
        default="vertical-grid-5yr",
        help="Defines the grid style (retained for compatibility)",
    )
    parser.add_argument(
        "--output-format",
        type=str,
        default="png,pdf",
        help="Comma-separated list of output formats (e.g., png, pdf, svg)",
    )
    parser.add_argument(
        "--variables",
        type=str,
        default=None,
        help="Comma-separated list of variables to check for combined availability.",
    )
    parser.add_argument(
        "--countries",
        type=str,
        default=None,
        help="Comma-separated list of ISO 3166-1 alpha-2 country codes to include.",
    )
    return parser.parse_args()


def get_country_name(iso_code: str) -> Optional[str]:
    """Converts an ISO 3166-1 alpha-2 code to a country name."""
    try:
        return pycountry.countries.get(alpha_2=iso_code.upper()).name
    except AttributeError:
        return None


def preprocess_lis_matrix(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """
    Transforms the LIS documentation matrix into a dictionary of
    standardized DataFrames, one for each variable.
    """
    datasets = {}

    years_row = df.iloc[1, 4:]
    countries_row = df.iloc[0, 4:]

    col_map = {}
    current_country = ""
    for i, country_val in enumerate(countries_row):
        if pd.notna(country_val):
            current_country = country_val.split('.')[0]
        year_val = years_row.iloc[i]
        col_map[4 + i] = (current_country, year_val)

    variable_rows = df[df.iloc[:, 2].notna()].index

    for row_idx in variable_rows:
        variable_name = df.iloc[row_idx, 2]
        if not variable_name or pd.isna(variable_name) or "Variable Name" in variable_name:
            continue

        data = []
        for col_idx, (country, year) in col_map.items():
            value = df.iloc[row_idx, col_idx]
            try:
                value = int(float(value)) if pd.notna(value) else 0
            except (ValueError, TypeError):
                value = 0
            data.append({'countries': country, 'year': year, 'value': value})

        if not data:
            continue

        long_df = pd.DataFrame(data)
        wide_df = long_df.pivot_table(index='countries', columns='year', values='value', aggfunc='max').fillna(0).astype(int)

        wide_df.columns = wide_df.columns.astype(str)

        datasets[variable_name] = wide_df.reset_index()

    return datasets


def load_csv_with_years(csv_path: str) -> Dict[str, Tuple[pd.DataFrame, List[int], str]]:
    """
    Load CSV and detect its format. Returns a dictionary of datasets to process.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    df_initial = pd.read_csv(csv_path, header=None)

    datasets = {}

    if "CAPTION" in str(df_initial.iloc[0, 0]):
        processed_datasets = preprocess_lis_matrix(df_initial)
        for var_name, var_df in processed_datasets.items():
            year_cols = [col for col in var_df.columns if col != 'countries']
            years = sorted([int(y) for y in year_cols if y.isdigit()])
            datasets[var_name] = (var_df, years, 'countries')
    else:
        df = pd.read_csv(csv_path)
        entity_col = "countries" if "countries" in df.columns else df.columns[0]

        year_cols = [
            str(col) for col in df.columns
            if str(col).strip().isdigit()
        ]

        if not year_cols:
            raise ValueError("No year columns detected (columns with purely numeric names)")

        years = sorted([int(y) for y in year_cols])

        slug = os.path.splitext(os.path.basename(csv_path))[0]
        datasets[slug] = (df, years, entity_col)

    return datasets


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
    country_list: Optional[List[str]] = None,
) -> Tuple[List[str], pd.DataFrame]:
    """Generate the sorted entity list and the binary availability matrix."""
    if country_list:
        df = df[df[entity_col].isin(country_list)]

    filtered_years = years
    if start_year is not None:
        filtered_years = [y for y in filtered_years if y >= start_year]
    if end_year is not None:
        filtered_years = [y for y in filtered_years if y <= end_year]

    if not filtered_years:
        raise ValueError("No years remain after filtering")

    year_cols_str = [str(y) for y in filtered_years]

    entity_data = []

    temp_df = df.set_index(entity_col)

    for entity, row in temp_df.iterrows():
        availability = [1 if pd.notna(row.get(year_str)) and row.get(year_str) != 0 else 0 for year_str in year_cols_str]
        longest_streak = compute_longest_streak(np.array(availability))
        entity_data.append({'entity': entity, 'streak': longest_streak, 'data': availability})

    matrix_df = pd.DataFrame([item['data'] for item in entity_data], index=[item['entity'] for item in entity_data], columns=filtered_years)
    streak_df = pd.DataFrame(entity_data).set_index('entity')

    sorted_matrix = matrix_df.loc[streak_df.sort_values('streak').index]

    if include_universal:
        sorted_matrix.loc["Universal"] = 1

    return sorted_matrix.index.tolist(), sorted_matrix


def write_image_outputs(
    matrix: pd.DataFrame,
    output_dir: str,
    slug: str,
    args,
):
    """Generate image outputs (PNG/PDF/SVG) using Matplotlib/Seaborn heatmap."""
    plt.figure(figsize=(12, max(6, len(matrix) * 0.3)))

    ax = sns.heatmap(
        matrix,
        cmap="binary",
        linewidths=0.5,
        linecolor="gray",
        cbar=False,
        xticklabels=True,
        yticklabels=True,
        square=True,
    )

    if args.tick_interval > 1 and len(matrix.columns) > 0:
        tick_labels = [
            label.get_text() if int(label.get_text()) % args.tick_interval == 0 else ""
            for label in ax.get_xticklabels()
        ]
        ax.set_xticklabels(tick_labels, rotation=45, ha="right")

    title_text = f"Data Availability for {slug}"
    if len(matrix.columns) > 0:
        title_text += f" ({matrix.columns.min()}-{matrix.columns.max()})"
    ax.set_title(title_text, fontsize=14)
    ax.set_ylabel("Entities (Sorted by Shortest Streak)", fontsize=12)
    ax.set_xlabel("Year", fontsize=12)

    plt.tight_layout()

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

    include_universal = args.include_universal.lower() in ("true", "1", "yes", "y")

    datasets_to_process = load_csv_with_years(args.csv_path)

    country_list = None
    if args.countries:
        country_codes = [code.strip() for code in args.countries.split(',')]
        country_list = [get_country_name(code) for code in country_codes if get_country_name(code)]
        if not country_list:
            print("Warning: No valid country names found for the given ISO codes.")

    # CRITICAL CHANGE: Create a subdirectory based on the input CSV file name
    base_name = os.path.splitext(os.path.basename(args.csv_path))[0]
    output_dir = os.path.join("analysis/data-availability/visuals", base_name)
    os.makedirs(output_dir, exist_ok=True)

    if args.variables:
        variables = [v.strip() for v in args.variables.split(',')]
        combined_df = None
        common_years = None
        entity_col = None

        for var in variables:
            if var in datasets_to_process:
                df, years, ec = datasets_to_process[var]
                df = df.set_index(ec)
                if combined_df is None:
                    combined_df = df
                    common_years = set(years)
                    entity_col = ec
                else:
                    # Align indices and combine
                    combined_df = combined_df.align(df, join='outer', axis=0)[0]
                    combined_df.update(df)
                    combined_df = combined_df.where((combined_df == df) & (combined_df == 1), 0)
                    common_years.intersection_update(years)
            else:
                print(f"Warning: Variable '{var}' not found in the dataset.")

        if combined_df is not None:
            slug = "-".join(variables)
            try:
                entity_names, availability_matrix = generate_availability_data(
                    combined_df.reset_index(),
                    sorted(list(common_years)),
                    entity_col,
                    include_universal,
                    args.start_year,
                    args.end_year,
                    country_list
                )

                formats = [f.strip() for f in args.output_format.lower().split(",")]
                if any(f in formats for f in ["png", "pdf", "svg"]):
                    write_image_outputs(availability_matrix, output_dir, slug, args)

            except Exception as e:
                print(f"Could not process combined dataset '{slug}': {e}")
    else:
        for slug, (df, years, entity_col) in datasets_to_process.items():
            try:
                entity_names, availability_matrix = generate_availability_data(
                    df.copy(),
                    years,
                    entity_col,
                    include_universal,
                    args.start_year,
                    args.end_year,
                    country_list,
                )

                formats = [f.strip() for f in args.output_format.lower().split(",")]
                if any(f in formats for f in ["png", "pdf", "svg"]):
                    write_image_outputs(availability_matrix, output_dir, slug, args)

            except Exception as e:
                print(f"Could not process dataset '{slug}': {e}")


if __name__ == "__main__":
    main()
