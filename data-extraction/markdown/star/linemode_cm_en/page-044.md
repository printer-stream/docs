<!-- image -->

## ESC B n1 n2…nk NUL

[Name] [Code]

Set vertical tab position

ASCII

ESC B n1 n2 ... nk NUL

Hex.

1B

42

n1

n2

...

nk

00

Decimal

27 66 n1 n2 ... nk 0

[Defined Area]

1 ≤ n ≤

255 16

0 ≤ k ≤

[Initial Value] [Function]

- - -

Sets the vertical tab to the (current form feed amount x n) position.

All other vertical tabs set before setting the vertical tab using this command are cancelled A maximum of 16 vertical tabs can be set. However, the tab position must satisfy the condition of 1 ≤ n1 ≤ n2... ≤ nk. When receiving such illegal codes, tabs up to the illegal code are set, but those after the illegal code are discarded up to the NUL code so illegal code tab are not set.

The vertical tab set using this command is unaffected by changing the form feed amount later. Vertical tabs set using the ESC B NUL command are cleared.

There is no initial value for the vertical tab.

## ESC B NUL

[Name]

Clear vertical tab position

[Code]

ASCII

ESC B NUL

Hex.

1B 42 00

Decimal

27 66 0

[Defined Area]

- - -

[Initial Value]

- - -

[Function]

Clears the currently set vertical tab.

-----------------------------------------------------------------------------
