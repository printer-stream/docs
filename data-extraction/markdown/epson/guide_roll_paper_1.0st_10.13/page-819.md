## C O N F I D E N T I A L

| Vertical layout ( sb )   | 2DH, 30H - 39H   | 45,48 - 57   | 0 - 5 bytes   |
|--------------------------|------------------|--------------|---------------|
| Separator                | 1FH              | 31           | 1 byte        |
| Vertical layout ( sc )   | 2DH, 30H - 39H   | 45,48 - 57   | 0 - 5 bytes   |
| Separator                | 1FH              | 31           | 1 byte        |
| Vertical layout ( sd )   | 30H - 39H        | 48 - 57      | 0 - 5 bytes   |
| Separator                | 1FH              | 31           | 1 byte        |
| Vertical layout ( se )   | 2DH, 30H - 39H   | 45,48 - 57   | 0 - 5 bytes   |
| Separator                | 1FH              | 31           | 1 byte        |
| Horizontal layout ( sf ) | 30H - 39H        | 48 - 57      | 0 - 5 bytes   |
| NUL                      | 00H              | 0            | 1 byte        |

Example:  When ( n = 64) is the setting value for [Information type], the data is the 2 bytes '64' [Hexadecimal = 36H, 34H / Decimal = 54, 52].

When ( n = 80) is the effective value for [Information type], the data is the 2 bytes '80' [Hexadecimal = 36H, 30H / Decimal = 56, 48].

- (*2) ( sm - sf ) of [Layout information] corresponds to ( sm - sf ) of &lt;Function 33&gt; of this command. Each item of information expressed as decimals is converted to text data and the high-order values are transmitted first.

Example:  When [Vertical layout ( sb ) is 15, the data is the 2 bytes '15' [Hexadecimal = 31H, 35H / Decimal = 49,53].

- ■ The transmission data when a setting value ( n = 64) is specified for information type is as follows.
- The setting value indicates the paper layout information (the setting value of &lt;Function 33&gt; of this command) saved in memory.
- When the first item of data of each layout information is '-' [Hexadecimal = 2DH / Decimal = 45], it indicates a negative number.
