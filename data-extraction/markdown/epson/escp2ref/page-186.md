## Format

<!-- formula-not-decoded -->

## Parameter range

0 ≤ nL ≤ 255 0 ≤ nH ≤ 31 m = 0, 1, 2, 3, 4, 5, 6, 7

## Function

Prints dot-graphics in 8-dot columns, depending on the following parameters:

m

nL, nH

Specifies the dot density (see table below)

Specify the total number of columns (k) of graphics data following, according to the formula

(number of dot columns) = ((nH × 256) + nL)

<!-- formula-not-decoded -->

d1 . . . d k Bytes of graphics data

## Dot density

|   Parameter m in ESC * command |   Horizontal density |   Vertical density | Adjacent dot printing   |   Dots per column |   Bytes per column |
|--------------------------------|----------------------|--------------------|-------------------------|-------------------|--------------------|
|                              0 |                   60 |                 72 | Yes                     |                 8 |                  1 |
|                              1 |                  120 |                 72 | Yes                     |                 8 |                  1 |
|                              2 |                  120 |                 72 | No                      |                 8 |                  1 |
|                              3 |                  240 |                 72 | No                      |                 8 |                  1 |
|                              4 |                   80 |                 72 | Yes                     |                 8 |                  1 |
|                              5 |                   72 |                 72 | Yes                     |                 8 |                  1 |
|                              6 |                   90 |                 72 | Yes                     |                 8 |                  1 |
|                              7 |                  144 |                 72 | Yes                     |                 8 |                  1 |

## Notes

- Graphics data that would print beyond the right-margin position is ignored.
- Bit-image graphics can be printed on the same line as text.
- Not all values for m are available on all printers; see the Command Table for a list of which values are available on your printer.
