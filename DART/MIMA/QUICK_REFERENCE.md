# MIMA Quick Reference

## One-Line Command

```bash
./compute_mima.py --ma-number N --countries "C1,C2,..." --start-year YYYY --end-year YYYY --input-path FILE --output-path DIR
```

## Quick Examples

### Standard 5-Year MA
```bash
./compute_mima.py --ma-number 5 --countries "Canada,Germany,France" \
  --start-year 1990 --end-year 2020 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

### Short-Term 3-Year MA
```bash
./compute_mima.py --ma-number 3 --countries "United States" \
  --start-year 2010 --end-year 2020 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

### Long-Term 7-Year MA
```bash
./compute_mima.py --ma-number 7 --countries "Australia,Canada,Japan" \
  --start-year 1985 --end-year 2021 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

## Parameter Constraints

| Parameter | Constraint | Example |
|-----------|------------|---------|
| `--ma-number` | 2 ≤ N ≤ 7 | 5 |
| `--countries` | Exact match to CSV | "Canada,France" |
| `--start-year` | ≤ end-year | 1990 |
| `--end-year` | ≥ start-year | 2020 |
| `--input-path` | File must exist | xlsxConverted/csvFiles/data.csv |
| `--output-path` | Parent dir must exist | DART |

## Output Files

```
[OUTPUT_PATH]/MIMA/
├── csv/
│   ├── [input]_centered_MA[N]_[years].csv
│   ├── [input]_trailing_MA[N]_[years].csv
│   ├── [input]_weighted_MA[N]_[years].csv  (odd N only)
│   └── [input]_MA[N]_metadata.txt
└── visualizations/
    ├── [input]_centered_MA[N]_[years].{png,pdf}
    ├── [input]_trailing_MA[N]_[years].{png,pdf}
    └── [input]_weighted_MA[N]_[years].{png,pdf}  (odd N only)
```

## MA Method Selection Guide

| Method | Use Case | Data Required |
|--------|----------|---------------|
| **Centered** | Historical analysis | Future data available |
| **Trailing** | Real-time monitoring | Past data only |
| **Weighted** | Trend emphasis | Odd window (3,5,7) |

## Common Issues

### "No data found for specified countries"
→ Check exact country names: `head xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv`

### "Weighted MA skipped"
→ Expected for even N (2,4,6). Use odd N for weighted MA.

### Many NaN in output
→ Use smaller window or extend year range

## Key Features

- ✅ Linear interpolation (≤2 year gaps)
- ✅ Minimum 3 non-NaN per window
- ✅ Triangular weights for weighted MA
- ✅ Professional PNG/PDF visualizations
- ✅ Comprehensive metadata logging

## Documentation

- **Full Guide**: `DART/MIMA/README.md`
- **Examples**: `DART/MIMA/EXAMPLES.md`
- **Technical**: `DART/MIMA/IMPLEMENTATION_SUMMARY.md`

## Help

```bash
./compute_mima.py --help
```
