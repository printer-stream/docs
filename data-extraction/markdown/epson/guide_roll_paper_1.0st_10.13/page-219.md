## C O N F I D E N T I A L

## FS p

[Name]

Print NV bit image

[Format]

```
ASCII FS p n m Hex 1C 70 n m Decimal 28 112 n m
```

[Printers not featuring this command] TM-L90 , TM-P60 , TM-U230

[Range]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 : 0 ≤ m ≤ 3, 48 ≤ m ≤ 51 TM-U220 : m = 0, 1, 48, 49

[Description]

1 ≤ n ≤ 255

Prints NV bit image n using the process of FS q and using the mode specified by m .

| m     | Mode          | Scaling for horizontal   | Scaling for vertical   |
|-------|---------------|--------------------------|------------------------|
| 0, 48 | Normal        | × 1                      | × 1                    |
| 1, 49 | Double-width  | × 2                      | × 1                    |
| 2, 50 | Double-height | × 1                      | × 2                    |
| 3, 51 | Quadruple     | × 2                      | × 2                    |

## [Recommended Functions]

This function is supported only by some printer models and may not be supported by future models. It is recommended that NV graphics function ( GS ( L GS 8 L : &lt;Function 51&gt; and &lt;Function 64&gt; ~ &lt;Function 69&gt;) be used because they offer the following additional features:

- Multiple logo data and mark data can be specified (except for some models).
- Data can be controlled by key code.
- Redefining or deleting the same data is possible for each key code.
- Color can be specified for the definition data.
- Data can be defined by raster format.
- The remaining capacity of the definition area can be confirmed.

EXECUTING COMMAND
