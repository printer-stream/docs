## C O N F I D E N T I A L

## TM-T20

## The bit image modes selectable by m are as follows: is

## When both standard mode and page mode are selected (a starting position specified by ESC T upper left or lower right).

|    |                       | Vertical    | Horizontal   | Horizontal        | Horizontal             | Horizontal                                  | Horizontal             | Horizontal                                   |
|----|-----------------------|-------------|--------------|-------------------|------------------------|---------------------------------------------|------------------------|----------------------------------------------|
|    |                       | Dot density | Dot density  |                   | Maximum number of dots | Maximum number of dots                      | Maximum number of dots | Maximum number of dots                       |
| m  | Bit Image Mode        |             |              | Set adjacent dots | Paper width 80mm       | Paperwidth 80 mmand 42 column mode selected | Paper width 58mm       | Paper width 58 mmand 42 column mode selected |
| 0  | 8-dot single-density  | 203/3 dpi   | 203/2 dpi    | Permitted         | 288                    | 273                                         | 210                    | 189                                          |
| 1  | 8-dot double-density  | 203/3 dpi   | 203 dpi      | Permitted         | 576                    | 546                                         | 420                    | 378                                          |
| 32 | 24-dot single-density | 203 dpi     | 203/2 dpi    | Permitted         | 288                    | 273                                         | 210                    | 189                                          |
| 33 | 24-dot double-density | 203 dpi     | 203 dpi      | Permitted         | 576                    | 546                                         | 420                    | 378                                          |

When the starting position specified by ESC T is upper right or lower left in page mode.

|    |                       | Vertical    | Vertical          | Vertical               | Horizontal   |
|----|-----------------------|-------------|-------------------|------------------------|--------------|
| m  | Bit Image Mode        | Dot density | Set adjacent dots | Maximum number of dots | Dot density  |
| 0  | 8-dot single-density  | 203/2 dpi   | Permitted         | 831                    | 203/3 dpi    |
| 1  | 8-dot double-density  | 203 dpi     | Permitted         | 1662                   | 203/3 dpi    |
| 32 | 24-dot single-density | 203/2 dpi   | Permitted         | 831                    | 203 dpi      |
| 33 | 24-dot double-density | 203 dpi     | Permitted         | 1662                   | 203 dpi      |

90 ° or 270 ° rotated bit-image data will be printed. dpi: dots per 25.4 mm (dots per inch)
