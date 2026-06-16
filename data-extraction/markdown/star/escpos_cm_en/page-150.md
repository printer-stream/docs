<!-- image -->

## 1.	GS	k	m	d1	…	dk	NUL, 2.3.	GS	k	m	n	d1	…	dk

Name

Print bar code

Code

1. ASCII GS k m  d1...dk  NUL

Hex. 1D 6B m  d1...dk  NUL

Decimal 29 107 m  d1...dk  NUL

2.3. ASCII  GS k m n  d1...dk

Hex.

1D 6B m n  d1...dk

Decimal

29 107 m n  d1...dk

Defined Region

1. 0 ≤ m ≤ 6 The definition region of k and d differ according to the bar code type.

2. 65 ≤ m ≤ 73   The definition region of n and d differ according to the bar code type.

3. 65 ≤ m ≤ 78   The definition region of n and d differ according to the bar code type.

Function

Selects bar code type and prints bar codes.

## For 1:

|   m | Bar Code Type   | Defined region of k                      | Defined region of d                                  |
|-----|-----------------|------------------------------------------|------------------------------------------------------|
|   0 | UPC-A           | 11 ≤ k ≤ 12                              | 48 ≤ d ≤ 57                                          |
|   1 | UPC-E           | 11 ≤ k ≤ 12                              | 48 ≤ d ≤ 57                                          |
|   2 | JAN13 (EAN13)   | 12 ≤ k ≤ 13                              | 48 ≤ d ≤ 57                                          |
|   3 | JAN8 (EAN8)     | 7 ≤ k ≤ 8                                | 48 ≤ d ≤ 57                                          |
|   4 | CODE39          | 1 ≤ k                                    | 48 ≤ d ≤ 57, 65 ≤ d ≤ 90, 32, 36, 37, 43, 45, 46, 47 |
|   5 | ITF             | 2 ≤ k (However, this is an even number.) | 48 ≤ d ≤ 57                                          |
|   6 | CODABAR         | 1 ≤ k                                    | 48 ≤ d ≤ 57, 65 ≤ d ≤ 68, 36, 43, 45, 46, 47, 58     |

## For 2:

|   m | Bar Code Type   | Defined region of n       | Defined region of d                                 |
|-----|-----------------|---------------------------|-----------------------------------------------------|
|  65 | UPC-A           | 11 ≤ n ≤ 12               | 48 ≤ d ≤ 57                                         |
|  66 | UPC-E           | 11 ≤ n ≤ 12               | 48 ≤ d ≤ 57                                         |
|  67 | JAN13(EAN13)    | 12 ≤ n ≤ 13               | 48 ≤ d ≤ 57                                         |
|  68 | JAN8(EAN8)      | 7 ≤ n ≤ 8                 | 48 ≤ d ≤ 57                                         |
|  69 | CODE39          | 1 ≤ n ≤ 255               | 48 ≤ d ≤ 57, 65 ≤ d ≤ 90,32, 36, 37, 43, 45, 46, 47 |
|  70 | ITF             | 2 ≤ n ≤ 255 (Even number) | 48 ≤ d ≤ 57                                         |
|  71 | CODABAR         | 1 ≤ n ≤ 255               | 48 ≤ d ≤ 57, 65 ≤ d ≤ 68,36, 43, 45, 46, 47, 58     |
|  72 | CODE93          | 1 ≤ n ≤ 255               | 0 ≤ d ≤ 127                                         |
|  73 | CODE128         | 2 ≤ n ≤ 255               | 0 ≤ d ≤ 127                                         |
