<!-- image -->

## GS	b	n

Name

Specify/cancel smoothing

Code

ASCII

GS b n

Hex.

1D 62 n

Decimal

29 98 n

Defined Region

0 ≤ n ≤ 255

Initial Value

n = 0

Function

Specifies or cancels smoothing.

- Cancels smoothing when n = &lt;*******0&gt;B.

- Specifies smoothing when n = &lt;*******1&gt;B.

Details

- n is effective only when it is the lowest bit.

- Targets for smoothing are: embedded characters, download characters and external characters

- Even if smoothing is specified, it will not be performed if the character is set for magnification in either the vertical or horizontal directions.

Reference

ESC !, GS !
