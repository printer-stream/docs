## C O N F I D E N T I A L

```
TM-U220 : d1...dk = "9600" [ a = 1] d = 48 [ a = 2] d = 48 [ a = 3] d = 56 [ a = 4]
```

Sets the configuration item for the serial interface specified by a to the values specified by d1...dk .

|   a | Configuration item   |
|-----|----------------------|
|   1 | Transmission speed   |
|   2 | Parity               |
|   3 | Flow control         |
|   4 | Data length          |

- Transmission speed ( a = 1) is specified by number. The baud rate that can be specified differs, depending on the printer model.

Example: When defining 19200 bps: 5 bytes as '19200' (Hexadecimal = 31H, 39H, 32H, 30H, 30H / Decimal = 49, 57, 50, 48, 48)

- Parity ( a = 2) is specified by d as follows:
- Flow control ( a = 3) is specified by d as follows:

|   d | Function           |
|-----|--------------------|
|  48 | Select no parity   |
|  49 | Select odd parity  |
|  50 | Select even parity |

|   d | Function                        |
|-----|---------------------------------|
|  48 | Select Flow control of DTR/DSR  |
|  49 | Select Flow control of XON/XOFF |

[Description]
