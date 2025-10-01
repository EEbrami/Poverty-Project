# Data Availability Analysis: 15-Phase Greedy Coverage Algorithm

This document contains results from 15 sequential exclusion phases using the Coverage-based pivot shrink (A1b) algorithm.

Each phase excludes countries from previous phases and finds the optimal submatrix of remaining data.

## Phase 1

<details>
<summary>Click to view full partition results for Phase 1...</summary>

| period    |   length |   num_countries | countries                                                                                                                                                                                                     |
|:----------|---------:|----------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1983-2022 |       40 |               2 | Germany;United States                                                                                                                                                                                         |
| 1983-2021 |       39 |               3 | Germany;United Kingdom;United States                                                                                                                                                                          |
| 1985-2021 |       37 |               5 | Canada;Germany;Luxembourg;United Kingdom;United States                                                                                                                                                        |
| 1985-2021 |       37 |               5 | Canada;Germany;Luxembourg;United Kingdom;United States                                                                                                                                                        |
| 1996-2021 |       26 |               6 | Canada;France;Germany;Luxembourg;United Kingdom;United States                                                                                                                                                 |
| 2000-2021 |       22 |               7 | Canada;France;Germany;Luxembourg;Sweden;United Kingdom;United States                                                                                                                                          |
| 2001-2021 |       21 |               9 | Canada;Colombia;France;Germany;Israel;Luxembourg;Sweden;United Kingdom;United States                                                                                                                          |
| 2002-2021 |       20 |              11 | Canada;Colombia;France;Germany;Greece;Ireland;Israel;Luxembourg;Sweden;United Kingdom;United States                                                                                                           |
| 2003-2021 |       19 |              13 | Austria;Belgium;Canada;Colombia;France;Germany;Greece;Ireland;Israel;Luxembourg;Sweden;United Kingdom;United States                                                                                           |
| 2004-2021 |       18 |              16 | Austria;Belgium;Canada;Colombia;France;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;United Kingdom;United States                                                                  |
| 2004-2021 |       18 |              16 | Austria;Belgium;Canada;Colombia;France;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;United Kingdom;United States                                                                  |
| 2004-2021 |       18 |              16 | Austria;Belgium;Canada;Colombia;France;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;United Kingdom;United States                                                                  |
| 2006-2021 |       16 |              17 | Austria;Belgium;Canada;Colombia;France;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland;United Kingdom;United States                                                      |
| 2006-2017 |       12 |              18 | Austria;Belgium;Canada;Colombia;France;Germany;Greece;Iceland;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland;United Kingdom;United States                                              |
| 2008-2017 |       10 |              19 | Austria;Belgium;Canada;Colombia;France;Germany;Greece;Iceland;Ireland;Israel;Japan;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland;United Kingdom;United States                                        |
| 2009-2017 |        9 |              20 | Austria;Belgium;Canada;Colombia;France;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland;United Kingdom;United States                              |
| 2015-2017 |        3 |              22 | Austria;Belgium;Canada;Colombia;Denmark;France;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland;United Kingdom;United States             |
| 2015-2017 |        3 |              22 | Austria;Belgium;Canada;Colombia;Denmark;France;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland;United Kingdom;United States             |
| 2016-2017 |        2 |              23 | Austria;Belgium;Canada;Colombia;Denmark;France;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Slovakia;South Korea;Spain;Sweden;Switzerland;United Kingdom;United States |

</details>

## Phase 2

<details>
<summary>Click to view full partition results for Phase 2...</summary>

| period    |   length |   num_countries | countries                                                                                                                                                                               |
|:----------|---------:|----------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1983-2021 |       39 |               1 | United Kingdom                                                                                                                                                                          |
| 1985-2021 |       37 |               3 | Canada;Luxembourg;United Kingdom                                                                                                                                                        |
| 1985-2021 |       37 |               3 | Canada;Luxembourg;United Kingdom                                                                                                                                                        |
| 1996-2021 |       26 |               4 | Canada;France;Luxembourg;United Kingdom                                                                                                                                                 |
| 2000-2021 |       22 |               5 | Canada;France;Luxembourg;Sweden;United Kingdom                                                                                                                                          |
| 2001-2021 |       21 |               7 | Canada;Colombia;France;Israel;Luxembourg;Sweden;United Kingdom                                                                                                                          |
| 2002-2021 |       20 |               9 | Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Sweden;United Kingdom                                                                                                           |
| 2003-2021 |       19 |              11 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Sweden;United Kingdom                                                                                           |
| 2004-2021 |       18 |              14 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;United Kingdom                                                                  |
| 2004-2021 |       18 |              14 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;United Kingdom                                                                  |
| 2004-2021 |       18 |              14 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;United Kingdom                                                                  |
| 2006-2021 |       16 |              15 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland;United Kingdom                                                      |
| 2006-2017 |       12 |              16 | Austria;Belgium;Canada;Colombia;France;Greece;Iceland;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland;United Kingdom                                              |
| 2008-2017 |       10 |              17 | Austria;Belgium;Canada;Colombia;France;Greece;Iceland;Ireland;Israel;Japan;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland;United Kingdom                                        |
| 2009-2017 |        9 |              18 | Austria;Belgium;Canada;Colombia;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland;United Kingdom                              |
| 2015-2017 |        3 |              20 | Austria;Belgium;Canada;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland;United Kingdom             |
| 2015-2017 |        3 |              20 | Austria;Belgium;Canada;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland;United Kingdom             |
| 2016-2017 |        2 |              21 | Austria;Belgium;Canada;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Slovakia;South Korea;Spain;Sweden;Switzerland;United Kingdom |

</details>

## Phase 3

<details>
<summary>Click to view full partition results for Phase 3...</summary>

| period    |   length |   num_countries | countries                                                                                                                                                                |
|:----------|---------:|----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1985-2023 |       39 |               1 | Luxembourg                                                                                                                                                               |
| 1985-2021 |       37 |               2 | Canada;Luxembourg                                                                                                                                                        |
| 1996-2021 |       26 |               3 | Canada;France;Luxembourg                                                                                                                                                 |
| 2000-2021 |       22 |               4 | Canada;France;Luxembourg;Sweden                                                                                                                                          |
| 2001-2021 |       21 |               6 | Canada;Colombia;France;Israel;Luxembourg;Sweden                                                                                                                          |
| 2002-2021 |       20 |               8 | Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Sweden                                                                                                           |
| 2003-2021 |       19 |              10 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Sweden                                                                                           |
| 2004-2021 |       18 |              13 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden                                                                  |
| 2004-2021 |       18 |              13 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden                                                                  |
| 2004-2021 |       18 |              13 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden                                                                  |
| 2006-2021 |       16 |              14 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland                                                      |
| 2006-2017 |       12 |              15 | Austria;Belgium;Canada;Colombia;France;Greece;Iceland;Ireland;Israel;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland                                              |
| 2008-2017 |       10 |              16 | Austria;Belgium;Canada;Colombia;France;Greece;Iceland;Ireland;Israel;Japan;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland                                        |
| 2009-2017 |        9 |              17 | Austria;Belgium;Canada;Colombia;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Spain;Sweden;Switzerland                              |
| 2015-2017 |        3 |              19 | Austria;Belgium;Canada;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland             |
| 2015-2017 |        3 |              19 | Austria;Belgium;Canada;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland             |
| 2016-2017 |        2 |              20 | Austria;Belgium;Canada;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Poland;Slovakia;South Korea;Spain;Sweden;Switzerland |

</details>

