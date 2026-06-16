<!-- image -->

## ESC * r T n NUL

[Name] [Code]

Set raster top margin

ASCII

ESC * r T n NUL

Hex.

1B 2A 72 54 n 00

Decimal

27 42 114 84 n 0

[Defined Area]

0 ≤ n ≤ 2

[Initial Value]

---

[Function]

Sets the raster top margin.

n is a decimal description (max. 255 digits) using ASCII characters.

|   n | Top margin                               |
|-----|------------------------------------------|
|   0 | Set To Default                           |
|   1 | Set top margin using reverse paper feed. |
|   2 | Set standard top margin.                 |

The line mode top margin setting continues after entering the raster mode.

Also, the top margin setting of the raster mode continues after ending the raster mode, and returning to the line mode.

Invalid in page mode.

## ESC * r K n NUL

[Name] [Code]

Set raster print color

ASCII ESC * r K n NUL

Hex.

1B

2A

72

4B

n

00

Decimal

27 42 114 75 n 0

[Defined Area]

0 ≤ n ≤ 3

[Initial Value]

n = 0

[Function]

Sets raster print color.

This command is effective only when specifying the 2 color mode using the line mode.

This command is ignored when not in the 2 color print mode.

n is a decimal description (max. 255 digits) using ASCII characters.

Invalid in page mode.

|   n | Print color   |
|-----|---------------|
|   0 | Black         |
|   1 | Cyan          |
|   2 | Magenta       |
|   3 | Yellow        |

-----------------------------------------------------------------------------
