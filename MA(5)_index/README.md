
# MA INDEX: Longitudinal Poverty and Inequality Analysis

This directory contains the necessary documentation, codebook excerpts, and data availability matrices to calculate and analyze a **Moving Average (MA) Index** of poverty and inequality.

***

### Rationale for the Index

The Moving Average (MA) of an index derived from the **median disposable household income (DHI)** is a superior measure for tracking the poverty line through time because it directly addresses the two main challenges in longitudinal, cross-national poverty research: **volatility** and **relevance**.

1.  **Ensuring Structural Relevance (The Median Anchor):**
    * The median represents the **current economic midpoint** of a society, unlike an absolute poverty line.
    * Basing the poverty line (e.g., at 50% or 60% of the median DHI) ensures the measure remains **relative** to the contemporary standard of living. As the national economy grows, the poverty line dynamically adjusts, ensuring the index captures **social exclusion** and relative deprivation.

2.  **Filtering for Persistence (The Moving Average):**
    * Applying a Moving Average to the median-derived index functions as a **noise filter**.
    * It effectively **smooths out** transient, high-frequency "noise" caused by short-term **business cycle fluctuations** (e.g., recessions) or inherent **sampling variability** present in individual survey waves .
    * This smoothing process extracts the **persistent, long-run structural trend** in poverty.
  

In essence, this methodology creates a poverty index that is **socially relevant** (via the median) and **statistically robust** (via the moving average), making it the most practical approach for structural analysis.

***

## Folder Contents

This directory contains the some documentation from the **METadata Information System (METIS) of Luxembourg Income Study (LIS) Database**.

| File Name | Description and Utility |
| :--- | :--- |
| `variables-definition.xlsx - Major Economic Aggregates.csv` | Explicit definitions for welfare aggregates, most crucially **Disposable Household Income (DHI)**, which forms the denominator for the relative poverty line. |
| `variables-definition.xlsx - Household Composition and Livin.csv` | Definitions for socio-demographic variables like household size (`NHHMEM`) necessary for calculating **equivalized** income. |
| `our-lis-documentation-availability-matrix.xlsx - All Waves as of 28-Sep-2025.csv` | The critical resource for identifying countries with a **"full streak"** of data, ensuring the necessary continuity for the Moving Average calculation. |
| `our-lis-documentation.xlsx - Surveys as of 28-Sep-2025.csv` | Metadata on the original national surveys, including collecting institutions and sampling methods, crucial for understanding data heterogeneity. |
| `codebook.xlsx - Table 1.csv` | Codebook excerpts detailing survey-specific identifiers and region classifications. |
