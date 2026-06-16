<!-- image -->

Rev. 2.31

## ESC * r P n NUL

[Name]

Set raster page length

[Code]

ASCII ESC * r P n NUL

Hex 1B 2A 72 50 n 00

Decimal 27 42 114 80 n 0

[Defined Area]  0, 200 ≦ n ≦ 64000 (Other than TSP100IIU) 0, 200 ≦ n ≦ 32000 (TSP100IIU)

[Initial Value] ---

[Function]

Sets the raster page length.

nI is a decimal notation using ASCII characters (up to 255 digits)

If raster data exists in the image buffer of raster mode, this command is ignored.

TSP100U, TSP100PU, TSP100GT, TSP100LAN, TSP100IIIW, TSP100IIILAN, TSP100IIIBI 、 TSP100IIIU

| n               |                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------|
| 0               | Continuous printing mode (page length without setting, but maximum page length is 64000 dot) |
| 200 ≦ n ≦ 64000 | Specified page length                                                                        |

## TSP100IIU

| n               |                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------|
| 0               | Continuous printing mode (page length without setting, but maximum page length is 32000 dot) |
| 200 ≦ n ≦ 32000 | Specified page length                                                                        |

## ESC * r Q n NUL

[Name]

Set raster print quality

[Code]

ASCII ESC * r Q n NUL

Hex

1B 2A 72 51 n 00

Decimal 27 42 114 81 n 0

## [Defined Area]  0 ≦ n ≦ 2

[Initial Value]

n = 0

[Function]

Sets the raster print quality.

nI is a decimal notation using ASCII characters (up to 255 digits)

If raster data exists in the image buffer of raster mode, this command is ignored.

|   n | Print quality                 |
|-----|-------------------------------|
|   0 | High-speed printing specified |
|   1 | Normal print quality          |
|   2 | High print quality            |

--------------------------------------------------------------------------------------
