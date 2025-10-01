#!/usr/bin/env python3
"""
Runner for availability submatrix analysis.

- Reads OECD income CSV from: xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv
- Writes per-algorithm JSON results to analysis/data-availability/results/
- Writes per-algorithm CSVs (for multi-row algorithms) to analysis/data-availability/results/multiple-rows/
- Writes consolidated summary to analysis/data-availability/summary.md
"""
import csv
import json
import os
from pathlib import Path
from typing import Dict

from availability_submatrix import run_all


REPO_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = REPO_ROOT / "xlsxConverted" / "csvFiles" / "dart-med-pop_decomp-dhi.csv"
OUT_DIR = REPO_ROOT / "analysis" / "data-availability" / "results"
OUT_DIR_MULTI = OUT_DIR / "multiple-rows"
SUMMARY_MD = REPO_ROOT / "analysis" / "data-availability" / "summary.md"


def load_json(p: Path) -> dict:
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def write_summary(results_map: Dict[str, str]) -> None:
    rows = []
    for key, path in results_map.items():
        data = load_json(Path(path))
        if "rows" in data:
            for i, row in enumerate(data["rows"], 1):
                rows.append({
                    "algorithm": f"{key}#row{i}",
                    "num_countries": row.get("num_countries", 0),
                    "length": row.get("length", 0),
                    "partition": row.get("partition", []),
                    "period": row.get("period", []),
                    "countries": row.get("countries", []),
                })
        else:
            rows.append({
                "algorithm": key,
                "num_countries": data.get("num_countries", 0),
                "length": data.get("length", 0),
                "partition": data.get("partition", []),
                "period": data.get("period", []),
                "countries": data.get("countries", []),
            })

    rows.sort(key=lambda r: (r["num_countries"] * r["length"], r["num_countries"], r["length"]), reverse=True)

    os.makedirs(SUMMARY_MD.parent, exist_ok=True)
    with open(SUMMARY_MD, "w", encoding="utf-8") as f:
        f.write("# Data Availability Submatrix Results\n\n")
        f.write("This summary aggregates results from multiple algorithms that search for the largest all-ones submatrix in the country-by-year availability matrix.\n\n")
        f.write("Metrics:\n")
        f.write("- num_countries: number of countries fully covered\n")
        f.write("- length: number of years in the partition\n")
        f.write("- partition: explicit years (for non-consecutive selections); consecutive intervals also show 'period'\n\n")

        f.write("| Rank | Algorithm | Countries | Length | Area | Period | Partition (years) |\n")
        f.write("| ---- | --------- | --------- | ------ | ---- | ------ | ----------------- |\n")
        for i, r in enumerate(rows, 1):
            area = r["num_countries"] * r["length"]
            period = ""
            if r["period"]:
                period = f"{r['period'][0]}–{r['period'][-1]}"
            part_str = ""
            if r["partition"]:
                if r["length"] <= 10:
                    part_str = ", ".join(str(y) for y in r["partition"])
                else:
                    part_str = f"{r['partition'][0]}, …, {r['partition'][-1]} ({r['length']} years)"
            f.write(f"| {i} | {r['algorithm']} | {r['num_countries']} | {r['length']} | {area} | {period} | {part_str} |\n")

        f.write("\n## Top Results Detail\n\n")
        for i, r in enumerate(rows[:5], 1):
            f.write(f"### {i}. {r['algorithm']}\n\n")
            f.write(f"- Countries: {r['num_countries']}\n")
            f.write(f"- Length: {r['length']}\n")
            if r["period"]:
                f.write(f"- Period: {r['period'][0]}–{r['period'][-1]}\n")
            if r["partition"]:
                f.write(f"- Partition (years): {', '.join(str(y) for y in r['partition'])}\n")
            if r["countries"]:
                sample = r["countries"][:20]
                f.write(f"- Countries list (first 20): {', '.join(sample)}")
                if len(r["countries"]) > 20:
                    f.write(f" (+{len(r['countries'])-20} more)")
                f.write("\n")
            f.write("\n")


def main():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"CSV not found at {CSV_PATH}")
    results_map = run_all(str(CSV_PATH), str(OUT_DIR))
    write_summary(results_map)
    print(f"Wrote results to: {OUT_DIR}")
    print(f"Wrote multiple-rows CSVs to: {OUT_DIR_MULTI}")
    print(f"Wrote summary to: {SUMMARY_MD}")


if __name__ == "__main__":
    main()
