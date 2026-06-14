**ESC * r D n NUL** [Name] Drawer drive [Code] ASCII ESC * r D n NUL Hex. 1B 2A 72 44 n 00 Decimal 27 42 114 68 n 0 

[Defined Area] 0≤n≤3 [Initial Value] n = 0 [Function] Drives the drawer in the raster mode. 

Drawer drive conditions conform to setting command (<ESC> <BEL> n1 n2) of the line mode. n is a decimal description (max. 255 digits) using ASCII characters. 

|n||Drive circuits|
|---|---|---|
|0||None|
|1||Externaldevice drive1drive|
|2||Externaldevice drive2drive|
|3||Externaldevice drive1drive and externaldevice drive2drive|
||Invalid in page mode.||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-72 
