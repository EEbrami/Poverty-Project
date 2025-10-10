import pandas as pd
import numpy as np

# --- File Paths (relative to the DART/ directory, where the script will be saved) ---
LISSY_FILE = '../LISSY/MIMA5/phase1_mima5_results.csv'
DART_FILE = 'dart-table_dhi_median.csv'
OUTPUT_CSV = 'dart_dhi_median_validation.csv'
OUTPUT_TXT = 'dart_dhi_median_error_facts.txt'

def run_validation():
    """Performs the data validation, comparison, and statistics generation."""
    try:
        # 1. Load and prepare LISSY data
        df_lissy = pd.read_csv(LISSY_FILE)
        df_lissy = df_lissy[['country', 'year', 'median_dhi']]
        df_lissy.rename(columns={'median_dhi': 'median_dhi_LISSY'}, inplace=True)
        df_lissy['year'] = df_lissy['year'].astype(int)
    except FileNotFoundError:
        print(f"Fatal Error: LISSY file not found at {LISSY_FILE}. Check relative path.")
        return
    
    try:
        # 2. Load DART data and melt from wide to long format
        df_dart = pd.read_csv(DART_FILE)
        year_cols = [str(y) for y in range(1985, 2022)]
        
        df_dart_long = df_dart.melt(
            id_vars=['countries'],
            value_vars=year_cols,
            var_name='year',
            value_name='median_dhi_DART'
        )
        
        df_dart_long.rename(columns={'countries': 'country'}, inplace=True)
        df_dart_long['year'] = pd.to_numeric(df_dart_long['year'], errors='coerce').astype('Int64')
        df_dart_long['median_dhi_DART'] = pd.to_numeric(df_dart_long['median_dhi_DART'], errors='coerce')
        df_dart_long.dropna(subset=['year', 'median_dhi_DART'], inplace=True)

    except FileNotFoundError:
        print(f"Fatal Error: DART file not found at {DART_FILE}. Check relative path.")
        return
    except Exception as e:
        print(f"Fatal Error processing DART file: {e}")
        return

    # 3. Merge dataframes (inner merge to guarantee matching country-year pairs)
    df_merged = pd.merge(df_lissy, df_dart_long, on=['country', 'year'], how='inner')
    df_merged = df_merged[df_merged['median_dhi_DART'] != 0].copy() # Avoid division by zero
    
    # 4. Calculate the percentage difference ("error in pp")
    df_merged['pct_diff_LISSY_vs_DART'] = (
        (df_merged['median_dhi_LISSY'] - df_merged['median_dhi_DART']) / df_merged['median_dhi_DART']
    ) * 100

    # Select and reorder columns for the output CSV
    df_output = df_merged[['country', 'year', 'median_dhi_LISSY', 'median_dhi_DART', 'pct_diff_LISSY_vs_DART']]

    # --- Save Comparison CSV ---
    try:
        df_output.to_csv(OUTPUT_CSV, index=False, float_format='%.4f')
        print(f"Successfully created validation comparison CSV: {OUTPUT_CSV}")
    except Exception as e:
        print(f"Error saving output CSV: {e}")

    # --- Calculate and Save Distribution Facts ---
    pct_diff_series = df_output['pct_diff_LISSY_vs_DART']
    stats = pct_diff_series.describe().to_dict()

    distribution_facts = f"""
Distribution Facts for Percentage Difference (LISSY vs. DART Median DHI)
--------------------------------------------------------------------------
Formula: ((median_dhi_LISSY - median_dhi_DART) / median_dhi_DART) * 100
(A positive value means the LISSY result is higher than the DART table value.)

Total Observations (Country-Years): {int(stats.get('count', 0))}

Mean Error (Bias):              {stats.get('mean', 0.0):.4f} percentage points
Standard Deviation (Dispersion):{stats.get('std', 0.0):.4f} percentage points
Minimum Error:                  {stats.get('min', 0.0):.4f} percentage points
Maximum Error:                  {stats.get('max', 0.0):.4f} percentage points

Percentiles (A measure of central tendency and spread):
  25th Percentile (Q1):         {stats.get('25%', 0.0):.4f} percentage points
  50th Percentile (Median):     {stats.get('50%', 0.0):.4f} percentage points
  75th Percentile (Q3):         {stats.get('75%', 0.0):.4f} percentage points
"""

    # Save to TXT file
    try:
        with open(OUTPUT_TXT, 'w') as f:
            f.write(distribution_facts)
        print(f"Successfully created distribution facts TXT: {OUTPUT_TXT}")
    except Exception as e:
        print(f"Error saving output TXT: {e}")

if __name__ == "__main__":
    run_validation()
