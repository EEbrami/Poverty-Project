#!/usr/bin/env python3
"""
Availability submatrix analysis on OECD income CSV.

- Builds binary availability matrix Y: Y[country, year] = 1 if income present, else 0.
- Implements multiple algorithms to find large all-ones submatrices:
  A1. Greedy longest-streak intersection (Phase 1 and Phase 2) as described by the user
  A1b. Coverage-based pivot shrink (records countries that fully cover pivot period, not just equal)
  A2. Best consecutive-year window (max countries fully covered by the interval)
  A3. Two- and three-year moving windows and offset-restricted variants
  A4. Maximum biclique (arbitrary years with full coverage; not necessarily consecutive)

Outputs are JSON objects with:
- num_countries: int
- length: int (number of years in the partition)
- partition: list of years (explicit years; for consecutive windows also includes 'period': [start_year, end_year])
- countries: list of country names (sorted)

Additionally, for algorithms that yield multiple rows (A1 and A1b), CSV summaries are also saved under
analysis/data-availability/results/multiple-rows/ with one row per discovered partition.

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


dataclass
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

def alg_consecutive_window_best(data: AvailabilityData) -> Dict:
    """Find best consecutive-year interval maximizing number of countries with full coverage."""
    df = data.matrix
    years = data.years
    n, T = df.shape
    # Precompute prefix sums for each row
    pref = np.cumsum(df.values, axis=1)
    best = {"num_countries": 0, "length": 0, "partition": [], "period": [], "countries": []}

    for l in range(T):
        for r in range(l, T):  # inclusive r
            L = r - l + 1
            # For each row i: sum[l..r] = pref[i,r] - pref[i,l-1]
            if l == 0:
                window_sums = pref[:, r]
            else:
                window_sums = pref[:, r] - pref[:, l - 1]
            mask = window_sums == L
            cnt = int(mask.sum())
            if cnt > best["num_countries"] or (cnt == best["num_countries"] and L > best["length"]):
                part = years[l : r + 1]
                best = {
                    "num_countries": cnt,
                    "length": L,
                    "partition": part,
                    "period": [part[0], part[-1]],
                    "countries": sorted(df.index[mask].tolist()),
                }
    return best

def alg_window_fixed_length(data: AvailabilityData, L: int, restrict_offsets: Optional[Set[int]] = None) -> Dict:
    """
    Best moving window of fixed length L (consecutive years).
    If restrict_offsets provided, only allow start indices l where l % L in restrict_offsets.
    """
    df = data.matrix
    years = data.years
    n, T = df.shape
    if L <= 0 or L > T:
        return {"num_countries": 0, "length": L, "partition": [], "period": [], "countries": []}

    pref = np.cumsum(df.values, axis=1)
    best = {"num_countries": 0, "length": L, "partition": [], "period": [], "countries": []}

    valid_starts = range(0, T - L + 1)
    if restrict_offsets is not None:
        valid_starts = [l for l in valid_starts if (l % L) in restrict_offsets]

    for l in valid_starts:
        r = l + L - 1
        window_sums = pref[:, r] - (pref[:, l - 1] if l > 0 else 0)
        mask = window_sums == L
        cnt = int(mask.sum())
        if cnt > best["num_countries"]:
            part = years[l : r + 1]
            best = {
                "num_countries": cnt,
                "length": L,
                "partition": part,
                "period": [part[0], part[-1]],
                "countries": sorted(df.index[mask].tolist()),
            }
    return best

def alg_max_biclique(data: AvailabilityData, time_limit_seconds: float = 8.0) -> Dict:
    """
    Exact maximum biclique on bipartite graph (Countries x Years),
    seeking R subset of countries and C subset of years such that every (r,c) is 1, maximizing |R|*|C|.
    Backtracking with simple bounds.

    Returns partition as a sorted list of years and list of countries.
    """
    import time

    years = data.years
    df = data.matrix

    # Build set per country of available years (indices)
    year_idx = list(range(len(years)))
    avail: Dict[str, Set[int]] = {c: set(np.where(df.loc[c].values == 1)[0].tolist()) for c in df.index}

    countries_sorted = sorted(df.index.tolist(), key=lambda c: len(avail[c]), reverse=True)

    best_rows: List[str] = []
    best_cols: Set[int] = set()
    best_area = 0

    start_time = time.time()

    def backtrack(idx: int, chosen_rows: List[str], cols: Set[int]) -> None:
        nonlocal best_rows, best_cols, best_area
        # Time check
        if time.time() - start_time > time_limit_seconds:
            return

        # Current area
        area = len(chosen_rows) * len(cols)
        if area > best_area:
            best_area = area
            best_rows = chosen_rows.copy()
            best_cols = cols.copy()

        # Upper bound if we took all remaining rows with current cols
        remaining = len(countries_sorted) - idx
        ub = (len(chosen_rows) + remaining) * len(cols)
        # Note: cols can only shrink; this UB is weak but cheap.
        if ub <= best_area:
            return

        # If no columns remain, adding rows won't help
        if not cols and chosen_rows:
            return

        # Try to include more rows
        for j in range(idx, len(countries_sorted)):
            c = countries_sorted[j]
            new_cols = cols & avail[c] if chosen_rows else avail[c].copy()
            if not new_cols:
                # Even with this row, no columns; area becomes 0, skip unless we had none selected
                continue
            # Prune if even optimistic bound with new_cols won't exceed best
            optimistic = (len(chosen_rows) + 1 + (len(countries_sorted) - j - 1)) * len(new_cols)
            if optimistic <= best_area:
                continue
            chosen_rows.append(c)
            backtrack(j + 1, chosen_rows, new_cols)
            chosen_rows.pop()

    # Start with empty selection, columns initially "unknown"; we'll set on first row
    backtrack(0, [], set())

    part_years = sorted(years[i] for i in best_cols)
    return {
        "num_countries": len(best_rows),
        "length": len(part_years),
        "partition": part_years,
        "period": [part_years[0], part_years[-1]] if part_years else [],
        "countries": sorted(best_rows),
    }

# ----------------------------
# Output helpers
# ----------------------------

def save_json(obj: Dict, out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def save_rows_csv(rows: List[Dict], out_csv_path: str) -> None:
    """Save multiple-row algorithm output to CSV.
    Columns: row_index, num_countries, length, period_start, period_end, partition_years, countries
    partition_years and countries are semicolon-separated lists.
    """    
    os.makedirs(os.path.dirname(out_csv_path), exist_ok=True)
    records = []
    for idx, r in enumerate(rows, 1):
        period = r.get("period", []) or []
        period_start = period[0] if len(period) >= 1 else ""
        period_end = period[-1] if len(period) >= 1 else ""
        part_list = r.get("partition", []) or []
        countries = r.get("countries", []) or []
        records.append({
            "row_index": idx,
            "num_countries": r.get("num_countries", 0),
            "length": r.get("length", 0),
            "period_start": period_start,
            "period_end": period_end,
            "partition_years": ";".join(str(y) for y in part_list),
            "countries": ";".join(countries),
        })
    pd.DataFrame.from_records(records).to_csv(out_csv_path, index=False)

def run_all(csv_path: str, results_dir: str) -> Dict[str, str]:
    data = load_availability(csv_path)

    outputs: Dict[str, str] = {}

    multi_dir = os.path.join(results_dir, "multiple-rows")

    # A1: Greedy (literal-equality rows)
    res_a1_phase1 = alg_greedy_longest_streak_process(data, phase2_exclude=None, record_equal_only=True)
    out1 = os.path.join(results_dir, "greedy_longest_streak_phase1_equal.json")
    save_json(res_a1_phase1, out1)
    # CSV export for multiple rows
    if res_a1_phase1.get("rows"):
        save_rows_csv(res_a1_phase1["rows"], os.path.join(multi_dir, "greedy_longest_streak_phase1_equal.csv"))
    outputs["greedy_longest_streak_phase1_equal"] = out1

    # Phase 2: exclude countries from first row and repeat
    exclude = set(res_a1_phase1["rows"][0]["countries"]) if res_a1_phase1.get("rows") else set()
    res_a1_phase2 = alg_greedy_longest_streak_process(data, phase2_exclude=exclude, record_equal_only=True)
    out2 = os.path.join(results_dir, "greedy_longest_streak_phase2_equal.json")
    save_json(res_a1_phase2, out2)
    if res_a1_phase2.get("rows"):
        save_rows_csv(res_a1_phase2["rows"], os.path.join(multi_dir, "greedy_longest_streak_phase2_equal.csv"))
    outputs["greedy_longest_streak_phase2_equal"] = out2

    # A1b: Coverage-based pivot shrink (phase 1 and 2)
    res_a1b_phase1 = alg_greedy_longest_streak_process(data, phase2_exclude=None, record_equal_only=False)
    out1b = os.path.join(results_dir, "greedy_pivot_coverage_phase1.json")
    save_json(res_a1b_phase1, out1b)
    if res_a1b_phase1.get("rows"):
        save_rows_csv(res_a1b_phase1["rows"], os.path.join(multi_dir, "greedy_pivot_coverage_phase1.csv"))
    outputs["greedy_pivot_coverage_phase1"] = out1b

    exclude_b = set(res_a1b_phase1["rows"][0]["countries"]) if res_a1b_phase1.get("rows") else set()
    res_a1b_phase2 = alg_greedy_longest_streak_process(data, phase2_exclude=exclude_b, record_equal_only=False)
    out2b = os.path.join(results_dir, "greedy_pivot_coverage_phase2.json")
    save_json(res_a1b_phase2, out2b)
    if res_a1b_phase2.get("rows"):
        save_rows_csv(res_a1b_phase2["rows"], os.path.join(multi_dir, "greedy_pivot_coverage_phase2.csv"))
    outputs["greedy_pivot_coverage_phase2"] = out2b

    # A2: Best consecutive-year window
    res_a2 = alg_consecutive_window_best(data)
    out3 = os.path.join(results_dir, "best_consecutive_window.json")
    save_json(res_a2, out3)
    outputs["best_consecutive_window"] = out3

    # A3: Two-/Three-year moving windows and restricted-offset variants
    res_2_all = alg_window_fixed_length(data, L=2, restrict_offsets=None)
    out4 = os.path.join(results_dir, "best_window_2y_any_start.json")
    save_json(res_2_all, out4)
    outputs["best_window_2y_any_start"] = out4

    res_2_off1 = alg_window_fixed_length(data, L=2, restrict_offsets={0})
    out5 = os.path.join(results_dir, "best_window_2y_offset0.json")
    save_json(res_2_off1, out5)
    outputs["best_window_2y_offset0"] = out5

    res_2_off2 = alg_window_fixed_length(data, L=2, restrict_offsets={1})
    out6 = os.path.join(results_dir, "best_window_2y_offset1.json")
    save_json(res_2_off2, out6)
    outputs["best_window_2y_offset1"] = out6

    res_3_all = alg_window_fixed_length(data, L=3, restrict_offsets=None)
    out7 = os.path.join(results_dir, "best_window_3y_any_start.json")
    save_json(res_3_all, out7)
    outputs["best_window_3y_any_start"] = out7

    res_3_off0 = alg_window_fixed_length(data, L=3, restrict_offsets={0})
    out8 = os.path.join(results_dir, "best_window_3y_offset0.json")
    save_json(res_3_off0, out8)
    outputs["best_window_3y_offset0"] = out8

    res_3_off1 = alg_window_fixed_length(data, L=3, restrict_offsets={1})
    out9 = os.path.join(results_dir, "best_window_3y_offset1.json")
    save_json(res_3_off1, out9)
    outputs["best_window_3y_offset1"] = out9

    res_3_off2 = alg_window_fixed_length(data, L=3, restrict_offsets={2})
    out10 = os.path.join(results_dir, "best_window_3y_offset2.json")
    save_json(res_3_off2, out10)
    outputs["best_window_3y_offset2"] = out10

    # A4: Max biclique (arbitrary years)
    res_a4 = alg_max_biclique(data, time_limit_seconds=8.0)
    out11 = os.path.join(results_dir, "max_biclique_any_years.json")
    save_json(res_a4, out11)
    outputs["max_biclique_any_years"] = out11

    return outputs
