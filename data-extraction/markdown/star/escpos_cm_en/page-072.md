<!-- image -->

Name

Select paper out sensor to enable at printing stop

Code

ASCII ESC c 4 n

Hex. 1B 63 34

n

Decimal 27 99 52

n

Defined Region

0 ≤ n ≤ 255

Initial Value

n = 0

Function

Selects the paper out detector to stop printing when paper has run out.

|   Bit | Function                     | '0'     | '1'   |
|-------|------------------------------|---------|-------|
|     7 | Undefined                    | --      | --    |
|     6 | Undefined                    | --      | --    |
|     5 | Undefined                    | --      | --    |
|     4 | Undefined                    | --      | --    |
|     3 | Undefined                    | --      | --    |
|     2 | Undefined                    | --      | --    |
|     1 | Paper roll near end detector | Invalid | Valid |
|     0 | Paper roll near end detector | Invalid | Valid |

## Details

- To stop printing, the printer stops after printing the current line and feeding paper.
- The printer goes offline when printing is stopped.
- If either bit 0 or bit 1 is set to 1, select the paper roll near end detector as the paper out detector effective to stop printing.
