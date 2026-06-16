## C O N F I D E N T I A L

- The HRI characters of special characters (SP, "(," ")") are printed as the respective characters (SP, "(," ")").
- The HRI character of special character ("*") prints a check digit.
- The HRI characters of bar code data ["{"+("(," ")," "*," "{")] are printed as the respective characters ("(," ")," "*," "{")
- ■ The range of data (d) that can be processed in each code set (CODE A, CODE B, CODE C) is shown in the table below. Data where the character field is diagonal cannot be used. Transmit the 2-byte data shown in the following table ([Hexadecimal = 7BH / Decimal = 123] + character code) from the host for the special characters (FNC1, FNC3) and bar code data "(", ")", "*", and "{",.

<!-- image -->

| i   | Decimat_&#124;   | cove A   | &#124; Cove 8   | &#124; CODE Cc   |             |             |          |        |        |        |
|-----|------------------|----------|-----------------|------------------|-------------|-------------|----------|--------|--------|--------|
|     |                  |          |                 | a7               |             |             |          |        |        |        |
|     |                  |          |                 | 38               |             |             |          |        |        |        |
|     |                  |          |                 | 39               |             |             |          |        |        |        |
|     |                  |          |                 | 40               |             |             |          |        |        |        |
|     |                  |          |                 | 4                |             |             |          |        |        |        |
|     |                  |          |                 | 42               |             |             |          |        |        |        |
|     |                  |          |                 | 43               |             |             |          |        |        |        |
|     |                  |          |                 | “4               |             |             |          |        |        |        |
|     |                  |          |                 | 45               |             |             |          |        |        |        |
|     |                  |          |                 | 46               |             |             |          |        |        |        |
|     |                  |          |                 | 47               |             |             |          |        |        |        |
|     |                  |          |                 | 48               |             |             |          |        |        |        |
|     |                  |          |                 | 49               |             |             |          |        |        |        |
|     |                  |          |                 | 50               |             |             |          |        |        |        |
|     |                  |          |                 | 51               |             |             |          |        |        |        |
|     |                  |          |                 | $2               |             |             |          |        |        |        |
|     |                  |          |                 | 53               |             |             |          |        |        |        |
|     |                  |          |                 | 54               |             |             |          |        |        |        |
|     |                  |          |                 | 55               |             |             |          |        |        |        |
|     |                  |          |                 | 56               |             |             |          |        |        |        |
|     |                  |          |                 | ST               | Decimal Hex | &#124; Cove | A &#124; | Cove B | CODE C | CODE C |
|     |                  |          |                 | $8               | 78.31       |             |          |        |        |        |
|     |                  |          |                 | 59               |             |             |          |        |        |        |
|     |                  |          |                 | 60               |             |             |          |        |        |        |
|     |                  |          |                 | 61               |             |             |          |        |        |        |
|     |                  |          |                 | 62               |             | 41          |          |        |        |        |
|     |                  |          |                 | 63               |             | 42          |          |        |        |        |
|     |                  |          |                 | 64               |             |             |          |        |        |        |
|     |                  |          |                 | 65               |             |             |          |        |        |        |
|     |                  |          |                 | 66               |             |             |          |        |        |        |
|     |                  |          |                 | 67               |             |             |          |        |        |        |
|     |                  |          |                 | 68               |             |             |          |        |        |        |
|     |                  |          |                 | 69               |             |             |          |        |        |        |
|     |                  |          |                 | m1               |             |             |          |        |        |        |
|     |                  |          |                 | 72               |             |             |          |        |        |        |
|     |                  |          |                 | 73               |             |             |          |        |        |        |
