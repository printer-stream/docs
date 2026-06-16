<!-- image -->

Rev. 2.31

## &lt; Printer Status 7 presenter paper position (9th byte) &gt;

|   Bit |                         | Condition   | Condition   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   |
|-------|-------------------------|-------------|-------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|       |                         | '0'         | '1'         | U        | PU       | IIU      | GT       | LAN      | IIIW     | IIILAN   | IIIBI    | IIIU     |
|     7 | Fixed at '0'            |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     6 | Not used (Fixed at '0') |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     5 | Not used (Fixed at '0') |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     4 | Fixed at '0'            |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     3 | -                       |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     2 | -                       |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     1 | -                       |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     0 | Fixed at '0'            |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |

## Status identification method

| COMMAND FUNCTION LIST           | Status   | Status   | Status   | Status   | Status   | Status   | Status   | Status   |
|---------------------------------|----------|----------|----------|----------|----------|----------|----------|----------|
|                                 | bit7     | bit6     | bit5     | bit4     | bit3     | bit2     | bit1     | bit0     |
| Normal status (Header 1)        | 0        | *        | *        | 0        | *        | *        | *        | 1        |
| Normal status (except header 1) | 0        | *        | *        | 0        | *        | *        | *        | 0        |

0 = "0" represents fixed bit / 1 = "1" represents fixed bit / * = represents the changing bit

--------------------------------------------------------------------------------------
