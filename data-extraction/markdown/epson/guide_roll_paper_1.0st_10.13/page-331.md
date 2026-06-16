## C O N F I D E N T I A L

- Error status ( n = 3) is as follows:

|   Bit |   Binary |   Hex |   Decimal | Status                           |
|-------|----------|-------|-----------|----------------------------------|
|     0 |        0 |    00 |         0 | Not used. Fixed to Off.          |
|     1 |        1 |    02 |         2 | Not used. Fixed to On.           |
|     2 |        0 |    00 |         0 | No recoverable error.            |
|     2 |        1 |    04 |         4 | Recoverable error occurred.      |
|     3 |        0 |    00 |         0 | No autocutter error.             |
|     3 |        1 |    08 |         8 | Autocutter error occurred.       |
|     4 |        1 |    10 |        16 | Not used. Fixed to On.           |
|     5 |        0 |    00 |         0 | No unrecoverable error.          |
|     5 |        1 |    20 |        32 | Unrecoverable error occurred.    |
|     6 |        0 |    00 |         0 | No auto-recoverable error.       |
|     6 |        1 |    40 |        64 | Auto-recoverable error occurred. |
|     7 |        0 |    00 |         0 | Not used. Fixed to Off.          |

## ... how to use this table

- If recoverable error (bit 2) or autocutter error (bit 3) occurs due to paper jams or the like, it is possible to recover by correcting the cause of the error and executing DLE ENQ ( n = 2).
- If an unrecoverable error (bit 5) occurs, turn off the power as soon as possible.
- The cause of the error can be checked by the offline response (when an offline cause is added). See Function 49 of GS ( H.
