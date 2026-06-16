## C O N F I D E N T I A L

## TM-J2000/J2100

Receive buffer capacity [Msw 1-2]: Large (when b = 48) = 4 KB; small (when b = 49) = 45 bytes .

This printer doesn't support [Msw 2-3] (Selecting character code system for the simplified Chinese model).

- When a = 8, memory switch 8 is set as follows:

| Msw        |   Setting value (b) | Function                                                           |
|------------|---------------------|--------------------------------------------------------------------|
| 8-1 to 8-7 |                  50 | Reserved                                                           |
| 8-8        |                  48 | Roll paper cover open during printing: automatic recoverable error |
| 8-8        |                  49 | Roll paper cover open during printing: recoverable error           |

Setting the memory switch ([Msw 1-2] ~ [Msw 1-5], [Msw 1-7], [Msw 1-8], [Msw 2-2]) can be changed by 'Memory switch setting mode' by the panel switch operation when the power supply is turned on.

## TM-T90

Receive buffer capacity [Msw 1-2]: Large (when b = 48) = 4 KB; small (when b = 49) = 45 bytes.

This printer doesn't support [Msw 1-6] (DM-D (Customer display) is connected or not)) and [Msw 23] (Selecting character code system for the simplified Chinese model).

- When a = 8, memory switch 8 is set as follows:

&lt;Other than Japanese model&gt;

| Msw      |   Setting value ( b ) | Function                                            |
|----------|-----------------------|-----------------------------------------------------|
| 8-1, 8-2 |                    50 | Reserved                                            |
| 8-3      |                    48 | PAPER LED is on when a paper near end is detected   |
| 8-3      |                    49 | PAPER LED is off when a paper near end is detected  |
| 8-4      |                    50 | Reserved                                            |
| 8-5      |                    48 | Spacing of both sides for bar code: not inserted    |
| 8-5      |                    49 | Spacing of both sides for bar code: inserts a space |
| 8-6      |                    50 | Reserved                                            |
