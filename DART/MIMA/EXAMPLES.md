# MIMA Workflow - Quick Start Examples

This document provides practical, ready-to-use examples for running the MIMA (Moving Average) workflow.

## Prerequisites

Ensure you have Python 3.x installed with the following packages:
- pandas
- numpy
- matplotlib
- seaborn

## Basic Usage Pattern

```bash
python3 compute_mima.py \
  --ma-number [WINDOW_SIZE] \
  --countries "[COUNTRY1,COUNTRY2,...]" \
  --start-year [YYYY] \
  --end-year [YYYY] \
  --input-path [INPUT_CSV] \
  --output-path [OUTPUT_DIR]
```

## Example 1: Standard 5-Year Moving Average

Compute a 5-year moving average for Canada, France, and Germany from 1990 to 2020:

```bash
python3 compute_mima.py \
  --ma-number 5 \
  --countries "Canada,France,Germany" \
  --start-year 1990 \
  --end-year 2020 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

**Output:**
- 3 CSV files (centered, trailing, weighted)
- 6 visualization files (PNG + PDF for each method)
- 1 metadata file

**Output location:** `DART/MIMA/`

## Example 2: Short-Term Trend (3-Year Window)

For analyzing recent trends with minimal smoothing:

```bash
python3 compute_mima.py \
  --ma-number 3 \
  --countries "United States,United Kingdom,Japan" \
  --start-year 2010 \
  --end-year 2020 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

**Use case:** Quick response to recent economic changes, policy analysis

## Example 3: Long-Term Structural Trends (7-Year Window)

For identifying deep structural changes:

```bash
python3 compute_mima.py \
  --ma-number 7 \
  --countries "Australia,Canada,France,Germany,Italy,Spain,United Kingdom" \
  --start-year 1985 \
  --end-year 2021 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

**Use case:** Long-term poverty trends, multi-decade comparisons

## Example 4: Even Window (Skips Weighted MA)

Using an even window size (only centered and trailing MA computed):

```bash
python3 compute_mima.py \
  --ma-number 4 \
  --countries "Canada,Germany" \
  --start-year 2000 \
  --end-year 2020 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

**Note:** Weighted MA will be skipped (logged in metadata)

## Example 5: Single Country Analysis

Focus on one country with maximum detail:

```bash
python3 compute_mima.py \
  --ma-number 5 \
  --countries "United States" \
  --start-year 1980 \
  --end-year 2021 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

## Example 6: Custom Output Location

Specify a different output directory:

```bash
python3 compute_mima.py \
  --ma-number 5 \
  --countries "Canada,Mexico" \
  --start-year 2000 \
  --end-year 2020 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path /path/to/custom/output
```

**Output location:** `/path/to/custom/output/MIMA/`

## Understanding Output Files

After running any example, you'll find:

### CSV Files
```
DART/MIMA/csv/
├── [input_name]_centered_MA[N]_[years].csv
├── [input_name]_trailing_MA[N]_[years].csv
├── [input_name]_weighted_MA[N]_[years].csv  (only for odd N)
└── [input_name]_MA[N]_metadata.txt
```

### Visualizations
```
DART/MIMA/visualizations/
├── [input_name]_centered_MA[N]_[years].png
├── [input_name]_centered_MA[N]_[years].pdf
├── [input_name]_trailing_MA[N]_[years].png
├── [input_name]_trailing_MA[N]_[years].pdf
├── [input_name]_weighted_MA[N]_[years].png  (only for odd N)
└── [input_name]_weighted_MA[N]_[years].pdf  (only for odd N)
```

## Interpreting Results

### When to Use Each MA Method

1. **Centered MA**: Historical analysis where future data is available
   - Best for: Academic research, retrospective policy evaluation
   - Smoothest of the three methods

2. **Trailing MA**: Real-time monitoring and forecasting
   - Best for: Current policy decisions, nowcasting
   - Only uses past data

3. **Weighted MA**: Emphasis on recent trends while smoothing
   - Best for: Trend analysis with temporal priority
   - Only available for odd window sizes

### Reading the Metadata File

The metadata file contains:
- All input parameters used
- Data quality metrics (NaN counts before/after interpolation)
- Execution logs for each MA method
- Warnings (e.g., skipped weighted MA for even N)

## Common Workflow Patterns

### Pattern 1: Compare Window Sizes

Run multiple analyses with different window sizes:

```bash
for n in 3 5 7; do
  python3 compute_mima.py \
    --ma-number $n \
    --countries "Canada" \
    --start-year 1990 \
    --end-year 2020 \
    --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
    --output-path DART
done
```

### Pattern 2: Regional Analysis

Analyze multiple regional groupings:

```bash
# Nordic countries
python3 compute_mima.py --ma-number 5 \
  --countries "Denmark,Finland,Norway,Sweden" \
  --start-year 1990 --end-year 2020 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART

# Southern Europe
python3 compute_mima.py --ma-number 5 \
  --countries "Greece,Italy,Portugal,Spain" \
  --start-year 1990 --end-year 2020 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

## Troubleshooting

### Issue: "No data found for specified countries"

**Solution:** Check exact country names in CSV:
```bash
head -n 20 xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv | cut -d',' -f1
```

### Issue: Many NaN values in output

**Solutions:**
1. Use smaller window size (`--ma-number 3`)
2. Extend year range to include more data
3. Check data availability in input CSV
4. Review interpolation results in metadata file

### Issue: Missing weighted MA output

**Expected behavior:** Weighted MA only computed for odd N (3, 5, 7)
- Check metadata file for confirmation
- Use odd window size if weighted MA is needed

## Performance Notes

- Typical runtime: <10 seconds for 5 countries, 30 years
- Memory usage scales with: (number of countries) × (number of years)
- Visualization generation is the most time-consuming step (~2-3 seconds per plot)

## Next Steps

After generating MIMA outputs:

1. Review visualizations for data quality and trends
2. Check metadata file for warnings or data issues
3. Import CSV files into your analysis pipeline
4. Compare different MA methods to understand trend differences
5. Use trailing MA for forecasting, centered MA for historical analysis

## Additional Resources

- Full documentation: `DART/MIMA/README.md`
- Methodology notes: `METIS-LIS/mima_indicator/`
- Data availability tools: `analysis/data-availability/`

## Citation

When using MIMA results in publications, please cite the Poverty-Project repository and acknowledge the methodology.
