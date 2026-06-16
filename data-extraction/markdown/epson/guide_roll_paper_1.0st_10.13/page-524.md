## C O N F I D E N T I A L

| Bit   | Binary   | Hex   | Decimal   | Function   |
|-------|----------|-------|-----------|------------|
| 4, 5  | -        | -     | -         | Reserved   |
| 6     | 1        | 40    | 64        | Fixed      |
| 7     | 0        | 00    | 0         | Fixed      |

## &lt;2nd byte of DIP switch information&gt;

<!-- image -->

| Bit   | Binary   | Hex   | Decimal   | Function         |
|-------|----------|-------|-----------|------------------|
| 0     | 0        | 00    | 0         | DIP switch 5 OFF |
| 0     | 1        | 01    | 1         | DIP switch 5 ON  |
| 1     | 0        | 00    | 0         | DIP switch 6 OFF |
| 1     | 1        | 02    | 2         | DIP switch 6 ON  |
| 2     | 0        | 00    | 0         | DIP switch 7 OFF |
| 2     | 1        | 04    | 4         | DIP switch 7 ON  |
| 3     | 0        | 00    | 0         | DIP switch 8 OFF |
| 3     | 1        | 08    | 8         | DIP switch 8 ON  |
| 4, 5  | -        | -     | -         | Reserved         |
| 6     | 1        | 40    | 64        | Fixed            |
| 7     | 0        | 00    | 0         | Fixed            |

## TM-T20

- Column emulation mode (n = 35)

| Transmission data     | Hex                  | Decimal              | Data amount   |
|-----------------------|----------------------|----------------------|---------------|
| Header                | 3DH                  | 61                   | 1 byte        |
| Identifier            | 23H                  | 35                   | 1 byte        |
| Printer information A | See the table below. | See the table below. | 0 to 80 bytes |
| NUL                   | 00H                  | 0                    | 1 byte        |
