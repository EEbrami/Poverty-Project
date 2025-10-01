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

## Phase 4

<details>
<summary>Click to view full partition results for Phase 4...</summary>

| period    |   length |   num_countries | countries                                                                                                                                                     |
|:----------|---------:|----------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1984-2021 |       38 |               1 | Canada                                                                                                                                                        |
| 1996-2021 |       26 |               2 | Canada;France                                                                                                                                                 |
| 2000-2021 |       22 |               3 | Canada;France;Sweden                                                                                                                                          |
| 2001-2021 |       21 |               5 | Canada;Colombia;France;Israel;Sweden                                                                                                                          |
| 2002-2021 |       20 |               7 | Canada;Colombia;France;Greece;Ireland;Israel;Sweden                                                                                                           |
| 2003-2021 |       19 |               9 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Sweden                                                                                           |
| 2004-2021 |       18 |              12 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden                                                                  |
| 2004-2021 |       18 |              12 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden                                                                  |
| 2004-2021 |       18 |              12 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden                                                                  |
| 2006-2021 |       16 |              13 | Austria;Belgium;Canada;Colombia;France;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden;Switzerland                                                      |
| 2006-2017 |       12 |              14 | Austria;Belgium;Canada;Colombia;France;Greece;Iceland;Ireland;Israel;Netherlands;Poland;Spain;Sweden;Switzerland                                              |
| 2008-2017 |       10 |              15 | Austria;Belgium;Canada;Colombia;France;Greece;Iceland;Ireland;Israel;Japan;Netherlands;Poland;Spain;Sweden;Switzerland                                        |
| 2009-2017 |        9 |              16 | Austria;Belgium;Canada;Colombia;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Spain;Sweden;Switzerland                              |
| 2015-2017 |        3 |              18 | Austria;Belgium;Canada;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland             |
| 2015-2017 |        3 |              18 | Austria;Belgium;Canada;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland             |
| 2016-2017 |        2 |              19 | Austria;Belgium;Canada;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;South Korea;Spain;Sweden;Switzerland |

</details>

## Phase 5

<details>
<summary>Click to view full partition results for Phase 5...</summary>

| period    |   length |   num_countries | countries                                                                                                                                              |
|:----------|---------:|----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1996-2022 |       27 |               1 | France                                                                                                                                                 |
| 2000-2021 |       22 |               2 | France;Sweden                                                                                                                                          |
| 2001-2021 |       21 |               4 | Colombia;France;Israel;Sweden                                                                                                                          |
| 2002-2021 |       20 |               6 | Colombia;France;Greece;Ireland;Israel;Sweden                                                                                                           |
| 2003-2021 |       19 |               8 | Austria;Belgium;Colombia;France;Greece;Ireland;Israel;Sweden                                                                                           |
| 2004-2021 |       18 |              11 | Austria;Belgium;Colombia;France;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden                                                                  |
| 2004-2021 |       18 |              11 | Austria;Belgium;Colombia;France;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden                                                                  |
| 2004-2021 |       18 |              11 | Austria;Belgium;Colombia;France;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden                                                                  |
| 2006-2021 |       16 |              12 | Austria;Belgium;Colombia;France;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden;Switzerland                                                      |
| 2006-2017 |       12 |              13 | Austria;Belgium;Colombia;France;Greece;Iceland;Ireland;Israel;Netherlands;Poland;Spain;Sweden;Switzerland                                              |
| 2008-2017 |       10 |              14 | Austria;Belgium;Colombia;France;Greece;Iceland;Ireland;Israel;Japan;Netherlands;Poland;Spain;Sweden;Switzerland                                        |
| 2009-2017 |        9 |              15 | Austria;Belgium;Colombia;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Spain;Sweden;Switzerland                              |
| 2015-2017 |        3 |              17 | Austria;Belgium;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland             |
| 2015-2017 |        3 |              17 | Austria;Belgium;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland             |
| 2016-2017 |        2 |              18 | Austria;Belgium;Colombia;Denmark;France;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;South Korea;Spain;Sweden;Switzerland |

</details>

## Phase 6

<details>
<summary>Click to view full partition results for Phase 6...</summary>

| period    |   length |   num_countries | countries                                                                                                                                       |
|:----------|---------:|----------------:|:------------------------------------------------------------------------------------------------------------------------------------------------|
| 2000-2021 |       22 |               1 | Sweden                                                                                                                                          |
| 2001-2021 |       21 |               3 | Colombia;Israel;Sweden                                                                                                                          |
| 2002-2021 |       20 |               5 | Colombia;Greece;Ireland;Israel;Sweden                                                                                                           |
| 2003-2021 |       19 |               7 | Austria;Belgium;Colombia;Greece;Ireland;Israel;Sweden                                                                                           |
| 2004-2021 |       18 |              10 | Austria;Belgium;Colombia;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden                                                                  |
| 2004-2021 |       18 |              10 | Austria;Belgium;Colombia;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden                                                                  |
| 2004-2021 |       18 |              10 | Austria;Belgium;Colombia;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden                                                                  |
| 2006-2021 |       16 |              11 | Austria;Belgium;Colombia;Greece;Ireland;Israel;Netherlands;Poland;Spain;Sweden;Switzerland                                                      |
| 2006-2017 |       12 |              12 | Austria;Belgium;Colombia;Greece;Iceland;Ireland;Israel;Netherlands;Poland;Spain;Sweden;Switzerland                                              |
| 2008-2017 |       10 |              13 | Austria;Belgium;Colombia;Greece;Iceland;Ireland;Israel;Japan;Netherlands;Poland;Spain;Sweden;Switzerland                                        |
| 2009-2017 |        9 |              14 | Austria;Belgium;Colombia;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Spain;Sweden;Switzerland                              |
| 2015-2017 |        3 |              16 | Austria;Belgium;Colombia;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland             |
| 2015-2017 |        3 |              16 | Austria;Belgium;Colombia;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Sweden;Switzerland             |
| 2016-2017 |        2 |              17 | Austria;Belgium;Colombia;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;South Korea;Spain;Sweden;Switzerland |

</details>

## Phase 7

<details>
<summary>Click to view full partition results for Phase 7...</summary>

| period    |   length |   num_countries | countries                                                                                                                                |
|:----------|---------:|----------------:|:-----------------------------------------------------------------------------------------------------------------------------------------|
| 2001-2022 |       22 |               1 | Colombia                                                                                                                                 |
| 2001-2021 |       21 |               2 | Colombia;Israel                                                                                                                          |
| 2002-2021 |       20 |               4 | Colombia;Greece;Ireland;Israel                                                                                                           |
| 2003-2021 |       19 |               6 | Austria;Belgium;Colombia;Greece;Ireland;Israel                                                                                           |
| 2004-2021 |       18 |               9 | Austria;Belgium;Colombia;Greece;Ireland;Israel;Netherlands;Poland;Spain                                                                  |
| 2004-2021 |       18 |               9 | Austria;Belgium;Colombia;Greece;Ireland;Israel;Netherlands;Poland;Spain                                                                  |
| 2004-2021 |       18 |               9 | Austria;Belgium;Colombia;Greece;Ireland;Israel;Netherlands;Poland;Spain                                                                  |
| 2006-2021 |       16 |              10 | Austria;Belgium;Colombia;Greece;Ireland;Israel;Netherlands;Poland;Spain;Switzerland                                                      |
| 2006-2017 |       12 |              11 | Austria;Belgium;Colombia;Greece;Iceland;Ireland;Israel;Netherlands;Poland;Spain;Switzerland                                              |
| 2008-2017 |       10 |              12 | Austria;Belgium;Colombia;Greece;Iceland;Ireland;Israel;Japan;Netherlands;Poland;Spain;Switzerland                                        |
| 2009-2017 |        9 |              13 | Austria;Belgium;Colombia;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Spain;Switzerland                              |
| 2015-2017 |        3 |              15 | Austria;Belgium;Colombia;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Switzerland             |
| 2015-2017 |        3 |              15 | Austria;Belgium;Colombia;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Switzerland             |
| 2016-2017 |        2 |              16 | Austria;Belgium;Colombia;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;South Korea;Spain;Switzerland |

</details>

## Phase 8

<details>
<summary>Click to view full partition results for Phase 8...</summary>

| period    |   length |   num_countries | countries                                                                                                                       |
|:----------|---------:|----------------:|:--------------------------------------------------------------------------------------------------------------------------------|
| 2001-2021 |       21 |               1 | Israel                                                                                                                          |
| 2002-2021 |       20 |               3 | Greece;Ireland;Israel                                                                                                           |
| 2003-2021 |       19 |               5 | Austria;Belgium;Greece;Ireland;Israel                                                                                           |
| 2004-2021 |       18 |               8 | Austria;Belgium;Greece;Ireland;Israel;Netherlands;Poland;Spain                                                                  |
| 2004-2021 |       18 |               8 | Austria;Belgium;Greece;Ireland;Israel;Netherlands;Poland;Spain                                                                  |
| 2004-2021 |       18 |               8 | Austria;Belgium;Greece;Ireland;Israel;Netherlands;Poland;Spain                                                                  |
| 2006-2021 |       16 |               9 | Austria;Belgium;Greece;Ireland;Israel;Netherlands;Poland;Spain;Switzerland                                                      |
| 2006-2017 |       12 |              10 | Austria;Belgium;Greece;Iceland;Ireland;Israel;Netherlands;Poland;Spain;Switzerland                                              |
| 2008-2017 |       10 |              11 | Austria;Belgium;Greece;Iceland;Ireland;Israel;Japan;Netherlands;Poland;Spain;Switzerland                                        |
| 2009-2017 |        9 |              12 | Austria;Belgium;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Spain;Switzerland                              |
| 2015-2017 |        3 |              14 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Switzerland             |
| 2015-2017 |        3 |              14 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Switzerland             |
| 2016-2017 |        2 |              15 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Netherlands;Poland;Slovakia;South Korea;Spain;Switzerland |

</details>

## Phase 9

<details>
<summary>Click to view full partition results for Phase 9...</summary>

| period    |   length |   num_countries | countries                                                                                                                |
|:----------|---------:|----------------:|:-------------------------------------------------------------------------------------------------------------------------|
| 2002-2021 |       20 |               2 | Greece;Ireland                                                                                                           |
| 2003-2021 |       19 |               4 | Austria;Belgium;Greece;Ireland                                                                                           |
| 2004-2021 |       18 |               7 | Austria;Belgium;Greece;Ireland;Netherlands;Poland;Spain                                                                  |
| 2004-2021 |       18 |               7 | Austria;Belgium;Greece;Ireland;Netherlands;Poland;Spain                                                                  |
| 2004-2021 |       18 |               7 | Austria;Belgium;Greece;Ireland;Netherlands;Poland;Spain                                                                  |
| 2006-2021 |       16 |               8 | Austria;Belgium;Greece;Ireland;Netherlands;Poland;Spain;Switzerland                                                      |
| 2006-2017 |       12 |               9 | Austria;Belgium;Greece;Iceland;Ireland;Netherlands;Poland;Spain;Switzerland                                              |
| 2008-2017 |       10 |              10 | Austria;Belgium;Greece;Iceland;Ireland;Japan;Netherlands;Poland;Spain;Switzerland                                        |
| 2009-2017 |        9 |              11 | Austria;Belgium;Greece;Iceland;Ireland;Japan;Lithuania;Netherlands;Poland;Spain;Switzerland                              |
| 2015-2017 |        3 |              13 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Switzerland             |
| 2015-2017 |        3 |              13 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Switzerland             |
| 2016-2017 |        2 |              14 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Japan;Lithuania;Netherlands;Poland;Slovakia;South Korea;Spain;Switzerland |

</details>

## Phase 10

<details>
<summary>Click to view full partition results for Phase 10...</summary>

| period    |   length |   num_countries | countries                                                                                                 |
|:----------|---------:|----------------:|:----------------------------------------------------------------------------------------------------------|
| 2003-2022 |       20 |               1 | Austria                                                                                                   |
| 2004-2022 |       19 |               3 | Austria;Poland;Spain                                                                                      |
| 2004-2021 |       18 |               5 | Austria;Belgium;Netherlands;Poland;Spain                                                                  |
| 2004-2021 |       18 |               5 | Austria;Belgium;Netherlands;Poland;Spain                                                                  |
| 2006-2021 |       16 |               6 | Austria;Belgium;Netherlands;Poland;Spain;Switzerland                                                      |
| 2006-2017 |       12 |               7 | Austria;Belgium;Iceland;Netherlands;Poland;Spain;Switzerland                                              |
| 2008-2017 |       10 |               8 | Austria;Belgium;Iceland;Japan;Netherlands;Poland;Spain;Switzerland                                        |
| 2009-2017 |        9 |               9 | Austria;Belgium;Iceland;Japan;Lithuania;Netherlands;Poland;Spain;Switzerland                              |
| 2015-2017 |        3 |              11 | Austria;Belgium;Denmark;Iceland;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Switzerland             |
| 2015-2017 |        3 |              11 | Austria;Belgium;Denmark;Iceland;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Switzerland             |
| 2016-2017 |        2 |              12 | Austria;Belgium;Denmark;Iceland;Japan;Lithuania;Netherlands;Poland;Slovakia;South Korea;Spain;Switzerland |

</details>

## Phase 11

<details>
<summary>Click to view full partition results for Phase 11...</summary>

| period    |   length |   num_countries | countries                                                                                         |
|:----------|---------:|----------------:|:--------------------------------------------------------------------------------------------------|
| 2004-2023 |       20 |               1 | Poland                                                                                            |
| 2004-2021 |       18 |               4 | Belgium;Netherlands;Poland;Spain                                                                  |
| 2004-2021 |       18 |               4 | Belgium;Netherlands;Poland;Spain                                                                  |
| 2006-2021 |       16 |               5 | Belgium;Netherlands;Poland;Spain;Switzerland                                                      |
| 2006-2017 |       12 |               6 | Belgium;Iceland;Netherlands;Poland;Spain;Switzerland                                              |
| 2008-2017 |       10 |               7 | Belgium;Iceland;Japan;Netherlands;Poland;Spain;Switzerland                                        |
| 2009-2017 |        9 |               8 | Belgium;Iceland;Japan;Lithuania;Netherlands;Poland;Spain;Switzerland                              |
| 2015-2017 |        3 |              10 | Belgium;Denmark;Iceland;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Switzerland             |
| 2015-2017 |        3 |              10 | Belgium;Denmark;Iceland;Japan;Lithuania;Netherlands;Poland;Slovakia;Spain;Switzerland             |
| 2016-2017 |        2 |              11 | Belgium;Denmark;Iceland;Japan;Lithuania;Netherlands;Poland;Slovakia;South Korea;Spain;Switzerland |

</details>

## Phase 12

<details>
<summary>Click to view full partition results for Phase 12...</summary>

| period    |   length |   num_countries | countries                                                                                  |
|:----------|---------:|----------------:|:-------------------------------------------------------------------------------------------|
| 2003-2021 |       19 |               1 | Belgium                                                                                    |
| 2004-2021 |       18 |               3 | Belgium;Netherlands;Spain                                                                  |
| 2006-2021 |       16 |               4 | Belgium;Netherlands;Spain;Switzerland                                                      |
| 2006-2017 |       12 |               5 | Belgium;Iceland;Netherlands;Spain;Switzerland                                              |
| 2008-2017 |       10 |               6 | Belgium;Iceland;Japan;Netherlands;Spain;Switzerland                                        |
| 2009-2017 |        9 |               7 | Belgium;Iceland;Japan;Lithuania;Netherlands;Spain;Switzerland                              |
| 2015-2017 |        3 |               9 | Belgium;Denmark;Iceland;Japan;Lithuania;Netherlands;Slovakia;Spain;Switzerland             |
| 2015-2017 |        3 |               9 | Belgium;Denmark;Iceland;Japan;Lithuania;Netherlands;Slovakia;Spain;Switzerland             |
| 2016-2017 |        2 |              10 | Belgium;Denmark;Iceland;Japan;Lithuania;Netherlands;Slovakia;South Korea;Spain;Switzerland |

</details>

## Phase 13

<details>
<summary>Click to view full partition results for Phase 13...</summary>

| period    |   length |   num_countries | countries                                                                          |
|:----------|---------:|----------------:|:-----------------------------------------------------------------------------------|
| 2004-2022 |       19 |               1 | Spain                                                                              |
| 2004-2021 |       18 |               2 | Netherlands;Spain                                                                  |
| 2006-2021 |       16 |               3 | Netherlands;Spain;Switzerland                                                      |
| 2006-2017 |       12 |               4 | Iceland;Netherlands;Spain;Switzerland                                              |
| 2008-2017 |       10 |               5 | Iceland;Japan;Netherlands;Spain;Switzerland                                        |
| 2009-2017 |        9 |               6 | Iceland;Japan;Lithuania;Netherlands;Spain;Switzerland                              |
| 2015-2017 |        3 |               8 | Denmark;Iceland;Japan;Lithuania;Netherlands;Slovakia;Spain;Switzerland             |
| 2015-2017 |        3 |               8 | Denmark;Iceland;Japan;Lithuania;Netherlands;Slovakia;Spain;Switzerland             |
| 2016-2017 |        2 |               9 | Denmark;Iceland;Japan;Lithuania;Netherlands;Slovakia;South Korea;Spain;Switzerland |

</details>

## Phase 14

<details>
<summary>Click to view full partition results for Phase 14...</summary>

| period    |   length |   num_countries | countries                                                                    |
|:----------|---------:|----------------:|:-----------------------------------------------------------------------------|
| 2004-2021 |       18 |               1 | Netherlands                                                                  |
| 2006-2021 |       16 |               2 | Netherlands;Switzerland                                                      |
| 2006-2017 |       12 |               3 | Iceland;Netherlands;Switzerland                                              |
| 2008-2017 |       10 |               4 | Iceland;Japan;Netherlands;Switzerland                                        |
| 2009-2017 |        9 |               5 | Iceland;Japan;Lithuania;Netherlands;Switzerland                              |
| 2015-2017 |        3 |               7 | Denmark;Iceland;Japan;Lithuania;Netherlands;Slovakia;Switzerland             |
| 2015-2017 |        3 |               7 | Denmark;Iceland;Japan;Lithuania;Netherlands;Slovakia;Switzerland             |
| 2016-2017 |        2 |               8 | Denmark;Iceland;Japan;Lithuania;Netherlands;Slovakia;South Korea;Switzerland |

</details>

## Phase 15

<details>
<summary>Click to view full partition results for Phase 15...</summary>

| period    |   length |   num_countries | countries                                                        |
|:----------|---------:|----------------:|:-----------------------------------------------------------------|
| 2006-2022 |       17 |               1 | Switzerland                                                      |
| 2006-2017 |       12 |               2 | Iceland;Switzerland                                              |
| 2008-2017 |       10 |               3 | Iceland;Japan;Switzerland                                        |
| 2009-2017 |        9 |               4 | Iceland;Japan;Lithuania;Switzerland                              |
| 2015-2017 |        3 |               6 | Denmark;Iceland;Japan;Lithuania;Slovakia;Switzerland             |
| 2015-2017 |        3 |               6 | Denmark;Iceland;Japan;Lithuania;Slovakia;Switzerland             |
| 2016-2017 |        2 |               7 | Denmark;Iceland;Japan;Lithuania;Slovakia;South Korea;Switzerland |

</details>

