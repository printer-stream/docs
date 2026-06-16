<!-- image -->

## ESC	J	n

Name

Print and Paper Feed

Code

ASCII ESC J n

Hex. 1B 4A n

Decimal 27 74 n

Defined Region

0 ≤ n ≤ 255

Function

Prints the data in the print buffer and feeds the paper [n x basic calculated pitch].

Details

- Sets the print position to the beginning of the next line after execution.

- The line spacing amount set by the following commands is not affected.

- a. ESC 2 (Default line feed amount)

- b. ESC 3 (Set line feed amount)

- The basic calculated pitch is set by GSP (Set basic calculated pitch).

- If the calculation results in fractions, the pitch is corrected to a minimal mechanical pitch and the rest is discarded.

- In standard mode, the basic calculated pitch (y) for the vertical direction is used.

- In page mode, the basic calculated pitch that is used according to the starting point varies.

- a. When the starting point is specified to be upper left or lower right by the ESC T command (Character print direction selection in page mode), the basic calculated pitch (x) for the horizontal direction is used.

- b. When the starting point is specified to be upper right or lower left by the ESC T command (Character print direction selection in page mode), the basic calculated pitch (y) for the horizontal direction is used.

- Paper is fed approximately 1016 mm if the [n x basic calculated pitch] exceeds approximately 1016 mm (40 inches).

STAR

- When the setting for the line feed amount is smaller than the print data height in standard mode:

- a. If there is no print data, a line feed operation is executed according to the line feed amount.

- b. If there is print data, a line feed operation is executed for the height of the print data.

Reference

GS P
