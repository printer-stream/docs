## C O N F I D E N T I A L

|   Bit |   Binary |   Hex |   Decimal | Status for ASB                                            |
|-------|----------|-------|-----------|-----------------------------------------------------------|
|     2 |        0 |    00 |         0 | No recoverable error (except for autocutter error).       |
|     2 |        1 |    04 |         4 | Recoverable error occurred (except for autocutter error). |
|     3 |        0 |    00 |         0 | No autocutter error.                                      |
|     3 |        1 |    08 |         8 | Autocutter error occurred.                                |
|     4 |        0 |    00 |         0 | Not used. Fixed to Off.                                   |
|     5 |        0 |    00 |         0 | No unrecoverable error.                                   |
|     5 |        1 |    20 |        32 | Unrecoverable error occurred.                             |
|     6 |        0 |    00 |         0 | No automatically recoverable error.                       |
|     6 |        1 |    40 |        64 | Automatically recoverable error occurred.                 |
|     7 |        0 |    00 |         0 | Not used. Fixed to Off.                                   |

- Online recovery wait (bit 0) is changed when GS ^ or GS FF is executed, the printer waits for the button to be pressed for removing a label, or roll paper to be replaced for some models.
- If recoverable error (bit 2) or autocutter error (bit 3) occurs due to paper jams or the like, it is possible to recover by correcting the cause of the error and executing DLE ENQ ( n = 2).
- If an unrecoverable error (bit 5) occurs, turn off the power as soon as possible.
- The cause of the error can be checked by the offline response (when an offline cause is added). See Function 49 of GS ( H .
