The band height affects the following:

- The taller the band height, the more memory you must prepare in your program to accomodate graphics data.
- The band height determines the number of times you must send the ESC . command. You must resend the ESC . command for each band of graphics you print. The taller the band height, the less number of ESC . commands you need to send.

The following table gives you an idea of how much memory is required for band heights at certain standard widths.

| Band width   | Bytes required for band heights at 180-dpi horizontal dot density   | Bytes required for band heights at 180-dpi horizontal dot density   | Bytes required for band heights at 180-dpi horizontal dot density   | Bytes required for band heights 360-dpi horizontal dot density   | Bytes required for band heights 360-dpi horizontal dot density   | at                 |
|--------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|--------------------|
|              | 1-dot band height                                                   | 8-dot band height                                                   | 24-dot band height                                                  | 1-dot band height                                                | 8-dot band height                                                | 24-dot band height |
| 8 inches     | 180                                                                 | 1,440                                                               | 4,320                                                               | 360                                                              | 2,880                                                            | 8,640              |
| 11 inches    | 248                                                                 | 1,984                                                               | 5,952                                                               | 495                                                              | 3,960                                                            | 11,880             |
| 14 inches    | 315                                                                 | 2,520                                                               | 7,560                                                               | 630                                                              | 5,040                                                            | 15,120             |

Use the ESC + command to set line spacing to match the band height. The following table shows the command format for each band height.

| ESC + command setting   |   Vertical dot density (dpi) |   Band height (dots) | Band height (inches)   |   Parameter m in ESC . command |
|-------------------------|------------------------------|----------------------|------------------------|--------------------------------|
| ESC + 1                 |                          360 |                    1 | 1/360                  |                              1 |
| ESC + 2                 |                          180 |                    1 | 2/360                  |                              1 |
| ESC + 8                 |                          360 |                    8 | 8/360                  |                              8 |
| ESC + 16                |                          180 |                    8 | 16/360                 |                              8 |
| ESC + 24                |                          360 |                   24 | 24/360                 |                             24 |
| ESC + 48                |                          180 |                   24 | 48/360                 |                             24 |
