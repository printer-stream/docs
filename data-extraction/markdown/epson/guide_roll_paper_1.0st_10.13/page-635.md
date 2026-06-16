## C O N F I D E N T I A L

## GS ( k &lt;Function 282&gt;

[Name]

MaxiCode: Transmit the size information of the symbol data in the symbol storage area

[Format]

[Range]

[Description]

[Notes]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

cn = 50

fn = 82

m = 48

Transmits the size information for the encoded MaxiCode symbol data in the symbol storage area using the process of &lt;Function 280&gt;.

- ■ In standard mode, use this function when the printer is 'at the beginning of a line,' or 'there is no data in the print buffer.'
- ■ The size information for each data is as follows;

| Send data             | Hex        | Decimal   | Data       |
|-----------------------|------------|-----------|------------|
| Header                | 37H        | 55        | 1 byte     |
| Identifier            | 37H        | 55        | 1 byte     |
| Horizontal size(*1)   | 30H - 39H  | 48 - 57   | 1 - 5 byte |
| Separator             | 1FH        | 31        | 1 byte     |
| Vertical size(*1)     | 30H - 39H  | 48 - 57   | 1 - 5 byte |
| Separator             | 1FH        | 31        | 1 byte     |
| Fixed value           | 31H        | 49        | 1 byte     |
| Separator             | 1FH        | 31        | 1 byte     |
| Other information(*2) | 30H or 31H | 48 or 49  | 1 byte     |
| NUL                   | 00H        | 0         | 1 byte     |
