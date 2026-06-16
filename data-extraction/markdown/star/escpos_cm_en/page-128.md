<!-- image -->

Name

Code

Defined Region

Initial Value

Function

Details Specify/cancel white/black inverted printing ASCII

GS B n

Hex.

Decimal

0 ≤ n ≤ 255

n = 0

Specifies or cancels black and white inverted printing.

- Cancels black and white inverted printing when n = &lt;*******0&gt;B.
- Specifies black and white inverted printing when n = &lt;*******1&gt;B.
- n is effective only when it is the lowest bit.
- Internal characters and download characters are targeted for black and white inverted printing.
- The right space of set characters set by ESC SP (Set character right space amount) is also targeted for black and white inverted printing.
- The following are not targeted for black and white inverted printing.
- This does not affect the line spacing.
- Black and white inverted printing has priority over underlines.  Therefore, the inverted characters are not underlined, even if underline is specified.  However, the underline setting status does not change.
- This command is effective for ANK and Chinese characters.

- a. ESC*

: Bit image

b. GS /

: Download bit image

- c. GS k

: Bar code

- d. GS H

: HRI Characters

- e. HT

: Skipped portion by horizontal tab

f. ESC $

: Skipped portion by specification of vertical position

- g. ESC \

: Skipped portion by specification of relative position

1D 42 n

29 66 n
