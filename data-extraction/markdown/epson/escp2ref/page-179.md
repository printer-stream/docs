## Format

ASCII ESC . c v h m nL nH d1 d2 . . . dk

<!-- formula-not-decoded -->

## Parameter range

c = 0

c = 1

v = 5 ,10, 20

h = 5 ,10, 20

<!-- formula-not-decoded -->

0 ≤ nL ≤ 255

0 ≤ nH ≤ 127

0 ≤ d ≤ 255

The following vertical and horizontal printing resolution combinations are available:

|   v |   h |   v (dpi) |   h (dpi) | m        |
|-----|-----|-----------|-----------|----------|
|  20 |  20 |       180 |       180 | 1, 8, or |
|  20 |  20 |       180 |       360 | 1, 8, or |
|  10 |  10 |       360 |       360 | 1, 8, or |

|   Stylus COLOR only |   Stylus COLOR only |   Stylus COLOR only |   Stylus COLOR only | Stylus COLOR only      |
|---------------------|---------------------|---------------------|---------------------|------------------------|
|                   5 |                   5 |                 720 |                 720 | 1 (with speical paper) |

## Function

- Prints dot graphics in raster format (row by row, left to right)
- Allows compression of graphics data during raster graphics printing; counters can be included with data to specify the number of times to repeat a particular byte of data
- Parameters are used as described below:

c = 0 Full graphics mode (noncompressed)

1 Compressed raster graphics (Run Length Encoding) mode

v

Vertical resolution in dpi-720, 360, 180 (3600/v dpi)

h

Horizontal resolution in dpi-720, 360, 180 (3600/h dpi)

m

Vertical dot count (rows of dot graphics)

nL, nH formula:

Horizontal dot count (columns of dot graphics), according to the following

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->
