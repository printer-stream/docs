<!-- image -->

## ESC SO

[Name] [Code]

Set double high

ASCII

ESC SO

Hex.

1B 0E

Decimal

27 14

[Defined Area]

- - -

[Initial Value]

Double high expansion cancelled.

[Function]

Specifies double high for ANK characters and Kanji characters.

This command is equivalent to ESC h  n (n = 1).

## ESC DC4

[Name]

Cancel expanded high

[Code]

ASCII

ESC  DC4

Hex.

1B 14

Decimal

27 20

[Defined Area]

- - -

[Initial Value]

- - -

[Function]

Cancels expanded high if the following commands specify expanded high.

- Double high specifying command (ESC SO)

- Set/cancel the double high (ESC h)

- Set/cancel double wide/high (ESC i)

This command is equivalent to ESC h  n (n = 0).

-----------------------------------------------------------------------------
