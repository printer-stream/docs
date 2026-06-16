<!-- image -->

Name

Specify absolute position

Code

ASCII ESC $ nL nH

Hex. 1B 24 nL nH

Decimal 27 36 nL nH

Defined Region

0 ≤ nL ≤ 255

0 ≤ nH ≤ 255

Function

Specifies the next printing starting position using an absolute position based on the left margin position.  The next printing starting position is the position specified by [(nL+nH×256) × basic calculated pitch] from the left margin position.

Details

- Specifications exceeding the print range are ignored.

- The basic calculated pitch is set by GSP (Set basic calculated pitch).

- If the calculation results in fractions, the pitch is corrected to a minimal mechanical pitch and the rest is discarded.

- In standard mode, the basic calculated pitch (x) for the horizontal direction is used.

- In page mode, the basic calculated pitch that is used according to the starting point varies.

- a. When the starting point is specified to be upper left or lower right by the ESC T command (Character print direction selection in page mode), the basic calculated pitch (x) for the horizontal direction is used.

- b. When the starting point is specified to be upper right or lower left by the ESC T command (Character print direction selection in page mode), the basic calculated pitch (y) for the horizontal direction is used.

STAR

Top of line does not exist when this command is used to specify anything other than the left margin position.  The top of the line is maintained only when the same position as the left margin position is specified.

Reference

ESC \ , GS $, GS \ , GS P
