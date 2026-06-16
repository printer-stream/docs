## C O N F I D E N T I A L

## GS Q 0

```
[Name] Print variable vertical size bit image [Format]
```

```
ASCII GS Q 0 m xL xH yL yH d1...dk Hex 1D 51 30 m xL xH yL yH d1...dk Decimal 29 81 48 m xL xH yL yH d1...dk
```

[Printers not featuring this command] TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 , TM-U230 , TM-U220

[Range] 0 ≤ m ≤ 3, 48 ≤ m ≤ 51 1 ≤ ( xL + xH × 256 ) ≤ 4256 (0 ≤ xL ≤ 255, 0 ≤ xH ≤ 12) 1 ≤ ( yL + yH × 256 ) ≤ 16 (1 ≤ yL ≤ 16, yH = 0) 0 ≤ d ≤ 255 k = ( xL + xH × 256) × ( yL + yH × 256)

[Description]

Prints a variable vertical size bit image using the mode specified by m , as follows:

| m     | Mode          | Scaling for horizontal   | Scaling for vertical   |
|-------|---------------|--------------------------|------------------------|
| 0, 48 | Normal        | × 1                      | × 1                    |
| 1, 49 | Double-width  | × 2                      | × 1                    |
| 2, 50 | Double-height | × 1                      | × 2                    |
| 3, 51 | Quadruple     | × 2                      | × 2                    |

- xL , xH specifies ( xL + xH × 256) dots in horizontal direction for the bit image.
- yL , yH specifies ( yL + yH × 256) bytes in vertical direction for the bit image.
- d specifies the bit image data (column format).
- k indicates the number of the bit image data. k is an explanation parameter; therefore, it does not need to be transmitted.

EXECUTING COMMAND
