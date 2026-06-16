<!-- image -->

## ESC * r Y n NUL

[Name]

Move vertical direction position (Line feed for specified dots)

[Code]

ASCII ESC * r Y n NUL

Hex.

1B 2A 72 59 n 00

Decimal

27 42 114 89 n 0

[Defined Area]

- - -

[Initial Value]

- - -

[Function]

Moves vertical direction position.

Moves position n dots with this command.

When the current page length setting is in continuous print mode, and the n dots exceed the remaining dot count of the raster image buffer length, this moves up to the remaining dot count and ignores the overflow.

If the page length is set, it moves to the current page length and ignores the overflow.

Note that when there is overflow, this expands the next raster data after printing the raster image buffer data with the next raster data transfer and move vertical direction position command.

n is a decimal description (max. 255 digits) using ASCII characters.

Invalid in page mode.

-----------------------------------------------------------------------------
