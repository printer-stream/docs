## C O N F I D E N T I A L

## ■ (*1) Status A is shown in the table below:

|   Bit | Function                                | Binary   | Hexadecimal   | Decimal   |
|-------|-----------------------------------------|----------|---------------|-----------|
|     0 | Ink end not detected (1st color)        | 0        | 00            | 0         |
|     0 | Ink end detected (1st color)            | 1        | 01            | 1         |
|     1 | Ink end not detected (1st color)        | 0        | 00            | 0         |
|     1 | Ink end detected (1st color)            | 1        | 02            | 2         |
|     2 | Ink cartridge installed (1st color)     | 0        | 00            | 0         |
|     2 | Ink cartridge not installed (1st color) | 0        | 04            | 4         |
|     3 | Ink cartridge installed (2nd color)     | 0        | 00            | 0         |
|     3 | Ink cartridge not installed (2nd color) | 1        | 08            | 8         |
|     4 | Reserved                                | -        | -             | -         |
|     5 | Cleaning is not being performed         | 0        | 00            | 0         |
|     5 | Cleaning is being performed             | 1        | 20            | 32        |
|     6 | Fixed                                   | 1        | 40            | 64        |
|     7 | Fixed                                   | 0        | 00            | 0         |

## ■ (*2) Status B is shown in the table below:

| Bit   | Function                              | Binary   | Hexadecimal   | Decimal   |
|-------|---------------------------------------|----------|---------------|-----------|
| 0     | Ink near-end not detected (2nd color) | 0        | 00            | 0         |
| 0     | Ink near-end detected (2nd color)     | 1        | 01            | 1         |
| 1     | Ink end not detected (2nd color)      | 0        | 00            | 0         |
| 1     | Ink end detected (2nd color)          | 1        | 02            | 2         |
| 2 ~ 5 | Reserved                              | -        | -             | -         |
| 6     | Fixed                                 | 1        | 40            | 64        |
| 7     | Fixed                                 | 0        | 00            | 0         |
