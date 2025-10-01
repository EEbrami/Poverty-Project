#!/usr/bin/env python3
"""
Availability submatrix analysis on OECD income CSV.

- Builds binary availability matrix Y: Y[country, year] = 1 if income present, else 0.
- Implements Coverage-based pivot shrink algorithm (A1b) for 15 sequential exclusion phases.
- Outputs a single Markdown file with all 15 phases in collapsible sections.

Each phase result includes:
- num_countries: int
- length: int (number of years in the partition)
- partition: list of years
- period: [start_year, end_year] (when consecutive)
- countries: list of country names (sorted)

Author: Copilot
"""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple, Set

import numpy as np
import pandas as pd


@dataclass
class AvailabilityData:
    countries: List[str]
    years: List[int]
    matrix: pd.DataFrame  # shape (n_countries, n_years), values {0,1}


def load_availability(csv_path: str) -> AvailabilityData:
    df = pd.read_csv(csv_path)
    # Find the year columns robustly: 4-digit year headers
    year_cols = []
    for col in df.columns:
        if col == "countries":
            continue
        if isinstance(col, str) and re.fullmatch(r"\d{4}", col.strip()):
            year_cols.append(col)
        elif isinstance(col, (int, np.integer)) and 1800 <= int(col) <= 2100:
            year_cols.append(str(col))

    # Fallback: if no regex match (e.g., minor formatting), attempt to parse 4-digit at start
    if not year_cols:
        for col in df.columns:
            if col == "countries":
                continue
            m = re.match(r"^\s*(\d{4})", str(col))
            if m:
                year_cols.append(m.group(1))

    # Deduplicate and sort years ascending
    years = sorted({int(y) for y in year_cols})
    years_str = [str(y) for y in years]

    # Create binary availability
    # Ensure all expected year columns exist; if some are missing, create empty
    for y in years_str:
        if y not in df.columns:
            df[y] = np.nan

    df_bin = (~df[years_str].isna()).astype(int)
    countries = df["countries"].astype(str).tolist()

    df_bin.index = countries
    df_bin.columns = years
    return AvailabilityData(countries=countries, years=years, matrix=df_bin)

def find_continuous_streaks(row: np.ndarray) -> List[Tuple[int, int]]:
    """Return list of (start_idx, end_idx_exclusive) for runs of 1s."""
    streaks: List[Tuple[int, int]] = []
    start: Optional[int] = None
    for i, v in enumerate(row):
        if v == 1 and start is None:
            start = i
        elif (v == 0 or np.isnan(v)) and start is not None:
            streaks.append((start, i))
            start = None
    if start is not None:
        streaks.append((start, len(row)))
    return streaks

def longest_streak(row: np.ndarray) -> Tuple[int, int]:
    """Longest run of 1s in row; ties broken by earliest start. Returns (start, end_excl)."""
    streaks = find_continuous_streaks(row)
    if not streaks:
        return (0, 0)
    best = max(streaks, key=lambda ab: (ab[1] - ab[0], -(ab[0])))
    return best

def interval_equal(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
    return a[0] == b[0] and a[1] == b[1]

def interval_intersection(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return (max(a[0], b[0]), min(a[1], b[1]))

def interval_len(a: Tuple[int, int]) -> int:
    return max(0, a[1] - a[0])

def countries_cover_interval(df_bin: pd.DataFrame, interval: Tuple[int, int]) -> List[str]:
    """Return countries with all ones across the consecutive-year interval [start, end)."""
    if interval_len(interval) <= 0:
        return []
    cols = df_bin.columns.tolist()
    start, end = interval
    win_years = cols[start:end]
    covered = df_bin[win_years].sum(axis=1) == len(win_years)
    return sorted(covered[covered].index.tolist())

def alg_greedy_longest_streak_process(
    data: AvailabilityData, phase2_exclude: Optional[Set[str]] = None, record_equal_only: bool = True
) -> Dict[str, List[Dict]]:
    """
    Implements the user's greedy process:
    - For each country, find longest partition p_k^m.
    - Sort by length descending.
    - Let p^u be the top; iterate countries:
      - if country’s longest partition equals p^u: collect
      - else: record current p^u row, then set p^u := intersection(p^u, p_k^m) and continue
    - Continue until last country.
    Two modes:
      record_equal_only=True: record matched-by-equality countries for each row (literal spec)
      record_equal_only=False: record all countries that fully cover p^u (coverage-based practical variant)
    Returns a dict with list of 'rows' recording: partition years, length, num_countries, countries.
    """
    df_bin = data.matrix.copy()
    if phase2_exclude:
        df_bin = df_bin.loc[[c for c in data.countries if c not in phase2_exclude]]
    n, T = df_bin.shape
    years = data.years

    # Compute longest streak per country
    streaks: List[Tuple[str, Tuple[int, int]]] = []
    for c in df_bin.index:
        s = longest_streak(df_bin.loc[c].values.astype(int))
        streaks.append((c, s))

    # Sort by streak length desc, tiebreak earlier start
    streaks.sort(key=lambda cs: (interval_len(cs[1]), -(cs[1][0])), reverse=True)

    if not streaks or interval_len(streaks[0][1]) == 0:
        return {"rows": []}

    p_u = streaks[0][1]
    equal_countries: List[str] = []
    rows: List[Dict] = []

    def record_row(interval: Tuple[int, int], eq_countries: List[str]) -> None:
        if interval_len(interval) <= 0:
            return
        part_years = years[interval[0] : interval[1]]
        if record_equal_only:
            countries_list = sorted(eq_countries)
        else:
            countries_list = countries_cover_interval(df_bin, interval)
        row = {
            "partition": part_years,
            "period": [part_years[0], part_years[-1]] if part_years else [],
            "length": len(part_years),
            "num_countries": len(countries_list),
            "countries": countries_list,
        }
        rows.append(row)

    # Iterate
    for c, s in streaks:
        if interval_len(p_u) <= 0:
            break
        if interval_equal(s, p_u):
            equal_countries.append(c)
        else:
            # finalize current row
            record_row(p_u, equal_countries)
            # intersect and continue
            p_u = interval_intersection(p_u, s)
            # reset equal collect; this country may match new p_u
            equal_countries = [c] if interval_equal(s, p_u) else []

    # Final row
    if interval_len(p_u) > 0:
        record_row(p_u, equal_countries)

    return {"rows": rows}

# ----------------------------
# Output helpers
# ----------------------------

def save_json(obj: Dict, out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def save_all_phases_to_markdown(all_phase_results: Dict[str, List[Dict]], output_md_path: str) -> None:
    """
    Save all phase results to a single Markdown file with collapsible sections.
    
    Args:
        all_phase_results: Dict with keys like "Phase 1", "Phase 2", etc., and values as list of row dicts
        output_md_path: Path to output .md file
    """
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write("# Data Availability Analysis: 15-Phase Greedy Coverage Algorithm\n\n")
        f.write("This document contains results from 15 sequential exclusion phases using the ")
        f.write("Coverage-based pivot shrink (A1b) algorithm.\n\n")
        f.write("Each phase excludes countries from previous phases and finds the optimal ")
        f.write("submatrix of remaining data.\n\n")
        
        # Sort phases by number (Phase 1, Phase 2, etc.)
        phase_keys = sorted(all_phase_results.keys(), 
                          key=lambda x: int(x.split()[1]) if len(x.split()) > 1 else 0)
        
        for phase_key in phase_keys:
            rows = all_phase_results[phase_key]
            
            # Extract phase number for heading
            phase_num = phase_key.split()[1] if len(phase_key.split()) > 1 else "?"
            
            # Write phase heading for GitHub TOC
            f.write(f"## Phase {phase_num}\n\n")
            
            if not rows:
                f.write("*No results found for this phase.*\n\n")
                continue
            
            # Prepare data for DataFrame
            table_data = []
            for idx, row in enumerate(rows, 1):
                countries_str = ";".join(row.get("countries", []))
                period = row.get("period", [])
                period_str = f"{period[0]}-{period[-1]}" if len(period) >= 2 else ""
                
                table_data.append({
                    "period": period_str,
                    "length": row.get("length", 0),
                    "num_countries": row.get("num_countries", 0),
                    "countries": countries_str
                })
            
            # Create DataFrame and convert to markdown
            df = pd.DataFrame(table_data)
            
            # Wrap in collapsible details section
            f.write(f"<details>\n")
            f.write(f"<summary>Click to view full partition results for Phase {phase_num}...</summary>\n\n")
            
            # Write the markdown table
            f.write(df.to_markdown(index=False))
            f.write("\n\n")
            
            f.write("</details>\n\n")



def run_all(csv_path: str, results_dir: str, num_phases: int = 15) -> Dict[str, str]:
    """
    Run the Coverage-based pivot shrink (A1b) algorithm for multiple sequential phases.
    
    Each phase excludes countries found in previous phases and runs the algorithm again
    on the remaining dataset.
    
    Args:
        csv_path: Path to input CSV file
        results_dir: Directory for output files
        num_phases: Number of sequential exclusion phases to run (default: 15)
    
    Returns:
        Dictionary with single key "all_phases_summary" mapping to the output markdown path
    """
    data = load_availability(csv_path)
    
    # Collect results from all phases
    all_phase_results: Dict[str, List[Dict]] = {}
    
    # Track countries to exclude across all phases
    cumulative_exclude: Set[str] = set()
    
    for phase_num in range(1, num_phases + 1):
        phase_key = f"Phase {phase_num}"
        
        # Run the algorithm with cumulative exclusions
        phase_exclude = cumulative_exclude if cumulative_exclude else None
        result = alg_greedy_longest_streak_process(
            data, 
            phase2_exclude=phase_exclude, 
            record_equal_only=False  # Coverage-based (A1b)
        )
        
        rows = result.get("rows", [])
        all_phase_results[phase_key] = rows
        
        # If we got results, add the first row's countries to exclusion list for next phase
        if rows and len(rows) > 0:
            first_row_countries = set(rows[0].get("countries", []))
            cumulative_exclude.update(first_row_countries)
        else:
            # No more results possible, stop early
            break
    
    # Create output directory for markdown file
    greedy_dir = os.path.join(results_dir, "greedy_algorithm")
    os.makedirs(greedy_dir, exist_ok=True)
    
    # Save all results to single markdown file
    output_md_path = os.path.join(greedy_dir, "all_phases_summary.md")
    save_all_phases_to_markdown(all_phase_results, output_md_path)
    
    return {"all_phases_summary": output_md_path}

