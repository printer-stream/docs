<!-- image -->

## GS ! n

Name

Select character size

Code

ASCII GS ! n

Hex.

1D 21 n

Decimal 29 33

n

Defined Region

0 ≤ n ≤ 255

However, 1 ≤ vertical direction magnification ratio ≤ 8, 1 ≤ horizontal direction magnification ratio ≤ 8

Initial Value

n = 0

Function

Specifies the character size (magnification ratio in the vertical and horizontal directions).

|   Bit | Function                                           | '0'               | '1'   |
|-------|----------------------------------------------------|-------------------|-------|
|     7 | Specifies horizontal direction magnification ratio | (See table below) |       |
|     6 | Specifies horizontal direction magnification ratio | (See table below) |       |
|     5 | Specifies horizontal direction magnification ratio | (See table below) |       |
|     4 | Specifies horizontal direction magnification ratio | (See table below) |       |
|     3 | Specifies vertical direction magnification ratio   | (See table below) |       |
|     2 | Specifies vertical direction magnification ratio   | (See table below) |       |
|     1 | Specifies vertical direction magnification ratio   | (See table below) |       |
|     0 | Specifies vertical direction magnification ratio   | (See table below) |       |

&lt;Horizontal Direction Magnification Ratio Specification&gt;

|   Bit-7 |   Bit-6 |   Bit-5 |   Bit-4 | Hor. Dir. Mag. Ratio   |
|---------|---------|---------|---------|------------------------|
|       0 |       0 |       0 |       0 | 1                      |
|       0 |       0 |       0 |       1 | 2                      |
|       0 |       0 |       1 |       0 | 3                      |
|       0 |       0 |       1 |       1 | 4                      |
|       0 |       1 |       0 |       0 | 5                      |
|       0 |       1 |       0 |       1 | 6                      |
|       0 |       1 |       1 |       0 | 7                      |
|       0 |       1 |       1 |       1 | 8                      |
|       1 |       0 |       0 |       0 | Undefined              |
|       1 |       0 |       0 |       1 | Undefined              |
|       1 |       0 |       1 |       0 | Undefined              |
|       1 |       0 |       1 |       1 | Undefined              |
|       1 |       1 |       0 |       0 | Undefined              |
|       1 |       1 |       0 |       1 | Undefined              |
|       1 |       1 |       1 |       0 | Undefined              |
|       1 |       1 |       1 |       1 | Undefined              |

&lt;Vertical Direction Magnification Ratio Specification&gt;

|   Bit-3 |   Bit-2 |   Bit-1 |   Bit-0 | Hor. Dir. Mag. Ratio   |
|---------|---------|---------|---------|------------------------|
|       0 |       0 |       0 |       0 | 1                      |
|       0 |       0 |       0 |       1 | 2                      |
|       0 |       0 |       1 |       0 | 3                      |
|       0 |       0 |       1 |       1 | 4                      |
|       0 |       1 |       0 |       0 | 5                      |
|       0 |       1 |       0 |       1 | 6                      |
|       0 |       1 |       1 |       0 | 7                      |
|       0 |       1 |       1 |       1 | 8                      |
|       1 |       0 |       0 |       0 | Undefined              |
|       1 |       0 |       0 |       1 | Undefined              |
|       1 |       0 |       1 |       0 | Undefined              |
|       1 |       0 |       1 |       1 | Undefined              |
|       1 |       1 |       0 |       0 | Undefined              |
|       1 |       1 |       0 |       1 | Undefined              |
|       1 |       1 |       1 |       0 | Undefined              |
|       1 |       1 |       1 |       1 | Undefined              |
