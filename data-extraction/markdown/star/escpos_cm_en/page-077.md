<!-- image -->

Name

Specify/cancel upside-down printing

Code

ASCII ESC { n

Hex. 1B 7B n

Decimal

27 123 n

Defined Region

0 ≤ n ≤ 255

Initial Value

n = 0

Function

Specifies or cancels upside-down printing.

- Cancels upside-down printing when n = &lt;*******0&gt;H.

- Specifies upside-down printing when n = &lt;*******1&gt;H.

Details

- n is effective only when it is the lowest bit.

- This command is effective only when input at the top of the line when standard mode is being used.

- This command has no affect in page mode.  In page mode, this command is only effective for the setting.

- Upside-down printing rotates line data 180 degrees.

STAR

- The characters that are printed in upside-down printing are reversed, but the order of the lines that are printed are not in reverse.

When upside-down printing is canceled

ABCDEF 012345

When upside-down printing is specified

ABCDEF 012345

Paper Feed Cirection

•Upside-down printing is enabled for the following images.

a. ESC * :

Specify bit image mode

b. GS /:

Print download bit images

c. FS P:

Print NV bit image mode
