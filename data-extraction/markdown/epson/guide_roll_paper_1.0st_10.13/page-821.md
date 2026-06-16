## C O N F I D E N T I A L

## FS ( L &lt;Function 48 &gt;

[Name]

Transmit the positioning information

[Format]

[Range]

[Description] [Notes]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Transmits the positioning information for the label or black mark paper.

- ■ Header to NUL shown in the following is transmitted in this function.

| Transmission data      | Hex        | Decimal   | Number of data   |
|------------------------|------------|-----------|------------------|
| Header                 | 37H        | 55        | 1 byte           |
| Identifier             | 38H        | 56        | 1 byte           |
| Position information A | 40H to 7FH | 64 to 127 | 1 byte           |
| Position information B | 40H to 7FH | 64 to 127 | 1 byte           |
| NUL                    | 00H        | 0         | 1 byte           |
