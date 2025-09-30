
# Median Income Moving Average (MIMA) Indicator 

This directory contains the necessary documentation, codebook excerpts, and data availability matrices to calculate and analyze a **Median Income Moving Average Indicator** of poverty and inequality.

***

### Rationale for the Indicator

The MIMA derived from the **median disposable household income (DHI)** is a superior measure for tracking the poverty line through time because it directly addresses the two main challenges in longitudinal, cross-national poverty research: **volatility** and **relevance**.

1.  **Ensuring Structural Relevance (The Median Anchor):**
    * The median represents the **current economic midpoint** of a society, unlike an absolute poverty line.
    * Basing the poverty line (e.g., at 50% or 60% of the median DHI) ensures the measure remains **relative** to the contemporary standard of living. As the national economy grows, the poverty line dynamically adjusts, ensuring the indicator captures **social exclusion** and relative deprivation.

2.  **Filtering for Persistence (The Moving Average):**
    * Applying a Moving Average to the median-derived indicator functions as a **noise filter**.
    * It effectively **smooths out** transient, high-frequency "noise" caused by short-term **business cycle fluctuations** (e.g., recessions) or inherent **sampling variability** present in individual survey waves .
    * This smoothing process extracts the **persistent, long-run structural trend** in poverty.
  

In essence, this methodology creates a poverty indicator that is **socially relevant** (via the median) and **statistically robust** (via the moving average), making it the most practical approach for structural analysis.

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

***

## Variable Definitions

### `nhhmem` — Number of Household Members
- **Topic:** Household Composition and Living Arrangements
- **Definition:**  
  Total number of members in a household.  
- **Comment:**  
  This count is used for all household composition metrics and for constructing the LIS equivalence scale in key figures.

---

### `dhi` — Disposable Household Income
- **Topic:** Income Aggregates / Major Economic Aggregates
- **Definition:**  
  The sum of cash and non-cash income from labour and capital, income from pensions (both private and public), non-pension public social benefits (from insurance, universal, or assistance schemes, including in-kind social assistance transfers), as well as cash and non-cash private transfers, **minus** income taxes and social contributions paid.
- **Formula:**  
  `dhi = hitotal (= hilabour + hicapital + hipension + hipubsoc + hiprivate) - hxitsc`
- **Comment:**  
  - Includes all recurrent payments (annual or more frequent) available for current consumption that do not reduce household net worth.
  - **Excludes:**  
    - Non-cash income from capital (e.g., imputed value of services from owned durable goods).
    - Non-cash universal government transfers (e.g., housing, education, health, or child care services).
    - Certain means-tested public benefits, especially where benefits are provided to the whole population by different means (e.g., Medicaid in the US is excluded).

---

### `hifactor` — Factor Income, Household
- **Topic:** Income Aggregates / Major Economic Aggregates
- **Definition:**  
  The sum of cash and non-cash income from labour and from capital.
- **Formula:**  
  `hifactor = hilabour + hicapital`

---

### `hitransfer` — Transfer Income, Household
- **Topic:** Income Aggregates / Major Economic Aggregates
- **Definition:**  
  The sum of total pensions (public and private), non-pension public social benefits (from insurance, universal, or assistance schemes, including in-kind social assistance transfers), and cash and non-cash private transfers.
- **Formula:**  
  `hitransfer = hipension + hipubsoc + hiprivate`

---

## Notes

- For more details or to access LIS microdata, refer to the [LIS Database documentation](https://www.lisdatacenter.org/).
- Variable names are standardized for cross-country and cross-time comparability.
