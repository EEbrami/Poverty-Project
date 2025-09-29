# Variable Definitions

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