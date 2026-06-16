## C O N F I D E N T I A L

- ■ Printer status ( n = 1) is as follows:

|   Bit |   Binary |   Hex |   Decimal | Status                                           |
|-------|----------|-------|-----------|--------------------------------------------------|
|     0 |        0 |    00 |         0 | Not used. Fixed to Off.                          |
|     1 |        1 |    02 |         2 | Not used. Fixed to On.                           |
|     2 |        0 |    00 |         0 | Drawer kick-out connector pin 3 is LOW.          |
|     2 |        1 |    04 |         4 | Drawer kick-out connector pin 3 is HIGH.         |
|     3 |        0 |    00 |         0 | Online.                                          |
|     3 |        1 |    08 |         8 | Offline.                                         |
|     4 |        1 |    10 |        16 | Not used. Fixed to On.                           |
|     5 |        0 |    00 |         0 | Not waiting for online recovery.                 |
|     5 |        1 |    20 |        32 | Waiting for online recovery.                     |
|     6 |        0 |    00 |         0 | Paper is not being fed by the paper feed button. |
|     6 |        1 |    04 |        64 | Paper is being fed by the paper feed button.     |
|     7 |        0 |    00 |         0 | Not used. Fixed to Off.                          |

## ... how to use this table

Online recovery wait (bit 5) is changed when GS ^ or GS FF is executed or the printer is waiting for the paper feed button to be pressed for removing a label or for roll paper to be replaced for some models.
