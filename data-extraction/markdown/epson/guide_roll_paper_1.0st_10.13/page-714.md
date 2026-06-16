## C O N F I D E N T I A L

- b) Do not open the roll paper cover or replace roll paper when power is off.
- c) If the roll paper cover is opened while power is off, open the cover to feed paper to the print start position after the power is turned on.
- d) If the print starting position is not set when power is turned on, the print position of the first sheet may shift, or a paper layout error may occur.

## TM-L90 models without peeler:

Receive buffer capacity [Msw 1-2]: Large (when b = 48) = 4 KB; small (when b = 49) = 45 bytes

'DM-D (customer display) is connected or not' [Msw 1-6] function is not supported.

'Selecting character code system for the simplified Chinese model' [Msw 2-3] is not supported.

Setting the memory switch ([Msw 1-2] ~ [Msw 1-4], [Msw 1-7], [Msw 1-8], [Msw 2-2], [Msw 8-4]) can be changed by 'Memory switch setting mode' by the panel switch operation when the power supply is turned on.

## · When a = 8, memory switch 8 is set as follows:

| Msw   |   Setting value ( b ) | Function                                                                         |
|-------|-----------------------|----------------------------------------------------------------------------------|
| 8-1   |                    50 | Reserved                                                                         |
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
