## C O N F I D E N T I A L

## GS ( k &lt;Function 380&gt;

[Name]

2-dimensional GS1 DataBar: Store the data in the symbol storage area

[Format]

ASCII

GS

(

k

pL

pH

cn

fn

m

n

d1...dk

Hex

1D

28

6B

pL

pH

33

50

30

n

d1...dk

Decimal 29 40 107 pL pH 51 80 48 n d1...dk

[Range]

6 ≤ ( pL + pH × 256) ≤ 259  (0 ≤ pL ≤ 255, pH = 0, 1)

cn = 51

fn = 80

m = 48

n =  72, 73, 76

k = ( pL + pH × 256) - 4

The domain of (d) differs with the type of 2-dimensional GS1 DataBar. Refer to the [Function] table.

[Description]

The 2-dimensional GS1 DataBar symbol data ( d1...dk ) specified by n is saved in the symbol storage area.

|    |                                     | Symbol data (SP indicates a space)   | Symbol data (SP indicates a space)                                              | Symbol data (SP indicates a space)                                                                                                                                   |
|----|-------------------------------------|--------------------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| m  | 2-dimensional GS1 DataBar           | Data (k)                             | Characters (ASCII)                                                              | Data ( d )                                                                                                                                                           |
| 72 | GS1 DataBar Stacked                 | k = 13                               | "0"~"9"                                                                         | 48 ≤ d ≤ 57                                                                                                                                                          |
| 73 | GS1 DataBar Stacked Omnidirectional | k = 13                               | "0"~"9"                                                                         | 48 ≤ d ≤ 57 [However d1 = 48, 49]                                                                                                                                    |
| 76 | GS1 DataBar Expanded Stacked        | 0 ≤ k ≤ 255                          | 0~9, A~D, a~d SP, !, ", %, $, ', (, ), *, +, ,, -, ., /, :, ;, <, =, >, ?, _, { | 48 ≤ d ≤ 57, 65 ≤ d ≤ 90, 97 ≤ d ≤ 122, 32 ≤ d ≤ 34, 37 ≤ d ≤ 47, 58 ≤ d ≤ 63, d = 95,123 [However d1 = 40, 48 ≤ d2 ≤ 57, 48 ≤ d3 ≤ 57 , 48 ≤ d1 ≤ 57, 48 ≤ d2 ≤ 57] |

[Notes]

- ■ Data stored in the symbol storage area by this function is processed by Functions 381 and 382. The data in the symbol storage area are reserved after processing Function 381 or 382.
