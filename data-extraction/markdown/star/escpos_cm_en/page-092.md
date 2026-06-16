<!-- image -->

## &lt;Function	49&gt;	GS	(	K	pL	pH	fn	m		(Fn=49)

Name

Set print density

Code

ASCII GS ( K pL pH fn m

Hex. 1D 28 4B pL pH fn m

Decimal 29 40 75 pL pH fn m

Defined Region

{pL + (pH × 256) } = 2 (pL = 2, pH = 0)

fn = 49

250 ≤ m ≤ 255, 0 ≤ m ≤ 6

Initial Value

m = 0

Function

Sets print density.

Spec. A

|   m |   Print Density |
|-----|-----------------|
| 250 |             0.7 |
| 251 |             0.7 |
| 252 |             0.8 |
| 253 |             0.8 |
| 254 |             0.9 |
| 255 |             0.9 |
|   0 |             1.0 |
|   1 |             1.1 |
|   2 |             1.1 |
|   3 |             1.2 |
|   4 |             1.2 |
|   5 |             1.3 |
|   6 |             1.3 |

Spec. B

|     | Print Density                     | Print Density                                                     |
|-----|-----------------------------------|-------------------------------------------------------------------|
| m   | Single Color Printing Mode        | 2-color Printing Mode Red Print Density Double Resolution Mode *1 |
| 250 | Print density -3                  | Print density -1                                                  |
| 251 | Print density -3                  | Print density -1                                                  |
| 252 | Print density -2                  | Print density -1                                                  |
| 253 | Print density -2                  | Print density -1                                                  |
| 254 | Print density -1                  | Standard print density (Standard)                                 |
| 255 | Print density -1                  | Standard print density (Standard)                                 |
| 0   | Standard print density (Standard) | Standard print density (Standard)                                 |
| 1   | Print density + 1                 | Standard print density (Standard)                                 |
| 2   | Print density + 1                 | Standard print density (Standard)                                 |
| 3   | Print density + 2                 | Print density + 1                                                 |
| 4   | Print density + 2                 | Print density + 1                                                 |
| 5   | Print density + 3                 | Print density + 1                                                 |
| 6   | Print density + 3                 | Print density + 1                                                 |
