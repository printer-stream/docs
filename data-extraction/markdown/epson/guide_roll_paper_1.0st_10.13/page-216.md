## C O N F I D E N T I A L

When both standard mode and page mode are selected (a starting position specified by ESC T is upper left or lower right).

|    |                       |                      | Horizontal   | Horizontal        | Horizontal                                     | Horizontal             |
|----|-----------------------|----------------------|--------------|-------------------|------------------------------------------------|------------------------|
|    |                       |                      |              |                   | Maximum number of dots                         | Maximum number of dots |
| m  | Bit Image Mode        | Vertical dot density | Dot density  | Set adjacent dots | Paper layout is not used / Top of a black mark | Bottom of a label      |
| 0  | 8-dot single-density  | 203/3 dpi            | 203/2 dpi    | Permitted         | 128 to 288                                     | 112 to 280             |
| 1  | 8-dot double-density  | 203/3 dpi            | 203 dpi      | Permitted         | 256 to 576                                     | 224 to 560             |
| 32 | 24-dot single-density | 203 dpi              | 203/2 dpi    | Permitted         | 128 to 288                                     | 112 to 280             |
| 33 | 24-dot double-density | 203 dpi              | 203 dpi      | Permitted         | 256 to 576                                     | 224 to 560             |

## A horizontal maximum print area is decided according to the width of the paper. When paper layout is not used or top of black mark is selected.

| Paper width   | Single density mode ( m = 0, 32)        | Double density mode ( m = 1, 33)    |
|---------------|-----------------------------------------|-------------------------------------|
| 80 mmto 78mm  | 288 dots                                | 576 dots                            |
| 77 mmto 38mm  | (256 + (paper width - 38) × 8 / 2) dots | (256 + (paper width - 38) × 8) dots |

## When paper layout is selected as the bottom of label.

| Paper width   | Single density mode ( m = 0, 32)        | Double density mode ( m = 1,33)     |
|---------------|-----------------------------------------|-------------------------------------|
| 80mm          | 280 dots                                | 560 dots                            |
| 79 mmto 38mm  | (224 + (paper width - 38) × 8 / 2) dots | (224 + (paper width - 38) × 8) dots |
