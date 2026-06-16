<!-- image -->

Name

Select peripheral device

Code

ASCII

ESC = n

Hex.

1B 3D n

Decimal

27 61 n

Defined Region

0 ≤ n ≤ 255

Initial Value

n = 1

Function

Selects the peripheral device for which the data is effective from the host computer.

|   Bit | Function   | '0'     | '1'   |
|-------|------------|---------|-------|
|     7 | Undefined  |         |       |
|     6 | Undefined  |         |       |
|     5 | Undefined  |         |       |
|     4 | Undefined  |         |       |
|     3 | Undefined  |         |       |
|     2 | Undefined  |         |       |
|     1 | Undefined  |         |       |
|     0 | Printer    | Invalid | Valid |

Details

- If the printer is selected to be invalid, the printer discards all data from the next data until the printer is made valid again by this command.  (This excludes DLEEOT, DLEENQ, DLEDC4.)

STAR

- Even when the printer is not invalid, the printer specification of this command (n = 1) is processed.
