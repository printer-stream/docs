## C O N F I D E N T I A L

- a) Turn off the power after feeding paper to the print starting position.
- b) Do not open the roll paper cover or replace roll paper when power is off.
- c) If the roll paper cover is opened while power is off, open the cover to feed paper to the print start position after the power is turned on.
- d) If the print starting position is not set when power is turned on, the print position of the first sheet may shift, or a paper layout error may occur.

## TM-P60

## · Peeler models:

When a = 8, memory switch 8 is set as follows:

| Msw       |   Setting value ( b ) | Function                                                                                         |
|-----------|-----------------------|--------------------------------------------------------------------------------------------------|
| 8-1       |                    48 | Power ON/Power OFF notification transmission and battery status is not transmitted automatically |
| 8-1       |                    49 | Power ON/Power OFF notification transmission and battery status is transmitted automatically     |
| 8-2       |                    48 | No beeps for low battery                                                                         |
| 8-2       |                    49 | Beeps for low battery                                                                            |
| 8-3       |                    48 | No beeps for host disconnection                                                                  |
| 8-3       |                    49 | Beeps for host disconnection                                                                     |
| 8-4       |                    48 | No beeps for roll paper end                                                                      |
| 8-4       |                    49 | Beeps for roll paper end                                                                         |
| 8-5       |                    48 | No beeps for recoverable and non-recoverable error occurred                                      |
| 8-5       |                    49 | Beeps for recoverable and non-recoverable error occurred                                         |
| 8-6       |                    48 | "Print starting position" is not the paper position immediately after a specific status          |
| 8-6       |                    49 | "Print starting position" is the paper position immediately after a specific status              |
| 8-7 ~ 8-8 |                    50 | Reserved                                                                                         |

Setting of [Msw8-1] affects the operation of DLE DC4 ( fn =2) but not affect the operation of DLE DC4 ( fn =7).
