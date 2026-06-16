<!-- image -->

## ESC 3 n

Name

Set line feed amount

Code

ASCII ESC 3 n

Hex. 1B 33 n

Decimal 27 51 n

Defined Region

0 ≤ n ≤ 255

Initial Value

Line feed amount equivalent to approximately 4.23 mm (1/6 inch).

Function

Sets the line space for one line to [n x basic calculated pitch].

Details

- Line spacing can be set independently for both the standard and page modes.

- The basic calculated pitch is set by GSP (Set basic calculated pitch).  Also, after setting the line space, it is not affected even if the basic calculated pitch is changed.

- If the calculation results in fractions, the pitch is corrected to a minimal mechanical pitch and the rest is discarded.

- In standard mode, the basic calculated pitch (y) for the vertical direction is used.

- In page mode, the basic calculated pitch that is used according to the starting point varies.

- a. When the starting point is specified to be upper left or lower right by the ESC T command (Character print direction selection in page mode), the basic calculated pitch (x) for the horizontal direction is used.

- b. When the starting point is specified to be upper right or lower left by the ESC T command (Character print direction selection in page mode), the basic calculated pitch (y) for the horizontal direction is used.

- The maximum value that can be set for the line space is approximately 1,016mm (or 40 inches).  Specifications that exceed the maximum value are rounded off to that value.

Reference

ESC 2, GS P
