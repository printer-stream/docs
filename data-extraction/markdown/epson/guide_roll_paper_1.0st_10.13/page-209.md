## C O N F I D E N T I A L

## TM-T90

The bit image modes selectable by m are as follows:

'Vertical' is in the direction of paper feeding and 'horizontal' is perpendicular (at right angles) to the direction of paper feeding.

See Functions 5 and 6 of GS ( E to specify the paper width.

When both standard mode and page mode are selected (a starting position specified by ESC T is upper left or lower right).

[Other than Japanese model]

When the starting position specified by ESC T is lower right or upper left in page mode or standard mode

<!-- image -->

|    |                        |                      | Horizontal   | Horizontal        | Horizontal             | Horizontal             | Horizontal             |
|----|------------------------|----------------------|--------------|-------------------|------------------------|------------------------|------------------------|
|    |                        |                      |              |                   | Maximum number of dots | Maximum number of dots | Maximum number of dots |
| m  | Bit Image Mode         | Vertical dot density | Dot density  | Set adjacent dots | Paper width 80mm       | Paper width 60mm       | Paper width 58mm       |
| 0  | 8-dot single-density   | 60 dpi               | 90 dpi       | Permitted         | 256                    | 192                    | 180                    |
| 1  | 8-dot double-density   | 60 dpi               | 180 dpi      | Permitted         | 512                    | 384                    | 360                    |
| 32 | 24-dot single-density  | 180 dpi              | 90 dpi       | Permitted         | 256                    | 192                    | 180                    |
| 33 | 24-dot double- density | 180 dpi              | 180 dpi      | Permitted         | 512                    | 384                    | 360                    |

When the starting position specified by ESC T is upper right or lower left in page mode.

|    |                       | Vertical    | Vertical          | Vertical               |                        |
|----|-----------------------|-------------|-------------------|------------------------|------------------------|
| m  | Bit Image Mode        | Dot density | Set adjacent dots | Maximum number of dots | Horizontal dot density |
| 0  | 8-dot single-density  | 90 dpi      | Permitted         | 415                    | 60 dpi                 |
| 1  | 8-dot double-density  | 180 dpi     | Permitted         | 831                    | 60 dpi                 |
| 32 | 24-dot single-density | 90 dpi      | Permitted         | 415                    | 180 dpi                |
| 33 | 24-dot double-density | 180 dpi     | Permitted         | 831                    | 180 dpi                |
