## C O N F I D E N T I A L

## GS k

[Name]

Print bar code

## [Format]

(A)ASCII

GS k m d1 ... dk

NUL

Hex

1D 6B m d1 ... dk

NUL

Decimal

29 107 m d1 ... dk

NUL

(B) ASCII

GS k m n

d1 ... dn

Hex

1D 6B m n

d1 ... dn

Decimal

29 107 m n

d1 ... dn

## [Range]

## TM-J2000/J2100 , TM-T90 , TM-T88IV , TM-T70 , TM-L90 :

(A)

0

≤

m

≤

6

(B)

65

≤

m

≤

73

## TM-T20 , TM-T88V :

- (B) 65 ≤ m ≤ 78
- (A) 0 ≤ m ≤ 6

## TM-P60 :

- (B) 65 ≤ m ≤ 78 [ TM-P60 with Peeler]
- (A) 0 ≤ m ≤ 6

65 ≤ m ≤ 73 [ TM-P60 other than Peeler model]

The domain of d and k of &lt;Function A&gt; and of n and d of &lt;Function B&gt; differs according to the bar code format. Refer to the [Function] table.

## [Printers not featuring this command] TM-U230 , TM-U220

## [Description]

Prints the bar code using the bar code system specified by m . &lt;Function A&gt;

|    |                 | Bar code data ('SP' in the table indicates space.)   | Bar code data ('SP' in the table indicates space.)   | Bar code data ('SP' in the table indicates space.)   | Bar code data ('SP' in the table indicates space.)   |
|----|-----------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| m  | Bar code system | Amount of data                                       | The range of k                                       | Characters                                           | Data ( d )                                           |
| 0  | UPC-A           | Fixed                                                | k = 11, 12                                           | 0~9                                                  | 48 ≤ d ≤ 57                                          |
| 1  | UPC-E           | Fixed                                                | 6 ≤ k ≤ 8, k = 11, 12                                | 0~9                                                  | 48 ≤ d ≤ 57 [However, d1 = 48 when k = 7, 8, 11, 12] |

EXECUTING COMMAND
