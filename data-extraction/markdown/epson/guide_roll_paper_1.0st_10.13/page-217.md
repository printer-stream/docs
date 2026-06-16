## C O N F I D E N T I A L

<!-- image -->

| When the starting position specified by ESC T is upper right or lower left in page mode.   | When the starting position specified by ESC T is upper right or lower left in page mode.   | When the starting position specified by ESC T is upper right or lower left in page mode.   | When the starting position specified by ESC T is upper right or lower left in page mode.   | When the starting position specified by ESC T is upper right or lower left in page mode.   | When the starting position specified by ESC T is upper right or lower left in page mode.   |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
|                                                                                            |                                                                                            | Vertical                                                                                   | Vertical                                                                                   | Vertical                                                                                   |                                                                                            |
| m                                                                                          | Bit Image Mode                                                                             | Dot density                                                                                | Set adjacent dots                                                                          | Maximum number of dots                                                                     | Horizontal dot density                                                                     |
| 0                                                                                          | 8-dot single-density                                                                       | 203/2 dpi                                                                                  | Permitted                                                                                  | 738                                                                                        | 203/3 dpi                                                                                  |
| 1                                                                                          | 8-dot double-density                                                                       | 203 dpi                                                                                    | Permitted                                                                                  | 1476                                                                                       | 203/3 dpi                                                                                  |
| 32                                                                                         | 24-dot single-density                                                                      | 203/2 dpi                                                                                  | Permitted                                                                                  | 738                                                                                        | 203 dpi                                                                                    |
| 33                                                                                         | 24-dot double-density                                                                      | 203 dpi                                                                                    | Permitted                                                                                  | 1476                                                                                       | 203 dpi                                                                                    |

90 ° or 270 ° rotated bit-image data will be printed.

## TM-U230

The bit image modes selectable by m are as follows:

'Vertical' is in the direction of paper feeding and 'horizontal' is perpendicular (at right angles) to the direction of paper feeding.

|    |                      |                      | Horizontal   | Horizontal        | Horizontal             |
|----|----------------------|----------------------|--------------|-------------------|------------------------|
| m  | Bit Image Mode       | Vertical dot density | Dot density  | Set adjacent dots | Maximum number of dots |
| 0  | 8-dot single-density | 72 dpi               | 80 dpi       | Permitted         | 200                    |
| 1  | 8-dot double-density | 72 dpi               | 160 dpi      | Prohibited        | 400                    |

dpi: dots per 25.4 mm (dots per inch)
