#!/usr/bin/env python3
import sys
import pandas as pd
from collections import defaultdict

INPUT_CSV = sys.argv[1] if len(sys.argv) > 1 else "converted_files/our-lis-documentation-availability-matrix - All Waves as of 28-Sep-2025.csv"
OUTPUT_CSV = "oecd_years_all_variables_available.csv"

OECD_COUNTRIES = [
    "Australia","Austria","Belgium","Canada","Chile","Colombia","Costa Rica","Czech Republic",
    "Denmark","Estonia","Finland","France","Germany","Greece","Hungary","Iceland","Ireland","Israel",
    "Italy","Japan","Korea","Latvia","Lithuania","Luxembourg","Mexico","Netherlands","New Zealand",
    "Norway","Poland","Portugal","Slovak Republic","Slovenia","Spain","Sweden","Switzerland",
    "Turkey","United Kingdom","United States"
]

def main():
    df = pd.read_csv(INPUT_CSV, header=None, dtype=str, keep_default_na=False, engine='python')
    first_row = df.iloc[0].tolist()
    country_col_index = first_row.index("Country")
    dataset_start_col = country_col_index + 1
    ncols = df.shape[1]
    year_row = df.iloc[1].tolist()
    unit_row_idx = None
    for ridx in range(len(df)):
        cell = str(df.iat[ridx, 0]).strip()
        if cell.lower() == "unit":
            unit_row_idx = ridx
            break
    if unit_row_idx is None:
        unit_row_idx = 5
    var_start = unit_row_idx + 1
    var_rows = []
    for r in range(var_start, len(df)):
        first_cell = str(df.iat[r, 0]).strip()
        second_cell = str(df.iat[r, 1]).strip() if df.shape[1] > 1 else ""
        if first_cell == "" and second_cell == "" and all(str(df.iat[r, c]).strip()=="" for c in range(dataset_start_col, min(ncols, dataset_start_col+5))):
            break
        if df.shape[1] > 2 and str(df.iat[r, 2]).strip() != "":
            var_rows.append(r)
    avail = df.iloc[var_rows, dataset_start_col:ncols].fillna("").astype(str).applymap(lambda x: x.strip() == "1")
    col_meta = []
    for c in range(dataset_start_col, ncols):
        country = str(df.iat[0, c]).strip()
        year = str(df.iat[1, c]).strip()
        col_meta.append((c, country, year))
    all_vars_per_col = avail.all(axis=0)
    country_years = defaultdict(set)
    for idx_offset, (c, country, year) in enumerate(col_meta):
        try:
            col_bool = all_vars_per_col.iloc[idx_offset]
        except Exception:
            col_bool = False
        if col_bool:
            country_years[country].add(year)
    results = []
    for c in OECD_COUNTRIES:
        years = sorted([y for y in country_years.get(c, set()) if y not in ("", "NA", "nan")], key=lambda x: int(x) if x.isdigit() else x)
        results.append({"country": c, "years_all_vars_available": ";".join(years) if years else ""})
    out_df = pd.DataFrame(results)
    out_df.to_csv(OUTPUT_CSV, index=False)
    for row in results:
        print(f"{row['country']}: {row['years_all_vars_available'] or '(none)'}")
    print(f"\nWrote results to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
