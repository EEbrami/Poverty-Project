# MIMA: Median Income Moving Average Analysis

This directory contains the results of computing three variants of 5-year moving averages (MA(5)) for equivalised disposable household income medians from the Luxembourg Income Study (LIS) Data Access Research Tool (DART).

## Overview

The analysis processes median income data for five countries over the period 1985-2021:
- **Canada**
- **Germany**
- **Luxembourg**
- **United Kingdom**
- **United States**

## Data Source

- **Input File**: `xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv`
- **Income Measure**: Equivalised Disposable Household Income (median values in national currencies)
- **Equivalisation**: Square root of household size
- **Coding**: Top- and bottom-coded per LIS standards

## Computation Script

The Python script `compute_mima.py` in the parent directory (`DART/`) performs all computations. To run:

```bash
python3 DART/compute_mima.py
```

### Requirements
- Python 3.x
- pandas
- numpy
- matplotlib

## Moving Average Variants

### 1. Centered 5-Year Moving Average
**File**: `centered_ma5_1985-2021.csv`

- **Window**: Symmetric window from t-2 to t+2 (5 years centered on year t)
- **Methodology**: Simple arithmetic mean of median incomes in the window
- **Minimum Values**: Requires at least 3 years of data in the window
- **Boundary Handling**: Uses partial windows at boundaries (e.g., 1985-1987 for year 1985)
- **Rationale**: Provides balanced smoothing, minimizing lag bias, as recommended for long-run trend analysis in LIS and OECD studies

### 2. Trailing 5-Year Moving Average
**File**: `trailing_ma5_1985-2021.csv`

- **Window**: Backward-looking window from t-4 to t (5 years ending at year t)
- **Methodology**: Simple arithmetic mean of median incomes in the window
- **Minimum Values**: Requires at least 3 years of data in the window
- **Boundary Handling**: Years 1985-1986 have insufficient historical data and are set to NaN
- **Rationale**: Emphasizes historical accumulation and is suitable for attenuating volatility without incorporating future data, as used in ILO labor income analyses

### 3. Weighted 5-Year Moving Average
**File**: `weighted_ma5_1985-2021.csv`

- **Window**: Centered window from t-2 to t+2
- **Weights**: Triangular weights [1, 2, 3, 2, 1] normalized by sum (9)
- **Methodology**: Weighted average emphasizing the central year
- **Minimum Values**: Requires at least 3 weighted values in the window
- **Boundary Handling**: Adjusts weights proportionally for partial windows
- **Rationale**: Provides nuanced smoothing with emphasis on the central year, reducing endpoint bias, analogous to weighted MAs in LIS working papers on tax rates and income floors

## Data Processing

### Missing Value Handling
- **Linear Interpolation**: Applied for gaps of 1-2 consecutive missing years
- **Conditions**: Interpolation requires non-missing values before and after the gap
- **Large Gaps**: Gaps exceeding 2 years or at endpoints are not interpolated
- **Documentation**: All interpolations are logged in the metadata section of output files

### Output Format

Each CSV file contains:
- **Header Row**: Column names (year, country names)
- **Data Rows**: Years 1985-2021 with computed MA values (2 decimal places)
- **Metadata Section**: Comments (prefixed with #) documenting:
  - Interpolation notes
  - Years with insufficient data (set to NaN)
  - Any exclusions due to data gaps

## Visualizations

For each moving average variant, both PNG and PDF visualizations are provided:

### Centered MA
- `centered_ma5_1985-2021.png` (high-resolution, 300 DPI)
- `centered_ma5_1985-2021.pdf` (vector format)

### Trailing MA
- `trailing_ma5_1985-2021.png` (high-resolution, 300 DPI)
- `trailing_ma5_1985-2021.pdf` (vector format)

### Weighted MA
- `weighted_ma5_1985-2021.png` (high-resolution, 300 DPI)
- `weighted_ma5_1985-2021.pdf` (vector format)

All visualizations include:
- Time series plots for all five countries
- Appropriate axis labels (Year, Median Income in National Currency)
- Legend identifying each country
- Grid for readability
- Title: "MIMA: [Variant Name] (1985-2021)"

## Methodological Notes

### Window Requirements
All three MA variants require a minimum of 3 valid data points within the window. This ensures:
- Statistical reliability of the computed average
- Avoidance of spurious values from insufficient data
- Consistency with time-series smoothing best practices

### Boundary Year Handling
- **Centered MA**: Uses partial windows at both start and end (e.g., 1985-1987 for year 1985, 2019-2021 for year 2021)
- **Trailing MA**: First valid values appear at year 1987 (requires years 1985-1987)
- **Weighted MA**: Adjusts triangular weights for partial windows while maintaining the center-emphasis principle

### National Currency Values
All median income values are reported in national currencies:
- Canada: Canadian Dollars (CAD)
- Germany: Euros (EUR) / Deutsche Mark (DM) for earlier years
- Luxembourg: Euros (EUR) / Luxembourg Francs (LUF) for earlier years
- United Kingdom: British Pounds (GBP)
- United States: US Dollars (USD)

Note: No PPP conversion or inflation adjustment is applied. Values reflect the nominal median income in the respective national currency for each year.

## References

This analysis follows methodological guidelines from:
- Luxembourg Income Study (LIS) Data Access Research Tool (DART)
- LIS working papers on income time-series smoothing
- OECD income distribution studies
- ILO labor income analyses

## Reproducibility

To reproduce these results:
1. Ensure the input file is available at the expected path
2. Install required Python packages: `pip install pandas numpy matplotlib`
3. Run the computation script: `python3 DART/compute_mima.py`
4. Results will be generated in the `DART/MIMA/` directory

## Generated Files

- `centered_ma5_1985-2021.csv` - Centered MA(5) results
- `centered_ma5_1985-2021.png` - Centered MA(5) visualization
- `centered_ma5_1985-2021.pdf` - Centered MA(5) visualization (PDF)
- `trailing_ma5_1985-2021.csv` - Trailing MA(5) results
- `trailing_ma5_1985-2021.png` - Trailing MA(5) visualization
- `trailing_ma5_1985-2021.pdf` - Trailing MA(5) visualization (PDF)
- `weighted_ma5_1985-2021.csv` - Weighted MA(5) results
- `weighted_ma5_1985-2021.png` - Weighted MA(5) visualization
- `weighted_ma5_1985-2021.pdf` - Weighted MA(5) visualization (PDF)
- `README.md` - This documentation file

## Last Updated

Generated: 2024 (automated processing)
