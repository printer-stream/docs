## C O N F I D E N T I A L

When both standard mode and page mode are selected (a starting position specified by ESC T is upper left or lower right).

|    |                       |             | Horizontal   | Horizontal   | Horizontal             | Horizontal             | Horizontal             | Horizontal             |
|----|-----------------------|-------------|--------------|--------------|------------------------|------------------------|------------------------|------------------------|
|    |                       | Vertical    | Dot density  | Set adjacent | Maximum number of dots | Maximum number of dots | Maximum number of dots | Maximum number of dots |
| m  | Bit Image Mode        | dot density |              | dots         | Paper width 82.5mm     | Paper width 76mm       | Paper width 69.5mm     | Paper width 57.5mm     |
| 0  | 8-dot single-density  | 60 dpi      | 90 dpi       | Permitted    | 256                    | 240                    | 216                    | 180                    |
| 1  | 8-dot double-density  | 60 dpi      | 180 dpi      | Permitted    | 512                    | 480                    | 432                    | 360                    |
| 32 | 24-dot single-density | 180 dpi     | 90 dpi       | Permitted    | 256                    | 240                    | 216                    | 180                    |
| 33 | 24-dot double-density | 180 dpi     | 180 dpi      | Permitted    | 512                    | 480                    | 432                    | 360                    |

## When the starting position specified by ESC T is upper right or lower left in page mode.

|    |                       | Vertical    | Vertical      | Vertical               | Vertical               | Vertical               | Vertical               | Horizontal dot   |
|----|-----------------------|-------------|---------------|------------------------|------------------------|------------------------|------------------------|------------------|
|    |                       | Dot density | Set           | Maximum number of dots | Maximum number of dots | Maximum number of dots | Maximum number of dots |                  |
| m  | Bit Image Mode        |             | adjacent dots | Paper width 82.5mm     | Paper width 76mm       | Paper width 69.5mm     | Paper width 57.5mm     | density          |
| 0  | 8-dot single-density  | 90 dpi      | Permitted     | 416                    | 444                    | 492                    | 592                    | 60 dpi           |
| 1  | 8-dot double-density  | 180 dpi     | Permitted     | 832                    | 888                    | 984                    | 1184                   | 60 dpi           |
| 32 | 24-dot single-density | 90 dpi      | Permitted     | 416                    | 444                    | 492                    | 592                    | 180 dpi          |
| 33 | 24-dot double-density | 180 dpi     | Permitted     | 832                    | 888                    | 984                    | 1184                   | 180 dpi          |

90 ° or 270 ° rotated bit-image data will be printed.

dpi: dots per 25.4 mm (dots per inch)
