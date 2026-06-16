<!-- image -->

## GS	*	xy	d1	…	d	(xX	yX	8)

Name

Define download bit images

Code

ASCII

GS * x y  d1...d (x×y×8)

Hex.

1D 2A x y  d1...d (x×y×8)

Decimal

29 42 x y  d1...d (x×y×8)

Defined Region

1 ≤ x ≤ 255

1 ≤ y ≤ 48 However, x × y ≤ 1536

0 ≤ d ≤ 255

Function

Defines the download bit image of the number of dots specified by x and y.

- x specifies the number of dots in the horizontal direction.

- y specifies the number of bytes in the vertical direction.

Details

- Horizontal direction dot count is x X 8 dots; Vertical direction dot count is y X 8 dots

- d indicates the bit-image data.

Bits that correspond to the dots to print are 1, and the bits that correspond to the dots that are not printed are 0.

- GS * (define download bit images) and ESC&amp; (define download characters) cannot both be defined simultaneously.  Download character definitions are cleared by executing this command.

- Defined download bit images are cleared under the following executions.

a. ESC @:

Initialize printer

b. ESC &amp;:

Define download characters

c. FS q:

Define NV bit image

- d. When the printer is reset or the power is turned off

- ·The following illustration shows the relationship between download bit images and the print data.
