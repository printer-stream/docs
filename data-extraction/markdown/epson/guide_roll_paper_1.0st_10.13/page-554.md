## C O N F I D E N T I A L

## &lt;Function 61&gt; FS ( E pL pH fn m c ( fn =61)

[Name]

Transmit set values for top/bottom logo printing

[Format]

[Range]

[Description]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

fn = 61

m = 2

c = 48, 49, 50

Transmits set values for top/bottom logo printing by specifying c .

|   c | Function                                                    |
|-----|-------------------------------------------------------------|
|  48 | Transmits set values for top logo printing.                 |
|  49 | Transmits set values for bottom logo printing.              |
|  50 | Transmits extended set values for top/bottom logo printing. |

## ■ Data to be transmitted is as follows:

| Data to be transmitted             | Hex                      | Decimal                  | Data amount   |
|------------------------------------|--------------------------|--------------------------|---------------|
| (1) Header                         | 37H                      | 55                       | 1 byte        |
| (2) Identifier                     | 48H                      | 72                       | 1 byte        |
| (3) Set values for top/bottom logo | See the following pages. | See the following pages. | 0 to 11 bytes |
| (4) NUL                            | 00H                      | 0                        | 1 byte        |

EXECUTING COMMAND
