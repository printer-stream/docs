<!-- image -->

Rev. 2.31

## ESC GS B B

[Name]

Customer display data request

[Code]

ASCII ESC GS B B

Hex.

1B 1D 42 42

Decimal

27 29 66 66

[Defined Area]

- - -

[Initial Value]

- - -

[Function]

Acquire customer display data from a customer display.

The customer display data transmission format from the printer &lt;ESC&gt;&lt;GS&gt; B B n1 n2 d1 ・・・ dk

n1+n2x256  : BYTE count (1 ≦ d ≦ 65535)

k

: n1 + n2 x 256

## ESC GS B C

[Name] Buffer clear

[Code]

ASCII

ESC GS B C

Hex.

1B 1D 42 43

Decimal

27 29 66 67

[Defined Area] - - -

[Initial Value]

- - -

[Function]

A customer display buffer of a printer is cleared.

--------------------------------------------------------------------------------------
