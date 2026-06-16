## C O N F I D E N T I A L

## GS ( E pL pH fn x c1 c2[y d1...d(x × y)] k &lt;Function 9&gt;

[Name]

Define the data (raster format) for the character code page

[Format]

[Range]

## [Description]

## [Notes]

```
ASCII GS ( E pL pH fn x c1 c2 [x d1...d(x × y)]k Hex 1D 28 45 pL pH  08  x c1 c2 [x d1...d(x × y)]k Decimal 29 40 69 pL pH 8 x c1 c2 [x d1...d(x × y)]k
```

5

≤

(

pL

+

pH

fn = 9

0 ≤ d ≤ 255

×

256)

≤

128 ≤ c1 ≤ d2 ≤ 255

k = c2 -c1 + 1

| Font No. (configuration)   |   y |   x |
|----------------------------|-----|-----|
| 10 (9 × 17)                |   2 |  17 |
| 12 (12 × 24)               |   2 |  24 |
| 17 (8 × 16)                |   1 |  16 |
| 18 (10 × 24)               |   2 |  24 |

Defines the character pattern (raster format) for  the character code page in the work area.

- x specifies the number of bytes in the horizontal direction.
- c1 specifies the beginning character code for the definition, and c2 specifies the final code.
- y specifies the number of dots in the vertical direction from the top.
- d specifies the defined data (raster format).
- k indicates the number of the defined data. k is an explanation parameter; therefore, it does not need to be transmitted.
- ■ This function works in user setting mode.
- ■ Characters in Hexiadecimal: 80H to FFH / in Decimal: 128 to 255 in ASCII code can be defined.
- ■ If y, c1, c2, or x process a value out of the definition range, processing of this function is canceled.
- ■ Changes the data of the user-defined code page that is copied into the work area by Function 7.

65535

(0

≤

pL

≤

255, 0

≤

pH

≤

255)
