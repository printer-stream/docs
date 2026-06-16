<!-- image -->

## ESC D n1 n2…nk NUL

[Name] [Code]

Set horizontal tab

ASCII

ESC

D

n1

n2

...

nk NUL

Hex.

1B

44

n1

n2

...

nk

00

Decimal

27

68

n1

n2

...

nk

0

[Defined Area]

1 ≤ n ≤ 255

0 ≤ k ≤ 16

[Initial Value] [Function]

- - -

Uses the left edge as a standard to set the horizontal tab to the position of (current ANK character pitch x n).

The horizontal tab reference point is the right edge of the paper, regardless of the left margin.

ANK character pitch includes the right space and expansion settings are enabled.

All other horizontal tabs set before setting the horizontal tab using this command are cancelled A maximum of 16 horizontal tabs can be set.

However, the tab position must satisfy the following conditions.

If the following conditions are not met, data up to the NUL code is discarded.

Normal tabs that meet the conditions below are set and tabs after errors occur are not set.

- 1&lt;n1 &lt; n2... &lt; nk

- nk ≤ Printable region

The horizontal tab set using this command is unaffected by changing the character pitch.

Horizontal tabs set using the ESC D NUL command are cleared.

There is no initial value for the horizontal tab.

Standard mode and page mode can be set independently of each other.

## ESC D NUL

[Name]

Clear horizontal tab

[Code]

ASCII

ESC D NUL

Hex.

1B 44 00

Decimal

27 68 0

[Defined Area] - - -

[Initial Value]

- - -

[Function]

Clears the currently set horizontal tab.

Standard mode and page mode can be set independently of each other.

-----------------------------------------------------------------------------
