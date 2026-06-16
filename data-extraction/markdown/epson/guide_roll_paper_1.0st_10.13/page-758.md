## C O N F I D E N T I A L

## GS ( E pL pH fn y c1 c2[x d1...d(y × x)] k &lt;Function 8&gt;

[Name]

Define the data (column format) for the character code page

[Format]

[Range]

## [Description]

## [Notes]

ASCII

Hex

Decimal

5

≤

(

pL

GS

1D

29

(

28

40

E

45

69

+

pH

×

256)

pL

pL

pL

≤

fn = 8

0 ≤ d ≤ 255

65535

128 ≤ c1 ≤ d2 ≤ 255

k = c2 -c1 + 1

| Font No. (configuration)   |   y |   x |
|----------------------------|-----|-----|
| 10 (9 × 17)                |   3 |   9 |
| 12 (12 × 24)               |   3 |  12 |
| 17 (8 × 16)                |   2 |   8 |
| 18 (10 × 24)               |   3 |  10 |

Defines the character pattern (column format) for the character code page in the work area.

- y specifies the number of bytes in the vertical direction.
- c1 specifies the beginning character code for the definition, and c2 specifies the final code.
- x specifies the number of dots in the horizontal direction from the left.
- d specifies the defined data (column format).
- k indicates the number of the defined data. k is an explanation parameter; therefore, it does not need to be transmitted.
- ■ This function works in user setting mode.
- ■ Characters in Hexadecimal: 80H to FFH / in Decimal: 128 to 255 in ASCII code can be defined.
- ■ If y, c1, c2, or x process a value out of the definition range, processing of this function is canceled.

pH

fn

y

pH  08  y

pH

8

y

(0

≤

pL

c1

c1

c1

≤

255, 0

c2

c2

c2

pH

[x

[x

[x d1...d(y

×

d1...d(y

×

d1...d(y

≤

×

255)

≤

x)]k

x)]k

x)]k
