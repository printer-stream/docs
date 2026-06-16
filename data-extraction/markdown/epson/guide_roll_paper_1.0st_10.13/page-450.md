## C O N F I D E N T I A L

## ESC ( A pL pH fn n c &lt; Function 97 &gt; (TM-T88V, TM-T20)

[Name]

Sound buzzer in TM-T88V , TM-T20 models (registered sound pattern specified) (optional external buzzer)

[Format]

[Range]

[Description]

ASCII

Hex

Decimal

(

pL

+

pH

fn

= 97

1

≤

n

≤

×

7

0 ≤ c ≤ 255

Sounds a pattern specified by n the number of times specified by c .

|   n | Pattern               |
|-----|-----------------------|
|   1 | Pattern A             |
|   2 | Pattern B             |
|   3 | Pattern C             |
|   4 | Pattern D             |
|   5 | Pattern E             |
|   6 | Pattern for error     |
|   7 | Pattern for paper-end |

ESC

1B

(

28

27

40

A

41

65

pL

pL

pL

pL

= 3, pH

256) = 3 (

pH

pH

pH

= 0)

fn

fn

fn

n

n

n

c

c

c
