# Median Income Moving Average (MIMA) Workflow

## Overview

This directory contains the tools and outputs for computing **Moving Average (MA) variants** of median income data. The MIMA workflow is designed to produce socially relevant and statistically robust poverty indicators by smoothing out transient fluctuations while maintaining structural relevance.

## Purpose and Rationale

The MIMA derived from **median disposable household income (DHI)** addresses two fundamental challenges in longitudinal, cross-national poverty research:

### 1. Ensuring Structural Relevance (The Median Anchor)
- The **median** represents the current economic midpoint of a society
- Basing poverty lines (e.g., 50% or 60% of median DHI) ensures measures remain **relative** to contemporary living standards
- As economies evolve, the poverty line dynamically adjusts, capturing **social exclusion** and relative deprivation

### 2. Filtering for Persistence (The Moving Average)
- Applying a Moving Average functions as a **noise filter**
- Smooths out transient "noise" from:
  - Short-term **business cycle fluctuations** (e.g., recessions)
  - **Sampling variability** in individual survey waves
- Extracts the **persistent, long-run structural trend** in poverty

This methodology creates an indicator that is both **socially relevant** (via the median) and **statistically robust** (via the moving average).

## Three MA Variants

The MIMA workflow computes three distinct Moving Average variants, each serving different analytical purposes:

### 1. Centered MA(N)
- **Method**: Simple arithmetic mean of a symmetric window centered on year *t*
- **Window**: From *t - (N/2)* to *t + (N/2)*
- **Purpose**: Optimal smoothing for historical analysis where future data is available
- **Trade-off**: Cannot be computed for the most recent *(N/2)* years in real-time applications

### 2. Trailing MA(N)
- **Method**: Simple arithmetic mean of a backward-looking window
- **Window**: From *t - (N-1)* to *t*
- **Purpose**: Real-time analysis and forecasting (uses only past data)
- **Trade-off**: Introduces a phase lag; reacts more slowly to structural changes

### 3. Weighted MA(N)
- **Method**: Centered window with **triangular weights**
- **Constraint**: **Only computed for odd N** (even N are skipped and logged)
- **Weights Example** (N=5): `[1, 2, 3, 2, 1]` (center year weighted most heavily)
- **Purpose**: Balances smoothing with responsiveness by emphasizing recent data
- **Boundary Handling**: At dataset edges, weights are **proportionally adjusted** for partial windows
  - Only active weights corresponding to non-NaN data points are used
  - The weighted sum is divided by the sum of active weights

## Computation Rules

### Data Pre-processing
1. **Filtering**: Input CSV is filtered for specified countries and years
2. **Missing Value Handling**: 
   - **Linear interpolation** applied for data gaps ≤ 2 years
   - Gaps > 2 years or at endpoints remain `NaN`

### MA Calculation Rules
- **Minimum requirement**: All MA calculations require **minimum 3 non-NaN values** within the rolling window
- If fewer than 3 values are available, the result for that year is set to `NaN`
- This ensures statistical reliability of the smoothed values

### Even N Constraint for Weighted MA
- Weighted MA is **skipped entirely** if N is even
- Rationale: Triangular weights require a clear center point (only possible with odd N)
- This exclusion is logged in the metadata file

## Usage

### Command-Line Execution

Run the `compute_mima.py` script from the repository root:

```bash
python compute_mima.py \
  --ma-number 5 \
  --countries "CAN,DEU,LUX,GBR,USA" \
  --start-year 1985 \
  --end-year 2021 \
  --input-path "xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv" \
  --output-path "DART"
```

#### Required Arguments

| Argument | Type | Description | Constraints |
|----------|------|-------------|-------------|
| `--ma-number` | Integer | MA window size (N) | Must be between 2 and 7 inclusive |
| `--countries` | String | Comma-separated ISO country codes | e.g., `'CAN,DEU,LUX'` |
| `--start-year` | Integer | Start year (inclusive) | Must be < end-year |
| `--end-year` | Integer | End year (inclusive) | Must be > start-year |
| `--input-path` | String | Full path to source CSV | File must exist |
| `--output-path` | String | Directory where MIMA/ will be created | e.g., `'DART'` creates `'DART/MIMA/'` |

### GitHub Actions Integration

The workflow can also be executed via GitHub Actions for automated, reproducible runs.

#### Workflow File
- **Location**: `.github/workflows/run_mima_workflow.yml`
- **Trigger**: Manual execution via `workflow_dispatch`

#### Running via GitHub Actions

1. Navigate to the **Actions** tab in the GitHub repository
2. Select **MIMA Workflow** from the workflow list
3. Click **Run workflow**
4. Enter the desired parameters (or use defaults):
   - **ma-number**: Default `5`
   - **countries**: Default `'CAN,DEU,LUX,GBR,USA'`
   - **start-year**: Default `1985`
   - **end-year**: Default `2021`
   - **input-path**: Default `'xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv'`
   - **output-path**: Default `'DART'`
5. Click **Run workflow** to execute

Results will be automatically committed and pushed to the repository.

## Output Structure

All outputs are saved under the following structure:

```
[OUTPUT_PATH]/MIMA/
├── csv/
│   ├── [Input_Stem]_centered_MA[N]_[Start]-[End].csv
│   ├── [Input_Stem]_trailing_MA[N]_[Start]-[End].csv
│   ├── [Input_Stem]_weighted_MA[N]_[Start]-[End].csv  (only for odd N)
│   └── [Input_Stem]_MA[N]_metadata.txt
└── visualizations/
    ├── [Input_Stem]_centered_MA[N]_[Start]-[End].png
    ├── [Input_Stem]_centered_MA[N]_[Start]-[End].pdf
    ├── [Input_Stem]_trailing_MA[N]_[Start]-[End].png
    ├── [Input_Stem]_trailing_MA[N]_[Start]-[End].pdf
    ├── [Input_Stem]_weighted_MA[N]_[Start]-[End].png  (only for odd N)
    └── [Input_Stem]_weighted_MA[N]_[Start]-[End].pdf  (only for odd N)
```

### Dynamic File Naming

Files use a self-documenting naming convention:
- **Format**: `[Input_File_Stem]_[method]_MA[N]_[Start_Year]-[End_Year].[ext]`
- **Example**: `dart-med-pop_decomp-dhi_centered_MA5_1985-2021.csv`

### Metadata File

A single metadata file (`[Input_Stem]_MA[N]_metadata.txt`) records:
- All input parameters (N, countries, years, file paths)
- Interpolation limit used
- Initial and final NaN counts
- Separate sections for each MA method with:
  - Execution details
  - Method-specific parameters (e.g., window, weights)
  - Warnings (e.g., even N skipping Weighted MA)
  - Value counts and statistics

**Important**: No metadata or comments are included within the CSV files themselves.

## Visualizations

The workflow automatically generates:
- **PNG files** (high resolution, 300 DPI) for digital use
- **PDF files** for publication-quality printing

Each visualization shows:
- Time series plots for all specified countries
- Clear labeling and legends
- Grid lines for readability
- Method and time period in the title

## Example Output

For the command:
```bash
python compute_mima.py \
  --ma-number 5 \
  --countries "CAN,DEU,LUX" \
  --start-year 1985 \
  --end-year 2021 \
  --input-path "xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv" \
  --output-path "DART"
```

Generated files:
```
DART/MIMA/
├── csv/
│   ├── dart-med-pop_decomp-dhi_centered_MA5_1985-2021.csv
│   ├── dart-med-pop_decomp-dhi_trailing_MA5_1985-2021.csv
│   ├── dart-med-pop_decomp-dhi_weighted_MA5_1985-2021.csv
│   └── dart-med-pop_decomp-dhi_MA5_metadata.txt
└── visualizations/
    ├── dart-med-pop_decomp-dhi_centered_MA5_1985-2021.png
    ├── dart-med-pop_decomp-dhi_centered_MA5_1985-2021.pdf
    ├── dart-med-pop_decomp-dhi_trailing_MA5_1985-2021.png
    ├── dart-med-pop_decomp-dhi_trailing_MA5_1985-2021.pdf
    ├── dart-med-pop_decomp-dhi_weighted_MA5_1985-2021.png
    └── dart-med-pop_decomp-dhi_weighted_MA5_1985-2021.pdf
```

## Technical Notes

### Dependencies
- `pandas >= 2.0.0`: Data manipulation and CSV I/O
- `numpy >= 1.24.0`: Numerical computations
- `matplotlib >= 3.5.0`: Visualization generation

### Performance Considerations
- Processing time scales linearly with the number of countries and years
- Typical execution time: < 10 seconds for 5 countries over 40 years
- Memory usage is minimal for standard datasets (< 100 MB)

### Data Quality
- The workflow performs robust validation of input parameters
- Missing data is handled transparently with clear logging
- All transformations are documented in the metadata file

## References

For more information on the LIS Database and median income variables:
- [LIS Cross-National Data Center](https://www.lisdatacenter.org/)
- See `METIS-LIS/mima_indicator/` for variable definitions and codebooks

## Support

For issues or questions:
1. Check the metadata file for execution details
2. Review the input CSV format (requires `countries` column + year columns)
3. Ensure all parameters meet the specified constraints
4. Verify that required dependencies are installed
