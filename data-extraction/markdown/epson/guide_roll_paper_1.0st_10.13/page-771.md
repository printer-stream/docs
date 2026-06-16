## C O N F I D E N T I A L

## GS ( E pL pH fn a &lt;Function 14&gt;

[Name]

Transmit the configuration item for the Bluetooth interface

[Format]

$$ASCII GS ( E pL pH fn a Hex 1D 28 45 02 00 0E a Decimal 29 40 69 02 00 14 a$$

[Range]

$$( pL + pH × 256) = 2 ( pL = 2, pH = 0) fn = 14 a = 48, 49, 65$$

[Description]

Transmits the configuration item for the Bluetooth interface specified by a .

|   a | Communication item                 |
|-----|------------------------------------|
|  48 | Bluetooth device address (BD_ADDR) |
|  49 | Passkey                            |
|  50 | Device name                        |

- When ( a = 48, 49) is specified, "ESC/POS transmission handshake" is unnecessary.
- When ( a = 65) is specified, "ESC/POS transmission handshake" is necessary.
- ■ This function operates in both the user setting mode and during normal operation.
- ■ When ( a = 48, 49) is specified, the following Header to NUL is transmitted.

| Transmit data                | Hex        | Decimal   | Data      |
|------------------------------|------------|-----------|-----------|
| Header                       | 37H        | 55        | 1 byte    |
| Identifier                   | 4AH        | 74        | 1 byte    |
| Communication condition (*1) | 30H or 31H | 48 or 49  | 1 byte    |
| Setting value (*2)           | 20H - FFH  | 32 - 255  | 1-16 byte |
| NUL                          | 00H        | 0         | 1 byte    |

[Notes]
