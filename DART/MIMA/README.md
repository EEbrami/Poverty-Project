# MIMA: Median Income Moving Average Indicator

## Overview

The **MIMA (Median Income Moving Average)** workflow is a comprehensive, command-line-driven tool designed to compute and analyze moving averages of income time-series data. This methodology is particularly valuable for longitudinal, cross-national poverty and inequality research, as it addresses two critical challenges: **volatility** and **structural relevance**.

### Why MIMA?

The Moving Average approach serves two essential purposes:

1. **Ensuring Structural Relevance (The Median Anchor)**
   - The median represents the **current economic midpoint** of a society, unlike absolute measures
   - Basing analyses on median income (e.g., 50% or 60% of median DHI) ensures measures remain **relative** to contemporary living standards
   - As economies evolve, the indicator dynamically adjusts to capture **social exclusion** and relative deprivation

2. **Filtering for Persistence (The Moving Average)**
   - Moving averages function as **noise filters**, smoothing out transient fluctuations
   - Effectively removes high-frequency "noise" from:
     - Short-term **business cycle fluctuations** (recessions, booms)
     - **Sampling variability** in individual survey waves
   - Extracts the **persistent, long-run structural trend** in income dynamics

Together, these elements create an indicator that is both **socially relevant** (via the median) and **statistically robust** (via the moving average).

---

## Three Moving Average Variants

The MIMA workflow implements three distinct moving average methodologies, each with specific use cases:

### 1. Centered Moving Average (Symmetric Window)

**Formula**: For year $t$ with window size $N$:
```
MA_centered(t) = mean(values[t - floor(N/2) : t + floor(N/2)])
```

**Characteristics**:
- Symmetric window centered on year $t$
- For $N=5$: averages years $(t-2, t-1, t, t+1, t+2)$
- **Best for**: Historical analysis where future data is available
- **Smoothest** among the three methods

**Limitations**:
- Requires future data (not suitable for real-time forecasting)
- Edge years have partial windows

### 2. Trailing Moving Average (Backward-Looking Window)

**Formula**: For year $t$ with window size $N$:
```
MA_trailing(t) = mean(values[t - (N-1) : t])
```

**Characteristics**:
- Backward-looking window ending at year $t$
- For $N=5$: averages years $(t-4, t-3, t-2, t-1, t)$
- **Best for**: Real-time analysis, forecasting, policy monitoring
- Only uses historical data

**Limitations**:
- Lags behind current trends
- First $N-1$ years have NaN values

### 3. Weighted Moving Average (Triangular Weights)

**Formula**: For year $t$ with **odd** window size $N$ and triangular weights $w$:
```
MA_weighted(t) = Σ(values[i] × w[i]) / Σ(w[i])
```

**Weight Pattern** (for $N=5$): $[1, 2, 3, 2, 1]$
- Center year receives highest weight
- Weights decrease linearly toward edges

**Characteristics**:
- **Only computed for odd window sizes** ($N = 3, 5, 7$)
- Centered window with emphasis on the focal year
- Automatically adjusts weights at dataset boundaries
- **Best for**: Emphasizing recent trends while smoothing noise

**Constraint**:
- **Skipped entirely for even $N$** (e.g., $N=2, 4, 6$)
- This is logged in the metadata file as a warning

---

## Data Preprocessing and Quality Controls

### Missing Value Handling

The workflow applies **linear interpolation** with strict constraints:

- **Interpolation limit**: Maximum of **2 consecutive years**
- **Boundary handling**: No extrapolation at dataset endpoints
- Gaps exceeding 2 years remain as `NaN`

**Rationale**: Short gaps (≤2 years) can be reliably estimated via linear interpolation without introducing significant bias. Longer gaps may represent structural breaks or data unavailability that should not be artificially filled.

### Minimum Value Requirement

All three MA methods enforce a **minimum of 3 non-NaN values** within each rolling window:

- Windows with fewer than 3 valid observations produce `NaN` results
- This prevents spurious averages from insufficient data
- Particularly important at dataset boundaries and during data gaps

**Example**: With $N=5$ and 2 valid values in a window, the result is `NaN` rather than an unreliable 2-value average.

---

## Output Structure and File Naming

### Directory Organization

All outputs are saved under:
```
[OUTPUT_PATH]/MIMA/
├── csv/                    # CSV result files and metadata
└── visualizations/         # PNG and PDF plots
```

### Dynamic File Naming Convention

All output files follow a self-documenting pattern:
```
[Input_File_Stem]_[method]_MA[N]_[Start_Year]-[End_Year].[ext]
```

**Examples**:
- Input: `dart-med-pop_decomp-dhi.csv`, $N=5$, Years: 1985-2021
- Outputs:
  - `dart-med-pop_decomp-dhi_centered_MA5_1985-2021.csv`
  - `dart-med-pop_decomp-dhi_trailing_MA5_1985-2021.png`
  - `dart-med-pop_decomp-dhi_weighted_MA5_1985-2021.pdf`

### CSV Output Format

- **Clean data only**: No metadata comments in CSV files
- First column: Country/entity names
- Subsequent columns: Years (as column headers)
- Values: Computed MA results (NaN for insufficient data)

### Metadata File

A single metadata text file is generated per execution:
```
[Input_File_Stem]_MA[N]_metadata.txt
```

**Contents**:
- All input parameters (window size, countries, years, paths)
- Interpolation settings and limits
- Initial and final NaN counts
- Separate execution logs for each MA method:
  - Warnings (e.g., even $N$ skipping Weighted MA)
  - Result statistics
  - Output file paths

---

## Usage Guide

### Basic Command Structure

```bash
python3 compute_mima.py \
  --ma-number [N] \
  --countries "[COUNTRY1],[COUNTRY2],..." \
  --start-year [YYYY] \
  --end-year [YYYY] \
  --input-path [PATH_TO_CSV] \
  --output-path [OUTPUT_DIR]
```

### Required Arguments

| Argument | Type | Constraint | Description |
|----------|------|------------|-------------|
| `--ma-number` | int | 2 ≤ N ≤ 7 | Moving average window size |
| `--countries` | str | Comma-separated | List of country names (must match CSV exactly) |
| `--start-year` | int | YYYY | Start year (inclusive) |
| `--end-year` | int | YYYY | End year (inclusive) |
| `--input-path` | str | Valid file path | Full path to input CSV |
| `--output-path` | str | Valid directory | Base output directory (MIMA subfolder created automatically) |

### Example 1: Standard Analysis (Odd Window)

```bash
python3 compute_mima.py \
  --ma-number 5 \
  --countries "Canada,Germany,Luxembourg" \
  --start-year 1985 \
  --end-year 2021 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

**Outputs**:
- All three MA variants (centered, trailing, weighted)
- 6 visualization files (PNG + PDF for each method)
- 3 CSV result files
- 1 metadata file

### Example 2: Even Window (Skips Weighted MA)

```bash
python3 compute_mima.py \
  --ma-number 4 \
  --countries "Canada,France,Italy" \
  --start-year 1990 \
  --end-year 2020 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

**Outputs**:
- Only centered and trailing MA variants
- 4 visualization files (PNG + PDF for each method)
- 2 CSV result files
- 1 metadata file with warning about skipped weighted MA

### Example 3: Short Time Window

```bash
python3 compute_mima.py \
  --ma-number 3 \
  --countries "United States,United Kingdom" \
  --start-year 2010 \
  --end-year 2020 \
  --input-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --output-path DART
```

---

## Input Data Requirements

### CSV Format Expectations

The input CSV must follow this structure:

```csv
countries,1980,1981,1982,...
Australia,20000,20500,21000,...
Canada,22000,22500,23000,...
...
```

**Requirements**:
- First column: Entity names (countries, regions, etc.)
- Remaining columns: Years (column headers must be numeric)
- Values: Numeric income data (NaN or empty cells acceptable)
- Country names in `--countries` must **exactly match** those in CSV

### Recommended Data Sources

This workflow is optimized for:
- **LIS (Luxembourg Income Study)** datasets
- **OECD** income statistics
- **World Bank** income/poverty indicators
- Any longitudinal income time-series in the required format

---

## Technical Notes

### Interpolation Algorithm

Uses `pandas.Series.interpolate()` with:
- `method='linear'`: Linear interpolation between points
- `limit=2`: Maximum consecutive NaN values to fill
- `limit_area='inside'`: Only interpolate interior gaps (not endpoints)

### Triangular Weight Calculation

For odd window size $N$:
1. Half-width: $h = \lfloor N/2 \rfloor$
2. Weights: $[1, 2, ..., h, h+1, h, ..., 2, 1]$
3. Example ($N=7$): $[1, 2, 3, 4, 3, 2, 1]$

At dataset boundaries:
- Weights are proportionally adjusted for partial windows
- Normalization: Divide by sum of **active** weights only

### Minimum Periods Enforcement

Implemented via `pandas.rolling(min_periods=3)`:
- Returns `NaN` if fewer than 3 non-NaN values in window
- Ensures statistical validity of computed averages
- Applied consistently across all three MA methods

---

## Troubleshooting

### Common Issues

**Issue**: "No data found for specified countries"
- **Cause**: Country names in `--countries` don't match CSV
- **Solution**: Check exact spelling/capitalization in input CSV

**Issue**: "No year columns found in range"
- **Cause**: Year range doesn't overlap with CSV columns
- **Solution**: Verify year columns in CSV using `head [file].csv`

**Issue**: Warning about even window size
- **Cause**: Using even `--ma-number` (2, 4, 6)
- **Solution**: This is expected; weighted MA only computes for odd windows

**Issue**: Many NaN values in output
- **Cause**: Insufficient data in rolling windows
- **Solution**: 
  - Use smaller `--ma-number`
  - Extend year range to include more data
  - Check data availability in input CSV

---

## References and Further Reading

### Methodological Background

- **Luxembourg Income Study (LIS)**: [www.lisdatacenter.org](https://www.lisdatacenter.org)
- **OECD Income Distribution Database**: [stats.oecd.org](https://stats.oecd.org)

### Related Documentation

- `METIS-LIS/mima_indicator/`: Detailed documentation on MIMA rationale
- `DART/Methodological_Notes.md`: Technical notes on DART methodology
- `analysis/data-availability/`: Data availability analysis tools

---

## Version History

- **v1.0**: Initial release with three MA variants, command-line interface, and comprehensive output structure

---

## License and Citation

This tool is part of the Poverty-Project repository. When using MIMA results in research, please cite:

```
[Repository citation information to be added]
```

---

## Support and Contribution

For issues, questions, or contributions:
- Open an issue on the repository
- Refer to repository documentation
- Contact the project maintainers

**Note**: This workflow is designed for batch processing of historical income data and requires the full dataset to be available locally. It is not suitable for streaming or real-time data processing.
