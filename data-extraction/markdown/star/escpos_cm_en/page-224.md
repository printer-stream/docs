<!-- image -->

Name

Set PDF417 module aspect ratio

Code

ASCII ESC GS x S 3 n

Hex. 1B 1D 78 53 33 n

Decimal 27 29 120 83 51 n

Defined Area

1 ≤ n ≤ 10

Initial Value

n = 3

Function

Parameter details

- n:  Sets the module aspect ratio (asp).

The module Y direction size (x-dim x asp) is set using this command.

It is recommended that 2 ≤ n when specifying using this command.

When using with n = 1, check by actual use.

## ESC	GS	x	D	nL	nH	d1	d2	…	dk

Name

Set PDF417 bar code data

Code

ASCII

ESC

GS

x

D

nL

nH

d1

d2

…

dk

Hex. 1B 1D 78 44 nL nH d1 d2 … dk

Decimal 27 29 120

68

nL

nH

d1

d2

…

dk

Defined Area

0 ≤ nL ≤ 255, 0 ≤ nH ≤ 255

1 ≤ (nL + nH x 256) ≤ 1024

0 ≤ d ≤ 255

1 ≤ k ≤ 1024

Initial Value

---

Function

Parameter details

• nL + nH x 256  : Bar code data count

• dk

: Bar code data (Maximum 1024 data)

When [nL + nH x 256] is outside of the definition, data of [nL + nH x 256] bytes is discarded.
