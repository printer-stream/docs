<!-- image -->

## ESC FS p n m

[Name] [Code]

Print logo

ASCII

ESC FS p n m

Hex.

1B 1C 70 n m

Decimal

27 28 112 n m

[Defined Area]

1 ≤ n ≤ 255 0 ≤ m ≤ 3 48 ≤ m ≤ 51 ('0' ≤ m ≤ '3')

[Initial Value] [Function]

- - -

Prints the logo of registration number n registered using the logo registration command (ESC FS q) according to the print mode m.

| m     | Logo print mode       |
|-------|-----------------------|
| 0, 48 | Normal mode           |
| 1, 49 | Double wide mode      |
| 2, 50 | Double high mode      |
| 3, 51 | Double high/wide mode |

If there is unprinted data in the line buffer, this command is executed after printing that data.

Therefore, it is not possible to print with other data in the same line (characters, bit images, bar codes).

Form feed obeys the vertical print size of the logo.

Adornments other than upside-down printing and expansion settings are unaffected.

The horizontal printing start position conforms to the left margin position and the horizontal print area conforms to the left and right margin settings.

If the logo horizontal print size exceeds the horizontal print region, the portion exceeding the area is not printed.

&lt;When using the 2 color print mode&gt;

When the logo register number n is odd:

Register number n is printed in black; register number n + 1 is printed in red and overlapped.

The command is ignored when the capacity of the register number n and the capacity of the register number n + 1 are different.

The command is ignored when the register number n = 255 is specified.

When the logo register number n is even:

Register number n is printed in black; register number n - 1 is printed in red and overlapped.

The command is ignored when the capacity of the register number n and the capacity of the register number n - 1 are different.

The command is ignored when the register number n = 255 is specified.

-----------------------------------------------------------------------------
