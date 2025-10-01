# Data Availability Submatrix Analysis

This module analyzes the OECD income dataset to find large all-ones submatrices within the country-by-year availability matrix (1 if income is present for a country in a year; 0 otherwise).

It implements several algorithms:
- Greedy longest-streak intersection (Phase 1 and Phase 2 as specified)
- Coverage-based pivot shrink (practical variant that records all countries covering the pivot)
- Best consecutive-year window
- Fixed 2- and 3-year window variants (including offset restrictions)
- Max biclique (arbitrary years, exact, with time limit + pruning)

## Input

- CSV: xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv
- Column "countries" for country names; remaining columns are expected to be 4-digit years.

## Output

Each algorithm writes a JSON file in analysis/data-availability/results/ with:
- num_countries: int
- length: int (number of years in the partition)
- partition: list of years
- period: [start_year, end_year] (when consecutive)
- countries: list of countries

For algorithms that may produce multiple rows (greedy variants), an extra CSV is written per algorithm to:
- analysis/data-availability/results/multiple-rows/
with columns:
- row_index, num_countries, length, period_start, period_end, partition_years (semicolon-delimited), countries (semicolon-delimited)

A consolidated summary is generated at:
- analysis/data-availability/summary.md

## How to run

From repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r analysis/data-availability/requirements.txt
python analysis/data-availability/run.py
```

Results will be written to analysis/data-availability/results/, multi-row CSVs to analysis/data-availability/results/multiple-rows/, and a summary to analysis/data-availability/summary.md.

## Algorithms

- Greedy longest-streak (Phase 1): Sort countries by their longest consecutive-ones streak p_k^m. Start with the largest p^u and collect countries whose p_k^m exactly equals p^u. On the first non-match, record the row and shrink p^u by intersecting with the new country's p_k^m. Repeat. Phase 2 repeats on the dataset with the Phase 1 first-row countries removed.
- Greedy pivot coverage: Same mechanics as above, but each recorded pivot interval includes all countries that fully cover the interval (not only those whose longest streak equals it).
- Best consecutive window: Searches all year intervals [l, r] and picks the interval with the largest number of fully covered countries (ties broken by longer interval).
- Fixed L-year windows: Picks the best L-year moving window overall; offset-restricted variants limit start positions to l % L in {offset}.
- Max biclique: Exact backtracking search to find an arbitrary set of years and countries forming a full rectangle of ones, maximizing area (num_countries × length). Limited by a small time budget with pruning.
