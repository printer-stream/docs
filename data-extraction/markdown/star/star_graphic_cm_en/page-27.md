<!-- image -->

Rev. 2.31

## ESC * r D n NUL

[Name]

Drive drawer

[Code]

ASCII ESC * r D n NUL

Hex

1B 2A 72 44 n 00

Decimal 27 42 114 68 n

## [Defined Area]  0 ≦ n ≦ 3

[Initial Value] n = 0

[Function]

Executes the drawer drive during raster mode.

Drawer driving conditions is equivalent to the conditions set by the line mode.

nI is a decimal notation using ASCII characters (up to 255 digits)

If raster data exists in the image buffer of raster mode, this command is ignored.

|   n | Drive circuit                                                 |
|-----|---------------------------------------------------------------|
|   0 | None                                                          |
|   1 | Drive external device drive 1                                 |
|   2 | Drive external device drive 2                                 |
|   3 | Drive external device drive 1 + Drive external device drive 2 |

## ESC * r E n NUL

[Name]

Set raster EOT mode

[Code]

ASCII

ESC * r E n NUL

Hex

1B 2A 72 45 n 00

Decimal

27 42 114 69 n 0

## [Defined Area]  n = 0, 1, 2, 3, 8, 9, 12, 13, 32, 33, 36, 37

[Initial Value] Cutter model n = 13

TearBar model n = 3

[Function]

Sets the raster EOT mode.

The EOT mode is an operation to be performed by the raster document end command (ESC FF EOT). nI is a decimal notation using ASCII characters (up to 255 digits)

If raster data exists in the image buffer of raster mode, this command is ignored.

## &lt;EOT mode setting format&gt;

| n   | Model   | Model   | Function       | Function       | Function       |
|-----|---------|---------|----------------|----------------|----------------|
| n   | Cutter  | TearBar | FormFeed       | Cut Feed       | Cutter         |
| 0   | Valid   | Valid   | Set To Default | Set To Default | Set To Default |
| 1   | Valid   | Valid   | OK             | －－             | －－             |
| 2   | Valid   | Invalid | OK             | OK             | －－             |
| 3   | Invalid | Valid   | OK             | TearBar        | －－             |
| 8   | Valid   | Invalid | OK             | －－             | Full Cut       |
| 9   | Valid   | Invalid | OK             | OK             | Full Cut       |
| 12  | Valid   | Invalid | OK             | －－             | Partial Cut    |
| 13  | Valid   | Invalid | OK             | OK             | Partial Cut    |
| 32  | Invalid | Invalid |                |                |                |
| 33  | Invalid | Invalid |                |                |                |
| 36  | Invalid | Invalid |                |                |                |
| 37  | Invalid | Invalid |                |                |                |

--------------------------------------------------------------------------------------

0
