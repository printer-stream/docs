<!-- image -->

## LF

Name

Line feed

Code

ASCII

LF

Hex.

0A

Decimal

10

Function

Prints the data in the print buffer and performs a line feed based on the set line feed amount.

Details

After execution, makes the top of the line the next print starting position.

STAR

When the setting for the line feed amount is smaller than the print data height:

a. If there is no print data, a line feed operation is executed according to the line feed amount.

b. If there is print data, a line feed operation is executed for the height of the print data.

Reference

See ESC 2, ESC 3, Appendix-1
