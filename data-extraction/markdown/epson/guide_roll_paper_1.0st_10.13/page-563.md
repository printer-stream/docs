## C O N F I D E N T I A L

## FS !

[Name]

Select print mode(s) for Kanji characters

[Format]

ASCII

FS ! n

Hex 1C 21 n

Decimal 28 33 n

[Printers not featuring this command] None

[Range]

0 ≤ n ≤ 255

[Default]

n = 0

[Description]

Selects the character styles (double-height, double-width, and Kanji-underlined) together for multi-byte code character as follows:

| n: Bit   | Function                           | Binary   |   Hexadecimal |   Decimal |
|----------|------------------------------------|----------|---------------|-----------|
| 0        | Reserved                           | Off      |            00 |         0 |
| 1        | Reserved                           | Off      |            00 |         0 |
| 2        | Double-width canceled              | 0ff      |            00 |         0 |
| 2        | Double-width selected              | On       |            04 |         4 |
| 3        | Double-height canceled             | Off      |            00 |         0 |
| 3        | Double-height selected             | On       |            08 |         8 |
| 4~6      | Reserved                           | Off      |            00 |         0 |
| 7        | Kanji underline mode is turned off | Off      |            00 |         0 |
| 7        | Kanji underline mode is turned on  | On       |            80 |       128 |

SETTING COMMAND
