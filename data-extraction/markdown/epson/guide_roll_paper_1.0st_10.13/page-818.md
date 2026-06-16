## C O N F I D E N T I A L

## FS ( L pL pH fn n &lt;Function 34&gt;

[Name]

Paper layout information transmission

[Format]

[Range]

[Description]

[Notes]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

n = 64,80

Transmits paper layout information specified by n .

|   n | Paper layout information type             |
|-----|-------------------------------------------|
|  64 | Paper layout setting value (unit: 0.1 mm) |
|  80 | Paper layout effective value (unit: dots) |

- ■ With this function, the [Header - NUL] shown below is transmitted.

| Transmission data       | Hex       | Decimal   | Amount of data   |
|-------------------------|-----------|-----------|------------------|
| Header                  | 37H       | 55        | 1 byte           |
| Identifier              | 4BH       | 76        | 1 byte           |
| Information type (*1)   | 30H - 39H | 48 - 57   | 2 bytes          |
| Separator               | 1FH       | 31        | 1 byte           |
| Layout information (*2) |           |           |                  |
| Layout reference ( sm ) | 30H - 33H | 48 - 51   | 0 or 1 byte      |
| Separator               | 1FH       | 31        | 1 byte           |
| Vertical layout ( sa )  | 30H - 39H | 48 - 57   | 0 - 5 bytes      |
| Separator               | 1FH       | 31        | 1 byte           |
