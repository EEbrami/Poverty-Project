# Data Availability Submatrix Results

This summary aggregates results from multiple algorithms that search for the largest all-ones submatrix in the country-by-year availability matrix.

Metrics:
- num_countries: number of countries fully covered
- length: number of years in the partition
- partition: explicit years (for non-consecutive selections); consecutive intervals also show 'period'

| Rank | Algorithm | Countries | Length | Area | Period | Partition (years) |
| ---- | --------- | --------- | ------ | ---- | ------ | ----------------- |
| 1 | greedy_pivot_coverage_phase1#row10 | 16 | 18 | 288 | 2004–2021 | 2004, …, 2021 (18 years) |
| 2 | greedy_pivot_coverage_phase1#row11 | 16 | 18 | 288 | 2004–2021 | 2004, …, 2021 (18 years) |
| 3 | greedy_pivot_coverage_phase1#row12 | 16 | 18 | 288 | 2004–2021 | 2004, …, 2021 (18 years) |
| 4 | greedy_pivot_coverage_phase1#row13 | 17 | 16 | 272 | 2006–2021 | 2006, …, 2021 (16 years) |
| 5 | greedy_pivot_coverage_phase2#row9 | 14 | 18 | 252 | 2004–2021 | 2004, …, 2021 (18 years) |
| 6 | greedy_pivot_coverage_phase2#row10 | 14 | 18 | 252 | 2004–2021 | 2004, …, 2021 (18 years) |
| 7 | greedy_pivot_coverage_phase2#row11 | 14 | 18 | 252 | 2004–2021 | 2004, …, 2021 (18 years) |
| 8 | greedy_pivot_coverage_phase1#row9 | 13 | 19 | 247 | 2003–2021 | 2003, …, 2021 (19 years) |
| 9 | greedy_pivot_coverage_phase2#row12 | 15 | 16 | 240 | 2006–2021 | 2006, …, 2021 (16 years) |
| 10 | greedy_pivot_coverage_phase1#row8 | 11 | 20 | 220 | 2002–2021 | 2002, …, 2021 (20 years) |
| 11 | greedy_pivot_coverage_phase1#row14 | 18 | 12 | 216 | 2006–2017 | 2006, …, 2017 (12 years) |
| 12 | greedy_pivot_coverage_phase2#row8 | 11 | 19 | 209 | 2003–2021 | 2003, …, 2021 (19 years) |
| 13 | greedy_pivot_coverage_phase2#row13 | 16 | 12 | 192 | 2006–2017 | 2006, …, 2017 (12 years) |
| 14 | greedy_pivot_coverage_phase1#row15 | 19 | 10 | 190 | 2008–2017 | 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 |
| 15 | greedy_pivot_coverage_phase1#row7 | 9 | 21 | 189 | 2001–2021 | 2001, …, 2021 (21 years) |
| 16 | greedy_pivot_coverage_phase1#row3 | 5 | 37 | 185 | 1985–2021 | 1985, …, 2021 (37 years) |
| 17 | greedy_pivot_coverage_phase1#row4 | 5 | 37 | 185 | 1985–2021 | 1985, …, 2021 (37 years) |
| 18 | greedy_pivot_coverage_phase1#row16 | 20 | 9 | 180 | 2009–2017 | 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 |
| 19 | greedy_pivot_coverage_phase2#row7 | 9 | 20 | 180 | 2002–2021 | 2002, …, 2021 (20 years) |
| 20 | greedy_pivot_coverage_phase2#row14 | 17 | 10 | 170 | 2008–2017 | 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 |
| 21 | greedy_pivot_coverage_phase2#row15 | 18 | 9 | 162 | 2009–2017 | 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 |
| 22 | greedy_pivot_coverage_phase1#row5 | 6 | 26 | 156 | 1996–2021 | 1996, …, 2021 (26 years) |
| 23 | greedy_pivot_coverage_phase1#row6 | 7 | 22 | 154 | 2000–2021 | 2000, …, 2021 (22 years) |
| 24 | greedy_pivot_coverage_phase2#row6 | 7 | 21 | 147 | 2001–2021 | 2001, …, 2021 (21 years) |
| 25 | greedy_pivot_coverage_phase1#row2 | 3 | 39 | 117 | 1983–2021 | 1983, …, 2021 (39 years) |
| 26 | greedy_pivot_coverage_phase2#row2 | 3 | 37 | 111 | 1985–2021 | 1985, …, 2021 (37 years) |
| 27 | greedy_pivot_coverage_phase2#row3 | 3 | 37 | 111 | 1985–2021 | 1985, …, 2021 (37 years) |
| 28 | greedy_pivot_coverage_phase2#row5 | 5 | 22 | 110 | 2000–2021 | 2000, …, 2021 (22 years) |
| 29 | greedy_pivot_coverage_phase2#row4 | 4 | 26 | 104 | 1996–2021 | 1996, …, 2021 (26 years) |
| 30 | greedy_longest_streak_phase1_equal#row1 | 2 | 40 | 80 | 1983–2022 | 1983, …, 2022 (40 years) |
| 31 | greedy_pivot_coverage_phase1#row1 | 2 | 40 | 80 | 1983–2022 | 1983, …, 2022 (40 years) |
| 32 | greedy_pivot_coverage_phase1#row17 | 22 | 3 | 66 | 2015–2017 | 2015, 2016, 2017 |
| 33 | greedy_pivot_coverage_phase1#row18 | 22 | 3 | 66 | 2015–2017 | 2015, 2016, 2017 |
| 34 | best_window_3y_any_start | 22 | 3 | 66 | 2015–2017 | 2015, 2016, 2017 |
| 35 | best_window_3y_offset0 | 22 | 3 | 66 | 2016–2018 | 2016, 2017, 2018 |
| 36 | best_window_3y_offset2 | 22 | 3 | 66 | 2015–2017 | 2015, 2016, 2017 |
| 37 | best_window_3y_offset1 | 21 | 3 | 63 | 2014–2016 | 2014, 2015, 2016 |
| 38 | greedy_pivot_coverage_phase2#row16 | 20 | 3 | 60 | 2015–2017 | 2015, 2016, 2017 |
| 39 | greedy_pivot_coverage_phase2#row17 | 20 | 3 | 60 | 2015–2017 | 2015, 2016, 2017 |
| 40 | greedy_pivot_coverage_phase1#row19 | 23 | 2 | 46 | 2016–2017 | 2016, 2017 |
| 41 | best_window_2y_any_start | 23 | 2 | 46 | 2016–2017 | 2016, 2017 |
| 42 | best_window_2y_offset1 | 23 | 2 | 46 | 2016–2017 | 2016, 2017 |
| 43 | best_window_2y_offset0 | 22 | 2 | 44 | 2015–2016 | 2015, 2016 |
| 44 | greedy_pivot_coverage_phase2#row18 | 21 | 2 | 42 | 2016–2017 | 2016, 2017 |
| 45 | greedy_longest_streak_phase1_equal#row8 | 2 | 20 | 40 | 2002–2021 | 2002, …, 2021 (20 years) |
| 46 | greedy_longest_streak_phase2_equal#row7 | 2 | 20 | 40 | 2002–2021 | 2002, …, 2021 (20 years) |
| 47 | greedy_longest_streak_phase1_equal#row2 | 1 | 39 | 39 | 1983–2021 | 1983, …, 2021 (39 years) |
| 48 | greedy_longest_streak_phase2_equal#row1 | 1 | 39 | 39 | 1983–2021 | 1983, …, 2021 (39 years) |
| 49 | greedy_pivot_coverage_phase2#row1 | 1 | 39 | 39 | 1983–2021 | 1983, …, 2021 (39 years) |
| 50 | best_consecutive_window | 31 | 1 | 31 | 2010–2010 | 2010 |
| 51 | greedy_longest_streak_phase1_equal#row6 | 1 | 22 | 22 | 2000–2021 | 2000, …, 2021 (22 years) |
| 52 | greedy_longest_streak_phase2_equal#row5 | 1 | 22 | 22 | 2000–2021 | 2000, …, 2021 (22 years) |
| 53 | greedy_longest_streak_phase1_equal#row7 | 1 | 21 | 21 | 2001–2021 | 2001, …, 2021 (21 years) |
| 54 | greedy_longest_streak_phase2_equal#row6 | 1 | 21 | 21 | 2001–2021 | 2001, …, 2021 (21 years) |
| 55 | greedy_longest_streak_phase1_equal#row12 | 1 | 18 | 18 | 2004–2021 | 2004, …, 2021 (18 years) |
| 56 | greedy_longest_streak_phase2_equal#row11 | 1 | 18 | 18 | 2004–2021 | 2004, …, 2021 (18 years) |
| 57 | greedy_longest_streak_phase1_equal#row3 | 0 | 37 | 0 | 1985–2021 | 1985, …, 2021 (37 years) |
| 58 | greedy_longest_streak_phase1_equal#row4 | 0 | 37 | 0 | 1985–2021 | 1985, …, 2021 (37 years) |
| 59 | greedy_longest_streak_phase2_equal#row2 | 0 | 37 | 0 | 1985–2021 | 1985, …, 2021 (37 years) |
| 60 | greedy_longest_streak_phase2_equal#row3 | 0 | 37 | 0 | 1985–2021 | 1985, …, 2021 (37 years) |
| 61 | greedy_longest_streak_phase1_equal#row5 | 0 | 26 | 0 | 1996–2021 | 1996, …, 2021 (26 years) |
| 62 | greedy_longest_streak_phase2_equal#row4 | 0 | 26 | 0 | 1996–2021 | 1996, …, 2021 (26 years) |
| 63 | greedy_longest_streak_phase1_equal#row9 | 0 | 19 | 0 | 2003–2021 | 2003, …, 2021 (19 years) |
| 64 | greedy_longest_streak_phase2_equal#row8 | 0 | 19 | 0 | 2003–2021 | 2003, …, 2021 (19 years) |
| 65 | greedy_longest_streak_phase1_equal#row10 | 0 | 18 | 0 | 2004–2021 | 2004, …, 2021 (18 years) |
| 66 | greedy_longest_streak_phase1_equal#row11 | 0 | 18 | 0 | 2004–2021 | 2004, …, 2021 (18 years) |
| 67 | greedy_longest_streak_phase2_equal#row9 | 0 | 18 | 0 | 2004–2021 | 2004, …, 2021 (18 years) |
| 68 | greedy_longest_streak_phase2_equal#row10 | 0 | 18 | 0 | 2004–2021 | 2004, …, 2021 (18 years) |
| 69 | greedy_longest_streak_phase1_equal#row13 | 0 | 16 | 0 | 2006–2021 | 2006, …, 2021 (16 years) |
| 70 | greedy_longest_streak_phase2_equal#row12 | 0 | 16 | 0 | 2006–2021 | 2006, …, 2021 (16 years) |
| 71 | greedy_longest_streak_phase1_equal#row14 | 0 | 12 | 0 | 2006–2017 | 2006, …, 2017 (12 years) |
| 72 | greedy_longest_streak_phase2_equal#row13 | 0 | 12 | 0 | 2006–2017 | 2006, …, 2017 (12 years) |
| 73 | greedy_longest_streak_phase1_equal#row15 | 0 | 10 | 0 | 2008–2017 | 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 |
| 74 | greedy_longest_streak_phase2_equal#row14 | 0 | 10 | 0 | 2008–2017 | 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 |
| 75 | greedy_longest_streak_phase1_equal#row16 | 0 | 9 | 0 | 2009–2017 | 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 |
| 76 | greedy_longest_streak_phase2_equal#row15 | 0 | 9 | 0 | 2009–2017 | 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017 |
| 77 | greedy_longest_streak_phase1_equal#row17 | 0 | 3 | 0 | 2015–2017 | 2015, 2016, 2017 |
| 78 | greedy_longest_streak_phase1_equal#row18 | 0 | 3 | 0 | 2015–2017 | 2015, 2016, 2017 |
| 79 | greedy_longest_streak_phase2_equal#row16 | 0 | 3 | 0 | 2015–2017 | 2015, 2016, 2017 |
| 80 | greedy_longest_streak_phase2_equal#row17 | 0 | 3 | 0 | 2015–2017 | 2015, 2016, 2017 |
| 81 | greedy_longest_streak_phase1_equal#row19 | 0 | 2 | 0 | 2016–2017 | 2016, 2017 |
| 82 | greedy_longest_streak_phase2_equal#row18 | 0 | 2 | 0 | 2016–2017 | 2016, 2017 |
| 83 | max_biclique_any_years | 0 | 0 | 0 |  |  |

## Top Results Detail

### 1. greedy_pivot_coverage_phase1#row10

- Countries: 16
- Length: 18
- Period: 2004–2021
- Partition (years): 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021
- Countries list (first 20): Austria, Belgium, Canada, Colombia, France, Germany, Greece, Ireland, Israel, Luxembourg, Netherlands, Poland, Spain, Sweden, United Kingdom, United States

### 2. greedy_pivot_coverage_phase1#row11

- Countries: 16
- Length: 18
- Period: 2004–2021
- Partition (years): 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021
- Countries list (first 20): Austria, Belgium, Canada, Colombia, France, Germany, Greece, Ireland, Israel, Luxembourg, Netherlands, Poland, Spain, Sweden, United Kingdom, United States

### 3. greedy_pivot_coverage_phase1#row12

- Countries: 16
- Length: 18
- Period: 2004–2021
- Partition (years): 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021
- Countries list (first 20): Austria, Belgium, Canada, Colombia, France, Germany, Greece, Ireland, Israel, Luxembourg, Netherlands, Poland, Spain, Sweden, United Kingdom, United States

### 4. greedy_pivot_coverage_phase1#row13

- Countries: 17
- Length: 16
- Period: 2006–2021
- Partition (years): 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021
- Countries list (first 20): Austria, Belgium, Canada, Colombia, France, Germany, Greece, Ireland, Israel, Luxembourg, Netherlands, Poland, Spain, Sweden, Switzerland, United Kingdom, United States

### 5. greedy_pivot_coverage_phase2#row9

- Countries: 14
- Length: 18
- Period: 2004–2021
- Partition (years): 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021
- Countries list (first 20): Austria, Belgium, Canada, Colombia, France, Greece, Ireland, Israel, Luxembourg, Netherlands, Poland, Spain, Sweden, United Kingdom

