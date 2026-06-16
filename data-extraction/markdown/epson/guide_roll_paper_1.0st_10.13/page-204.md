## C O N F I D E N T I A L

[Description]

## [Notes]

Stores the bit image data in the print buffer using the mode specified by bit image mode m as follows:

|   m | Bit image Mode        |   Number of bits for vertical data | Dot density in horizontal   |
|-----|-----------------------|------------------------------------|-----------------------------|
|   0 | 8-dot single-density  |                                  8 | Single-density              |
|   1 | 8-dot double-density  |                                  8 | Double-density              |
|  32 | 24-dot single-density |                                 24 | Single-density              |
|  33 | 24-dot double-density |                                 24 | Double-density              |

- nL , nH specifies a bit image in the horizontal direction as ( nL + nH × 256) dots.
- d specifies the bit image data (column format).
- k indicates the amount of bit image data. k is an explanation parameter; therefore it does not need to be transmitted.
- ■ Data ( d ) specifies a bit printed to 1 and not printed to 0.
- ■ If the bit image data exceeds the number of dots to be printed on a line, the excess data is ignored.
- ■ The bit-image is not affected by print mode (emphasized, double-strike, underline, character size, white/ black reverse printing, or 90° clockwise-rotated), except for upside-down print mode.
- ■ After printing a bit image, the printer processes normal data.
- ■ When printing multiple line bit images, selecting unidirectional print mode with ESC U enables printing patterns in which the top and bottom parts are aligned vertically.
- ■ This command is used to print a picture or logo.
- ■ The relationship between the bit image data and the print result is as follows.
