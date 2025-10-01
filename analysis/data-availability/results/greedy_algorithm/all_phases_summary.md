# Data Availability Analysis: 15-Phase Greedy Coverage Algorithm

This document contains results from 15 sequential exclusion phases using the Coverage-based pivot shrink (A1b) algorithm.

Each phase excludes countries from previous phases and finds the optimal submatrix of remaining data.

## Phase 1

<details>
<summary>Click to view full partition results for Phase 1...</summary>

| period    |   length |   num_countries | countries                                                                                                                                                                  |
|:----------|---------:|----------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1983-2022 |       40 |               1 | United States                                                                                                                                                              |
| 1983-2021 |       39 |               2 | United Kingdom;United States                                                                                                                                               |
| 1984-2021 |       38 |               3 | Canada;United Kingdom;United States                                                                                                                                        |
| 1985-2021 |       37 |               4 | Canada;Germany;United Kingdom;United States                                                                                                                                |
| 2000-2021 |       22 |               5 | Canada;Germany;Sweden;United Kingdom;United States                                                                                                                         |
| 2001-2021 |       21 |               6 | Canada;Germany;Israel;Sweden;United Kingdom;United States                                                                                                                  |
| 2002-2021 |       20 |               7 | Canada;Germany;Ireland;Israel;Sweden;United Kingdom;United States                                                                                                          |
| 2003-2021 |       19 |               8 | Belgium;Canada;Germany;Ireland;Israel;Sweden;United Kingdom;United States                                                                                                  |
| 2004-2021 |       18 |              10 | Belgium;Canada;Germany;Ireland;Israel;Netherlands;Spain;Sweden;United Kingdom;United States                                                                                |
| 2004-2019 |       16 |              11 | Belgium;Canada;Germany;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;United Kingdom;United States                                                                     |
| 2004-2019 |       16 |              11 | Belgium;Canada;Germany;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;United Kingdom;United States                                                                     |
| 2006-2019 |       14 |              13 | Belgium;Canada;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom;United States                                                  |
| 2006-2019 |       14 |              13 | Belgium;Canada;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom;United States                                                  |
| 2007-2019 |       13 |              14 | Austria;Belgium;Canada;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom;United States                                          |
| 2007-2017 |       11 |              15 | Austria;Belgium;Canada;Germany;Greece;Iceland;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom;United States                                  |
| 2008-2017 |       10 |              16 | Austria;Belgium;Canada;Germany;Greece;Iceland;Ireland;Israel;Japan;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom;United States                            |
| 2009-2017 |        9 |              17 | Austria;Belgium;Canada;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom;United States                  |
| 2015-2017 |        3 |              19 | Austria;Belgium;Canada;Denmark;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Sweden;Switzerland;United Kingdom;United States |
| 2015-2017 |        3 |              19 | Austria;Belgium;Canada;Denmark;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Sweden;Switzerland;United Kingdom;United States |

</details>

## Phase 2

<details>
<summary>Click to view full partition results for Phase 2...</summary>

| period    |   length |   num_countries | countries                                                                                                                                                    |
|:----------|---------:|----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1983-2021 |       39 |               1 | United Kingdom                                                                                                                                               |
| 1984-2021 |       38 |               2 | Canada;United Kingdom                                                                                                                                        |
| 1985-2021 |       37 |               3 | Canada;Germany;United Kingdom                                                                                                                                |
| 2000-2021 |       22 |               4 | Canada;Germany;Sweden;United Kingdom                                                                                                                         |
| 2001-2021 |       21 |               5 | Canada;Germany;Israel;Sweden;United Kingdom                                                                                                                  |
| 2002-2021 |       20 |               6 | Canada;Germany;Ireland;Israel;Sweden;United Kingdom                                                                                                          |
| 2003-2021 |       19 |               7 | Belgium;Canada;Germany;Ireland;Israel;Sweden;United Kingdom                                                                                                  |
| 2004-2021 |       18 |               9 | Belgium;Canada;Germany;Ireland;Israel;Netherlands;Spain;Sweden;United Kingdom                                                                                |
| 2004-2019 |       16 |              10 | Belgium;Canada;Germany;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;United Kingdom                                                                     |
| 2004-2019 |       16 |              10 | Belgium;Canada;Germany;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;United Kingdom                                                                     |
| 2006-2019 |       14 |              12 | Belgium;Canada;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom                                                  |
| 2006-2019 |       14 |              12 | Belgium;Canada;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom                                                  |
| 2007-2019 |       13 |              13 | Austria;Belgium;Canada;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom                                          |
| 2007-2017 |       11 |              14 | Austria;Belgium;Canada;Germany;Greece;Iceland;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom                                  |
| 2008-2017 |       10 |              15 | Austria;Belgium;Canada;Germany;Greece;Iceland;Ireland;Israel;Japan;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom                            |
| 2009-2017 |        9 |              16 | Austria;Belgium;Canada;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Spain;Sweden;Switzerland;United Kingdom                  |
| 2015-2017 |        3 |              18 | Austria;Belgium;Canada;Denmark;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Sweden;Switzerland;United Kingdom |
| 2015-2017 |        3 |              18 | Austria;Belgium;Canada;Denmark;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Sweden;Switzerland;United Kingdom |

</details>

## Phase 3

<details>
<summary>Click to view full partition results for Phase 3...</summary>

| period    |   length |   num_countries | countries                                                                                                                                     |
|:----------|---------:|----------------:|:----------------------------------------------------------------------------------------------------------------------------------------------|
| 1984-2021 |       38 |               1 | Canada                                                                                                                                        |
| 1985-2021 |       37 |               2 | Canada;Germany                                                                                                                                |
| 2000-2021 |       22 |               3 | Canada;Germany;Sweden                                                                                                                         |
| 2001-2021 |       21 |               4 | Canada;Germany;Israel;Sweden                                                                                                                  |
| 2002-2021 |       20 |               5 | Canada;Germany;Ireland;Israel;Sweden                                                                                                          |
| 2003-2021 |       19 |               6 | Belgium;Canada;Germany;Ireland;Israel;Sweden                                                                                                  |
| 2004-2021 |       18 |               8 | Belgium;Canada;Germany;Ireland;Israel;Netherlands;Spain;Sweden                                                                                |
| 2004-2019 |       16 |               9 | Belgium;Canada;Germany;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden                                                                     |
| 2004-2019 |       16 |               9 | Belgium;Canada;Germany;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden                                                                     |
| 2006-2019 |       14 |              11 | Belgium;Canada;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                                  |
| 2006-2019 |       14 |              11 | Belgium;Canada;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                                  |
| 2007-2019 |       13 |              12 | Austria;Belgium;Canada;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                          |
| 2007-2017 |       11 |              13 | Austria;Belgium;Canada;Germany;Greece;Iceland;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                  |
| 2008-2017 |       10 |              14 | Austria;Belgium;Canada;Germany;Greece;Iceland;Ireland;Israel;Japan;Luxembourg;Netherlands;Spain;Sweden;Switzerland                            |
| 2009-2017 |        9 |              15 | Austria;Belgium;Canada;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Spain;Sweden;Switzerland                  |
| 2015-2017 |        3 |              17 | Austria;Belgium;Canada;Denmark;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Sweden;Switzerland |
| 2015-2017 |        3 |              17 | Austria;Belgium;Canada;Denmark;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Sweden;Switzerland |

</details>

## Phase 4

<details>
<summary>Click to view full partition results for Phase 4...</summary>

| period    |   length |   num_countries | countries                                                                                                                              |
|:----------|---------:|----------------:|:---------------------------------------------------------------------------------------------------------------------------------------|
| 1985-2022 |       38 |               1 | Germany                                                                                                                                |
| 2000-2021 |       22 |               2 | Germany;Sweden                                                                                                                         |
| 2001-2021 |       21 |               3 | Germany;Israel;Sweden                                                                                                                  |
| 2002-2021 |       20 |               4 | Germany;Ireland;Israel;Sweden                                                                                                          |
| 2003-2021 |       19 |               5 | Belgium;Germany;Ireland;Israel;Sweden                                                                                                  |
| 2004-2021 |       18 |               7 | Belgium;Germany;Ireland;Israel;Netherlands;Spain;Sweden                                                                                |
| 2004-2019 |       16 |               8 | Belgium;Germany;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden                                                                     |
| 2004-2019 |       16 |               8 | Belgium;Germany;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden                                                                     |
| 2006-2019 |       14 |              10 | Belgium;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                                  |
| 2006-2019 |       14 |              10 | Belgium;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                                  |
| 2007-2019 |       13 |              11 | Austria;Belgium;Germany;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                          |
| 2007-2017 |       11 |              12 | Austria;Belgium;Germany;Greece;Iceland;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                  |
| 2008-2017 |       10 |              13 | Austria;Belgium;Germany;Greece;Iceland;Ireland;Israel;Japan;Luxembourg;Netherlands;Spain;Sweden;Switzerland                            |
| 2009-2017 |        9 |              14 | Austria;Belgium;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Spain;Sweden;Switzerland                  |
| 2015-2017 |        3 |              16 | Austria;Belgium;Denmark;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Sweden;Switzerland |
| 2015-2017 |        3 |              16 | Austria;Belgium;Denmark;Germany;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Sweden;Switzerland |

</details>

## Phase 5

<details>
<summary>Click to view full partition results for Phase 5...</summary>

| period    |   length |   num_countries | countries                                                                                                                      |
|:----------|---------:|----------------:|:-------------------------------------------------------------------------------------------------------------------------------|
| 2000-2021 |       22 |               1 | Sweden                                                                                                                         |
| 2001-2021 |       21 |               2 | Israel;Sweden                                                                                                                  |
| 2002-2021 |       20 |               3 | Ireland;Israel;Sweden                                                                                                          |
| 2003-2021 |       19 |               4 | Belgium;Ireland;Israel;Sweden                                                                                                  |
| 2004-2021 |       18 |               6 | Belgium;Ireland;Israel;Netherlands;Spain;Sweden                                                                                |
| 2004-2019 |       16 |               7 | Belgium;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden                                                                     |
| 2004-2019 |       16 |               7 | Belgium;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden                                                                     |
| 2006-2019 |       14 |               9 | Belgium;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                                  |
| 2006-2019 |       14 |               9 | Belgium;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                                  |
| 2007-2019 |       13 |              10 | Austria;Belgium;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                          |
| 2007-2017 |       11 |              11 | Austria;Belgium;Greece;Iceland;Ireland;Israel;Luxembourg;Netherlands;Spain;Sweden;Switzerland                                  |
| 2008-2017 |       10 |              12 | Austria;Belgium;Greece;Iceland;Ireland;Israel;Japan;Luxembourg;Netherlands;Spain;Sweden;Switzerland                            |
| 2009-2017 |        9 |              13 | Austria;Belgium;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Spain;Sweden;Switzerland                  |
| 2015-2017 |        3 |              15 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Sweden;Switzerland |
| 2015-2017 |        3 |              15 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Sweden;Switzerland |

</details>

## Phase 6

<details>
<summary>Click to view full partition results for Phase 6...</summary>

| period    |   length |   num_countries | countries                                                                                                               |
|:----------|---------:|----------------:|:------------------------------------------------------------------------------------------------------------------------|
| 2001-2021 |       21 |               1 | Israel                                                                                                                  |
| 2002-2021 |       20 |               2 | Ireland;Israel                                                                                                          |
| 2003-2021 |       19 |               3 | Belgium;Ireland;Israel                                                                                                  |
| 2004-2021 |       18 |               5 | Belgium;Ireland;Israel;Netherlands;Spain                                                                                |
| 2004-2019 |       16 |               6 | Belgium;Ireland;Israel;Luxembourg;Netherlands;Spain                                                                     |
| 2004-2019 |       16 |               6 | Belgium;Ireland;Israel;Luxembourg;Netherlands;Spain                                                                     |
| 2006-2019 |       14 |               8 | Belgium;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Switzerland                                                  |
| 2006-2019 |       14 |               8 | Belgium;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Switzerland                                                  |
| 2007-2019 |       13 |               9 | Austria;Belgium;Greece;Ireland;Israel;Luxembourg;Netherlands;Spain;Switzerland                                          |
| 2007-2017 |       11 |              10 | Austria;Belgium;Greece;Iceland;Ireland;Israel;Luxembourg;Netherlands;Spain;Switzerland                                  |
| 2008-2017 |       10 |              11 | Austria;Belgium;Greece;Iceland;Ireland;Israel;Japan;Luxembourg;Netherlands;Spain;Switzerland                            |
| 2009-2017 |        9 |              12 | Austria;Belgium;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Spain;Switzerland                  |
| 2015-2017 |        3 |              14 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Switzerland |
| 2015-2017 |        3 |              14 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Israel;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Switzerland |

</details>

## Phase 7

<details>
<summary>Click to view full partition results for Phase 7...</summary>

| period    |   length |   num_countries | countries                                                                                                        |
|:----------|---------:|----------------:|:-----------------------------------------------------------------------------------------------------------------|
| 2002-2021 |       20 |               1 | Ireland                                                                                                          |
| 2003-2021 |       19 |               2 | Belgium;Ireland                                                                                                  |
| 2004-2021 |       18 |               4 | Belgium;Ireland;Netherlands;Spain                                                                                |
| 2004-2019 |       16 |               5 | Belgium;Ireland;Luxembourg;Netherlands;Spain                                                                     |
| 2004-2019 |       16 |               5 | Belgium;Ireland;Luxembourg;Netherlands;Spain                                                                     |
| 2006-2019 |       14 |               7 | Belgium;Greece;Ireland;Luxembourg;Netherlands;Spain;Switzerland                                                  |
| 2006-2019 |       14 |               7 | Belgium;Greece;Ireland;Luxembourg;Netherlands;Spain;Switzerland                                                  |
| 2007-2019 |       13 |               8 | Austria;Belgium;Greece;Ireland;Luxembourg;Netherlands;Spain;Switzerland                                          |
| 2007-2017 |       11 |               9 | Austria;Belgium;Greece;Iceland;Ireland;Luxembourg;Netherlands;Spain;Switzerland                                  |
| 2008-2017 |       10 |              10 | Austria;Belgium;Greece;Iceland;Ireland;Japan;Luxembourg;Netherlands;Spain;Switzerland                            |
| 2009-2017 |        9 |              11 | Austria;Belgium;Greece;Iceland;Ireland;Japan;Lithuania;Luxembourg;Netherlands;Spain;Switzerland                  |
| 2015-2017 |        3 |              13 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Switzerland |
| 2015-2017 |        3 |              13 | Austria;Belgium;Denmark;Greece;Iceland;Ireland;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Switzerland |

</details>

## Phase 8

<details>
<summary>Click to view full partition results for Phase 8...</summary>

| period    |   length |   num_countries | countries                                                                                                |
|:----------|---------:|----------------:|:---------------------------------------------------------------------------------------------------------|
| 2003-2021 |       19 |               1 | Belgium                                                                                                  |
| 2004-2021 |       18 |               3 | Belgium;Netherlands;Spain                                                                                |
| 2004-2019 |       16 |               4 | Belgium;Luxembourg;Netherlands;Spain                                                                     |
| 2004-2019 |       16 |               4 | Belgium;Luxembourg;Netherlands;Spain                                                                     |
| 2006-2019 |       14 |               6 | Belgium;Greece;Luxembourg;Netherlands;Spain;Switzerland                                                  |
| 2006-2019 |       14 |               6 | Belgium;Greece;Luxembourg;Netherlands;Spain;Switzerland                                                  |
| 2007-2019 |       13 |               7 | Austria;Belgium;Greece;Luxembourg;Netherlands;Spain;Switzerland                                          |
| 2007-2017 |       11 |               8 | Austria;Belgium;Greece;Iceland;Luxembourg;Netherlands;Spain;Switzerland                                  |
| 2008-2017 |       10 |               9 | Austria;Belgium;Greece;Iceland;Japan;Luxembourg;Netherlands;Spain;Switzerland                            |
| 2009-2017 |        9 |              10 | Austria;Belgium;Greece;Iceland;Japan;Lithuania;Luxembourg;Netherlands;Spain;Switzerland                  |
| 2015-2017 |        3 |              12 | Austria;Belgium;Denmark;Greece;Iceland;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Switzerland |
| 2015-2017 |        3 |              12 | Austria;Belgium;Denmark;Greece;Iceland;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Switzerland |

</details>

## Phase 9

<details>
<summary>Click to view full partition results for Phase 9...</summary>

| period    |   length |   num_countries | countries                                                                                        |
|:----------|---------:|----------------:|:-------------------------------------------------------------------------------------------------|
| 2004-2022 |       19 |               1 | Spain                                                                                            |
| 2004-2019 |       16 |               3 | Luxembourg;Netherlands;Spain                                                                     |
| 2004-2019 |       16 |               3 | Luxembourg;Netherlands;Spain                                                                     |
| 2006-2019 |       14 |               5 | Greece;Luxembourg;Netherlands;Spain;Switzerland                                                  |
| 2006-2019 |       14 |               5 | Greece;Luxembourg;Netherlands;Spain;Switzerland                                                  |
| 2007-2019 |       13 |               6 | Austria;Greece;Luxembourg;Netherlands;Spain;Switzerland                                          |
| 2007-2017 |       11 |               7 | Austria;Greece;Iceland;Luxembourg;Netherlands;Spain;Switzerland                                  |
| 2008-2017 |       10 |               8 | Austria;Greece;Iceland;Japan;Luxembourg;Netherlands;Spain;Switzerland                            |
| 2009-2017 |        9 |               9 | Austria;Greece;Iceland;Japan;Lithuania;Luxembourg;Netherlands;Spain;Switzerland                  |
| 2015-2017 |        3 |              11 | Austria;Denmark;Greece;Iceland;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Switzerland |
| 2015-2017 |        3 |              11 | Austria;Denmark;Greece;Iceland;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Spain;Switzerland |

</details>

## Phase 10

<details>
<summary>Click to view full partition results for Phase 10...</summary>

| period    |   length |   num_countries | countries                                                                                  |
|:----------|---------:|----------------:|:-------------------------------------------------------------------------------------------|
| 2002-2019 |       18 |               1 | Luxembourg                                                                                 |
| 2004-2019 |       16 |               2 | Luxembourg;Netherlands                                                                     |
| 2006-2019 |       14 |               4 | Greece;Luxembourg;Netherlands;Switzerland                                                  |
| 2006-2019 |       14 |               4 | Greece;Luxembourg;Netherlands;Switzerland                                                  |
| 2007-2019 |       13 |               5 | Austria;Greece;Luxembourg;Netherlands;Switzerland                                          |
| 2007-2017 |       11 |               6 | Austria;Greece;Iceland;Luxembourg;Netherlands;Switzerland                                  |
| 2008-2017 |       10 |               7 | Austria;Greece;Iceland;Japan;Luxembourg;Netherlands;Switzerland                            |
| 2009-2017 |        9 |               8 | Austria;Greece;Iceland;Japan;Lithuania;Luxembourg;Netherlands;Switzerland                  |
| 2015-2017 |        3 |              10 | Austria;Denmark;Greece;Iceland;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Switzerland |
| 2015-2017 |        3 |              10 | Austria;Denmark;Greece;Iceland;Japan;Lithuania;Luxembourg;Netherlands;Slovakia;Switzerland |

</details>

