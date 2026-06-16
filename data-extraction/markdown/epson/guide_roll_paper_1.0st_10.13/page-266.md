## C O N F I D E N T I A L

See Function 49 of GS ( E for the origin of layout (paper layout is not used / top of black mark / bottom of label).

|         | Horizontal   | Horizontal                                                     | Horizontal                           | Vertical    | Vertical                 |
|---------|--------------|----------------------------------------------------------------|--------------------------------------|-------------|--------------------------|
| Scaling | Dot density  | Maximum print area (dot)(*1)                                   | Maximum print area (dot)(*1)         | Dot density |                          |
|         |              | When paper layout is not used or top of black mark is selected | When the bottom of label is selected |             | Maximum print area (dot) |
| × 1     | 203 dpi      | 256 to 576                                                     | 224 to 560                           | 203 dpi     | 738                      |
| × 2     | 203/2 dpi    | 128 to 288                                                     | 112 to 280                           | 203/2 dpi   | 369                      |

(*1) The maximum print area in the horizontal direction is defined by the paper width.

A horizontal maximum print area is decided according to the width of the paper.

|                                          | Paper width   | When ( x = 1) is specified.        | When ( x = 2) is specified.            |
|------------------------------------------|---------------|------------------------------------|----------------------------------------|
| When paper layout is not or top of black | 80 to 78mm    | 576 dot                            | 288 dot                                |
| used mark is selected                    | 77 to 38mm    | (256 + (paper width - 38) × 8) dot | (256 + (paper width - 38) × 8 / 2) dot |
| When the bottom of label is selected     | 80mm          | 560 dot                            | 280 dot                                |
| When the bottom of label is selected     | 79 to 38mm    | (224 + (paper width - 38) × 8) dot | (224 + (paper width - 38) × 8 / 2) dot |

## TM-P60

The dot density and the maximum print area are described in the next tables (dpi: number of dots per 25.4 mm).

'Vertical' is in the direction of paper feeding and 'horizontal' is perpendicular (at right angles) to the direction of paper feeding.

The maximum print area in the vertical direction is information used when graphics are printed with the page mode selected (for the starting position specified with ESC T is 'Upper right' or 'Lower left'). In this case, graphics rotated by 90 degrees or 270 degrees are printed.
