<!-- image -->

## 3) Status identification method

| Command/Functions           | Status   | Status   | Status   | Status   | Status   | Status   | Status   | Status   |
|-----------------------------|----------|----------|----------|----------|----------|----------|----------|----------|
|                             | bit7     | bit6     | bit5     | bit4     | bit3     | bit2     | bit1     | bit0     |
| XON                         | 0        | 0        | 0        | 1        | 0        | 0        | 0        | 1        |
| XOFF                        | 0        | 0        | 0        | 1        | 0        | 0        | 1        | 1        |
| ENQ                         | *        | *        | *        | 0        | *        | *        | *        | *        |
| EOT                         | *        | *        | *        | 1        | *        | *        | *        | 0        |
| ASB (Header - 1)            | 0        | *        | *        | 0        | *        | *        | *        | 1        |
| ASB (Other than Header - 1) | 0        | *        | *        | 0        | *        | *        | *        | 0        |

Indicates '0' bit is fixed at 0/Indicates 1 is fixed at 1/Indicates * variable bit.

-----------------------------------------------------------------------------
