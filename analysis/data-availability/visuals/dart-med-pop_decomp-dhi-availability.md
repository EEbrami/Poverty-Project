# Data Availability Visualization

This visualization shows data availability across years 1983-2023 for entities in the source file `xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv`. The grid displays 33 entities with their availability patterns.

```
Entity          | LS | Availability by Year
------------------------------------------------------------
Chile           |  1 |        █ █ █ █ █ █  █  █  █ █ █ █ █      
Czech Republic  |  1 |          █   █     █ █  █  █  █  █       
Estonia         |  1 |                  █   █  █  █  █  █       
Finland         |  1 |     █   █   █    █   █  █  █  █  █       
Hungary         |  1 |         █  █    █     █ █ █  █  █        
Slovenia        |  1 |               █ █    █  █  █ █  █        
Australia       |  2 |   █   █     █     █ ██   █ █   █ █ █ █   
Italy           |  2 | ██ ██ █ █ █ █  █ █ █ █ █ █ █ █ █ █   █   
Mexico          |  3 |  █    █  █ █ █ █ █ █ ███ █ █ █ █ █ █ █ █ 
Norway          |  4 |    █    █   █    █   █  █  █  █  █  ████ 
South Korea     |  6 |                        █ █ █ █ █ ██████  
Slovakia        |  6 |          █   █       █  █  █  ██████     
Denmark         |  8 |     █    █  █    █   █  █  █  █ ████████ 
Japan           | 13 |                          █████████████   
Lithuania       | 13 |                           █████████████  
Iceland         | 15 |                     ███████████████      
Switzerland     | 17 |          █       █ █ █ █████████████████ 
Netherlands     | 18 | █   █  █  █     █    ██████████████████  
Belgium         | 19 |   █  █   █  █ █  █  ███████████████████  
Spain           | 19 |   █    █  ████████   ███████████████████ 
Austria         | 20 |            ███████  ████████████████████ 
Greece          | 20 |             █    █ ████████████████████  
Ireland         | 20 |     █      ███   █ ████████████████████  
Poland          | 20 |    █     █  █   █    ████████████████████
Israel          | 21 |    █     █    █   █████████████████████  
Colombia        | 22 |                   ██████████████████████ 
Sweden          | 22 |     █    █  █    ██████████████████████  
France          | 27 |  █     █     ███████████████████████████ 
Canada          | 38 |  ██████████████████████████████████████  
Luxembourg      | 39 |   ███████████████████████████████████████
United Kingdom  | 39 | ███████████████████████████████████████  
Germany         | 40 | ████████████████████████████████████████ 
United States   | 40 | ████████████████████████████████████████ 
Universal       | 41 | █████████████████████████████████████████

                  |    | 1985    1990    1995    2000    2005    2010    2015    2020
```

## Summary

- **Number of entities**: 33
- **Year range**: 1983-2023
- **Total years**: 41
- **Tick interval**: 5 years
- **Sorting**: Entities are sorted by shortest longest-streak first

**Legend**: `█` = data available, ` ` (space) = data not available
**LS** = Longest Streak (maximum consecutive years with data)

The **Universal** row shows complete availability across all years.
