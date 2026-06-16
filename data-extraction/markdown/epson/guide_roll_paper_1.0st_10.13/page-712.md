## C O N F I D E N T I A L

## · When a = 7, memory switch 7 is set as follows:

[Msw 7-8]: Enabled in the continuous issuing mode.

| Msw        |   Setting value ( b ) | Function                                                                                                       |
|------------|-----------------------|----------------------------------------------------------------------------------------------------------------|
| 7-1 to 7-7 |                    50 | Reserved                                                                                                       |
| 7-8        |                    48 | Printer operation when the FEED button is pressed: Feeds paper to the next printing position on the next label |
|            |                    49 | Printer operation when the FEED button is pressed: Issues label                                                |

The process of label issuing is as follows:

Feeds paper to the label peeling position when the FEED button is pressed.

Feeds paper to the print starting position on the next label when the FEED button is pressed again.

## · When a = 8, memory switch 8 is set as follows:

| Msw   |   Setting value ( b ) | Function                                                                         |
|-------|-----------------------|----------------------------------------------------------------------------------|
| 8-1   |                    48 | Recovery from paper layout error: DLE ENQ execution or pressing the FEED button  |
| 8-1   |                    49 | Recovery from paper layout error: DLE ENQ execution                              |
| 8-2   |                    48 | Recovery from paper layout error: DLE ENQ execution or opening/closing the cover |
| 8-2   |                    49 | Recovery from paper layout error: DLE ENQ execution                              |
| 8-3   |                    48 | PAPER LED is on when a paper near end is detected                                |
| 8-3   |                    49 | PAPER LED is off when a paper near end is detected                               |
| 8-4   |                    48 | Sets the maximum length of automatic paper measurement to 160mm                  |
| 8-4   |                    49 | Sets the maximum length of automatic paper measurement to 300mm                  |
| 8-5   |                    48 | Spacing of both sides for bar code: not inserted                                 |
| 8-5   |                    49 | Spacing of both sides for bar code: inserts a space                              |
| 8-6   |                    48 | Perform paper feed to the print starting position when power is turned on        |
| 8-6   |                    49 | Not perform paper feed to the print starting position when power is turned on    |
