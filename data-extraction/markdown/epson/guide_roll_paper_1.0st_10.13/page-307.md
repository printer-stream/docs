## C O N F I D E N T I A L

## [Printers not featuring this command] TM-P60 , TM-U230 , TM-U220

[Description]

Prints a raster bit image using the mode specified by m , as follows:

| m     | Mode          | Scaling for horizontal   | Scaling for vertical   |
|-------|---------------|--------------------------|------------------------|
| 0, 48 | Normal        | × 1                      | × 1                    |
| 1, 49 | Double-width  | × 2                      | × 1                    |
| 2, 50 | Double-height | × 1                      | × 2                    |
| 3, 51 | Quadruple     | × 2                      | × 2                    |

- xL , xH specifies ( xL + xH × 256) bytes in horizontal direction for the bit image.
- yL , yH specifies ( yL + yH × 256) dots in vertical direction for the bit image.
- d specifies the bit image data (raster format).
- k indicates the number of bit image data. k is an explanation parameter; therefore, it does not need to be transmitted.

## [Recommended Functions]

This command is supported by only some of the printer models and will not be supported by future models.

It is recommended to use graphics function ( GS ( L GS 8 L : &lt;Function 50&gt; and &lt;Function 112&gt; ). The graphics function is superior in operating to GS v 0 for the following reasons:

- Selecting a color for printing is possible.
- Size setting in dot unit is possible.
- ■ When standard mode is selected, this command is enabled only when there is no data in the print buffer and printer is in the beginning of the line. If data exists in the print buffer, the printer processes m and the following data as normal data.
- ■ In page mode, the bit image is only stored in the print buffer and is not printed.
- ■ Data ( d ) specifies a bit printed to 1 and not printed to 0.
- ■ If a raster bit image exceeds one line, the excess data is not printed.

## [Notes]
