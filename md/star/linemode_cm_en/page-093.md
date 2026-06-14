**ESC * r P n NUL** [Name] Set raster page length [Code] ASCII ESC * r P n NUL Hex. 1B 2A 72 50 n 00 Decimal 27 42 114 80 n 0 [Defined Area] - - - [Initial Value] Raster image buffer length [Function] Sets raster page length. n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. n 0 Continuous print mode (no page length setting) 1≤n Specify page length 

## **ESC * r Q n NUL** 

[Name] Set raster print quality [Code] ASCII ESC * r Q n NUL Hex. 1B 2A 72 51 n 00 Decimal 27 42 114 81 n 0 [Defined Area] 0≤n≤2 [Initial Value] n = 0 [Function] Sets raster print quality. n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. 

|n|Print quality|
|---|---|
|0|Specifyhighspeed printing|
|1|Normal print quality|
|2|Highprintquality|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-75 
