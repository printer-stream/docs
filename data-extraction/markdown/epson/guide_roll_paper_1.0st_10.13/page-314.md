## C O N F I D E N T I A L

## GS /

[Name]

Print downloaded bit image

[Format]

ASCII

GS / m

Hex

1D 2F m

Decimal 29 47 m

[Range]

0 ≤ m ≤ 3, 48 ≤ m ≤ 51

[Default]

None

[Printers not featuring this command] TM-P60 , TM-U230 , TM-U220

[Description]

Prints downloaded bit image using the process of GS ✻ and using the mode specified by m , as follows:

| m     | Mode          | Scaling for horizontal   | Scaling for vertical   |
|-------|---------------|--------------------------|------------------------|
| 0, 48 | Normal        | × 1                      | × 1                    |
| 1, 49 | Double-width  | × 2                      | × 1                    |
| 2, 50 | Double-height | × 1                      | × 2                    |
| 3, 51 | Quadruple     | × 2                      | × 2                    |

## [Recommended Functions]

This command is supported only by some printer models and may not be supported by future models.

It is recommended that NV graphics function (GS ( L GS 8 L: &lt;Function 52&gt; and &lt;Function 80&gt; ~ &lt;Function 85&gt;) be used because it offers the following additional features:

- Multiple logo data and mark data can be specified. (except for some models)
- Data can be controlled by key code.
- Redefining or deleting the same data is possible for each key code.
- Color can be specified for the definition data.
- Data can be defined by raster format.
- The remaining capacity of definition area can be confirmed.

EXECUTING COMMAND
