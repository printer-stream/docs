<!-- image -->

## ESC 2

Name

Set default line spacing

Code

ASCII ESC 2

Hex.

1B 32

Decimal 27 50

Function

Sets line feed amount per one line to approximately 4.23 mm (1/6 inch).

Details

Line spacing can be set independently for both the standard and page modes.

STAR

EPSON has models that have 180 DPI and 203 DPI print heads.  STAR's print head is 203 DPI.  Therefore, when targeting models with the EPSON 180 DPI print head, it is necessary to correct the line spacing that will generate from the difference in the head's print density.

In this case, the default line spacing on STAR printers is corrected to the following according to the basic calculated pitch correction.  This does not apply for target models that have 203 DPI print heads, or models that do not require correction.

| Basic Calculate Pitch Correction   | Default Line Spacing             |
|------------------------------------|----------------------------------|
| 203 DPI                            | Approximately 4.23 mm (1/6 inch) |
| 180 DPI                            | Approximately 3.75 mm            |

Reference

ESC 3
