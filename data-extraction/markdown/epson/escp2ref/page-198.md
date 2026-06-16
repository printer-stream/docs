## Format

<!-- formula-not-decoded -->

## Parameter range

0 ≤ nL ≤ 255

<!-- formula-not-decoded -->

## Function

Prints dot-graphics in 9-dot columns, depending on the following parameters:

m

Specifies the dot density (see table below)

nL, nH

Specify the total number of graphics data bytes (two bytes per column)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## d1 . . . d k Bytes of graphics data

## Dot density

|   Parameter m |   Horizontal density (dpi) |   Vertical density (dpi) | Adjacent dot printing   |   Dots per column |   Bytes per column |
|---------------|----------------------------|--------------------------|-------------------------|-------------------|--------------------|
|             0 |                         60 |                       72 | Yes                     |                 9 |                  2 |
|             1 |                        120 |                       72 | Yes                     |                 9 |                  2 |

Each dot column requires two bytes of data. The first byte represents the top 8 dots in the print head. Bit 0 (the LSB) in the second byte represents the ninth (bottom) dot in the print head; the remaining 7 bits are ignored.

## Notes

- This is a nonrecommended command; use the ESC * command instead.
- Graphics data that would print beyond the right-margin position is ignored.
- Bit-image graphics can be printed on the same line as text.
