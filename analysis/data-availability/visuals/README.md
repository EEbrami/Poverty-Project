# Data Availability Visualizations

This directory contains tools for generating data availability visualizations from country-by-year CSV data.

## Overview

The visualization tool creates two output files for each CSV:

1. **Plain text file (`.txt`)**: A grid visualization with headers and legend
2. **Markdown file (`.md`)**: Same grid in a code fence plus a summary section

Both files show data availability across years for each entity (country), with rows sorted by ascending longest streak length.

## Files

- `generate_visuals.py`: Python script that generates the visualizations
- `*.txt`: Generated plain text visualizations
- `*.md`: Generated Markdown visualizations

## How to Generate Visualizations

### Via GitHub Actions (Recommended)

1. Navigate to the **Actions** tab in the GitHub repository
2. Select the **Data Availability Visuals** workflow
3. Click **Run workflow**
4. Fill in the required input:
   - **csv_path**: Path to the CSV file relative to repo root (e.g., `xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv`)
5. Optionally adjust other inputs:
   - **start_year**: Clip to years >= this value (e.g., `2000`)
   - **end_year**: Clip to years <= this value (e.g., `2020`)
   - **tick_interval**: Tick mark spacing for x-axis in years (default: `5`)
   - **glyph**: Character to render for available data (default: `█`)
   - **include_universal**: Whether to include Universal row showing full availability (default: `true`)
6. Click **Run workflow**

The workflow will:
- Checkout the repository
- Setup Python and install dependencies
- Run the script to generate visualizations
- Commit the generated `.txt` and `.md` files back to this directory

### Via Command Line

You can also run the script locally:

```bash
# Basic usage
python analysis/data-availability/visuals/generate_visuals.py \
  --csv-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv

# With optional filters
python analysis/data-availability/visuals/generate_visuals.py \
  --csv-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv \
  --start-year 2000 \
  --end-year 2020 \
  --tick-interval 5 \
  --glyph "█" \
  --include-universal true
```

## Input CSV Format

The script expects CSV files with:
- An entity column named `countries` (or the first column if `countries` doesn't exist)
- Year columns with purely numeric names (e.g., `1983`, `1984`, ...)
- Data cells containing numeric values or NaN/missing for unavailable data

Example:
```csv
countries,1983,1984,1985,...
Australia,,,21807.0,...
Austria,,,,...
```

## Output Format

### Text File (.txt)

```
Data Availability Visualization
============================================================

Source: xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv
Year range: 1983-2023 (41 years)
Number of entities: 33

Legend:
  █ = Data available for that year
    = Data not available

Entity          | LS | Availability by Year
------------------------------------------------------------
Chile           |  1 |        █ █ █ █ █ █  █  █  █ █ █ █ █      
...
Universal       | 41 | █████████████████████████████████████████

                  |    | 1985    1990    1995    2000    2005    ...

Note: LS = Longest Streak (max consecutive years with data)
Entities are sorted by ascending longest streak.
The 'Universal' row shows full availability across all years.
```

### Markdown File (.md)

Contains the same grid in a code fence, plus a summary section with:
- Number of entities
- Year range
- Total years
- Tick interval
- Sorting explanation
- Legend

## Algorithm Details

1. **Entity Column Detection**: Uses `countries` column if present, otherwise uses first column
2. **Year Column Detection**: Identifies columns with purely numeric names
3. **Availability**: Treats non-NaN cells as available data
4. **Longest Streak**: Computes maximum contiguous run of years with data for each entity
5. **Sorting**: Sorts entities by ascending longest streak (shortest first)
6. **Universal Row**: Optional row showing full availability across all years (always last)

## Notes

- Only `.txt` and `.md` files are generated and committed
- No intermediate CSV files or tables are created
- The grid uses `█` (U+2588) by default for available data and space for missing data
- X-axis ticks are shown every N years (default 5) for readability
