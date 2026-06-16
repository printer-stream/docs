## C O N F I D E N T I A L

## GS ( E pL pH fn a &lt;Function 12&gt;

```
[Name] Transmit the configuration item for the serial interface [Format] ASCII GS ( E pL pH fn a Hex 1D 28 45 pL pH  0B a Decimal 29 40 69 pL pH 11 a [Range] ( pL + pH × 256) = 2 ( pL = 2, pH = 0) fn = 12 TM-J2000/J2100 , TM-T90 , TM-L90 , TM-T20 , TM-U220 :1 ≤ a ≤ TM-T88IV , TM-T88V , TM-T70 : a = 1 TM-P60 : a = 1, 2
```

[Description]

[Notes]

4

Transmits the configuration item for the serial interface specified by a .

|   a | Communication item   |
|-----|----------------------|
|   1 | Transmission speed   |
|   2 | Parity               |
|   3 | Flow control         |
|   4 | Data length          |

- "ESC/POS transmission handshake" is unnecessary with this function.
- ■ This function works in user setting mode and during normal operation.
- ■ This function transmits 'Header to NUL' as follows:

| Transmit data                | Hex     | Decimal   | Data   |
|------------------------------|---------|-----------|--------|
| Header                       | 37H     | 55        | 1 byte |
| Identifier                   | 33H     | 51        | 1 byte |
| Communication condition (*1) | 30H-34H | 48-52     | 1 byte |
