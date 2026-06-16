## C O N F I D E N T I A L

Settings of [Msw8-2] ~ [Msw8-5] do not affect the operation of function 48 of ESC (A .

[Msw8-6]: "Specific status" indicates when the peeler cover is closed, when the power is turned on, and when the printer is reset.

TM-P60 models without Peeler

## · When a = 8, memory switch 8 is set as follows:

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
| 8-4       |                    48 | No beeps for recoverable and non-recoverable error                                               |
| 8-4       |                    49 | Beeps for recoverable and non-recoverable error                                                  |
| 8-5 ~ 8-6 |                    50 | Reserved                                                                                         |

Setting of [Msw8-1] affects the operation of DLE DC4 ( fn =2) but not not affect the operation of DLE DC4 ( fn =7).

Settings of [Msw8-2] ~ [Msw8-5] do not affect the operation of function 48 of ESC (A .

## TM-U220

'Auto cutter is provided or not' [Msw 2-3] is not supported.
