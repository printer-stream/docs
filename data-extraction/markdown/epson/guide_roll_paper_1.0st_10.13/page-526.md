## C O N F I D E N T I A L

Bits 2, 3, 5, and 6 are not supported.

Bit 1: Autocutter installed

- Printer model ( n = 67)
- Model dependent printer information ( n = 111):

Printer model: TM-T88V

Sends 4 byte data group composed of [header + printer information (2 bytes) + NUL].

## &lt;1st byte of DIP switch information&gt;

| Bit   | Binary   | Hex   | Decimal   | Function           |
|-------|----------|-------|-----------|--------------------|
| 0     | 0        | 00    | 0         | DIP switch 1-1 OFF |
| 0     | 1        | 01    | 1         | DIP switch 1-1 ON  |
| 1     | 0        | 00    | 0         | DIP switch 1-2 OFF |
| 1     | 1        | 02    | 2         | DIP switch 1-2 ON  |
| 2     | 0        | 00    | 0         | DIP switch 1-3 OFF |
| 2     | 1        | 04    | 4         | DIP switch 1-3 ON  |
| 3     | 0        | 00    | 0         | DIP switch 1-4 OFF |
| 3     | 1        | 08    | 8         | DIP switch 1-4 ON  |
| 4, 5  | -        | -     | -         | Reserved           |
| 6     | 1        | 40    | 64        | Fixed              |
| 7     | 0        | 00    | 0         | Fixed              |

## &lt;2nd byte of DIP switch information&gt;

|   Bit |   Binary |   Hex |   Decimal | Function           |
|-------|----------|-------|-----------|--------------------|
|     0 |        0 |    00 |         0 | DIP switch 1-5 OFF |
|       |        1 |    01 |         1 | DIP switch 1-5 ON  |
