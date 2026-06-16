## C O N F I D E N T I A L

## GS !

[Name]

Select character size

[Format]

ASCII

GS ! n

Hex

1D 21 n

Decimal 29 33

n

[Range]

0 ≤ n ≤ 7, 16 ≤ n ≤ 23, 32 ≤ n ≤ 39, 48 ≤ n ≤ 55,

64 ≤ n ≤ 71, 80 ≤ n ≤ 87, 96 ≤ n ≤ 103, 112 ≤ n ≤ 119

(1 ≤ height ≤ 8, 1 ≤ width ≤ 8)

[Default]

n = 0

[Printers not featuring this command] TM-U230 , TM-U220

[Description]

Selects the character height (vertical number of times normal font size) using bits 0 to 2 and selects the character width (horizontal number of times normal font size) using bits 4 to 6, as follows:

| Character width selection   | Character width selection   | Character width selection   | Character width selection   | Character width selection   | Character width selection   |
|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| Bit 6                       | Bit 5                       | Bit 4                       | Hex                         | Decimal                     | Width                       |
| Off                         | Off                         | Off                         | 00                          | 0                           | 1 (normal)                  |
| Off                         | Off                         | On                          | 10                          | 16                          | 2 (double- width)           |
| Off                         | On                          | Off                         | 20                          | 32                          | 3                           |
| Off                         | On                          | On                          | 30                          | 48                          | 4                           |
| On                          | Off                         | Off                         | 40                          | 64                          | 5                           |
| On                          | Off                         | On                          | 50                          | 80                          | 6                           |
| On                          | On                          | Off                         | 60                          | 96                          | 7                           |
| On                          | On                          | On                          | 70                          | 112                         | 8                           |

| Character height selection   | Character height selection   | Character height selection   | Character height selection   | Character height selection   | Character height selection   |
|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
| Bit 2                        | Bit 1                        | Bit 0                        | Hex                          | Decimal                      | Height                       |
| Off                          | Off                          | Off                          | 00                           | 0                            | 1 (normal)                   |
| Off                          | Off                          | On                           | 01                           | 1                            | 2 (double- height)           |
| Off                          | On                           | Off                          | 02                           | 2                            | 3                            |
| Off                          | On                           | On                           | 03                           | 3                            | 4                            |
| On                           | Off                          | Off                          | 04                           | 4                            | 5                            |
| On                           | Off                          | On                           | 05                           | 5                            | 6                            |
| On                           | On                           | Off                          | 06                           | 6                            | 7                            |
| On                           | On                           | On                           | 07                           | 7                            | 8                            |

SETTING COMMAND
