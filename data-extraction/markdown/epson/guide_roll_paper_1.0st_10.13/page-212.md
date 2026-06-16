## C O N F I D E N T I A L

## TM-T88IV

The bit image modes selectable by m are as follows:

When both standard mode and page mode are selected (a starting position specified by ESC T is upper left or lower right).

|                  |                       |                      | Horizontal   | Horizontal        | Horizontal           | Horizontal           |
|------------------|-----------------------|----------------------|--------------|-------------------|----------------------|----------------------|
|                  |                       |                      |              |                   | Maximumnumberof dots | Maximumnumberof dots |
| m Bit Image Mode | m Bit Image Mode      | Vertical dot density | Dot density  | Set adjacent dots | Paperwidth 80mm      | Paper width 58mm     |
| 0                | 8-dot single-density  | 60 dpi               | 90 dpi       | Permitted         | 256                  | 180                  |
| 1                | 8-dot double-density  | 60 dpi               | 180 dpi      | Permitted         | 512                  | 360                  |
| 32               | 24-dot single-density | 180 dpi              | 90 dpi       | Permitted         | 256                  | 180                  |
| 33               | 24-dot double-density | 180 dpi              | 180 dpi      | Permitted         | 512                  | 360                  |

When the starting position specified by ESC T is upper right or lower left in page mode.

|    |                       | Vertical    | Vertical          | Vertical                       | Vertical                   |                        |
|----|-----------------------|-------------|-------------------|--------------------------------|----------------------------|------------------------|
|    |                       |             |                   | Maximum number of dots         | Maximum number of dots     |                        |
| m  | Bit Image Mode        | Dot density | Set adjacent dots | Single- color printing control | Two-color printing control | Horizontal dot density |
| 0  | 8-dot single-density  | 90 dpi      | Permitted         | 831                            | 415                        | 60 dpi                 |
| 1  | 8-dot double-density  | 180 dpi     | Permitted         | 1662                           | 831                        | 60 dpi                 |
| 32 | 24-dot single-density | 90 dpi      | Permitted         | 831                            | 415                        | 180 dpi                |
| 33 | 24-dot double-density | 180 dpi     | Permitted         | 1662                           | 831                        | 180 dpi                |

90 ° or 270 ° rotated bit-image data will be printed.

dpi: dots per 25.4 mm (dots per inch)
