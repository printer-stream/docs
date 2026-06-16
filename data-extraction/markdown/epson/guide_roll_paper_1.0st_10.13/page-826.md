## C O N F I D E N T I A L

## FS ( L &lt; Function 65 &gt;

[Name]

Feed paper to the label peeling position

[Format]

ASCII

FS

(

L

pL

pH

fn

m

Hex

1C

28

4C

02

00

41

m

Decimal

28

40

76

2

0

65

m

[Range]

(

pL

+

pH

×

256) = 2 (

pL

= 2,

pH

= 0)

m = 48, 49

fn = 65

TM-L90

: with Peeler

m = 48 [When the peeling issuing mode is selected]

m = 48, 49 [When the continuous issuing mode is selected]

[Models other than the above]

m = 48, 49

TM-P60 :

m = 48, 49

## [Description]

## [Notes]

Feeds paper to the label peeling position.

|   m | Function                                                                                                                                                                  |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  48 | Feeds paper to the label peeling position. However, if the paper is in standby at the label peeling position, the printer does not feed.                                  |
|  49 | Feeds paper to the label peeling position. However, if the paper is in standby at the label peeling position, the printer feeds paper to the next label peeling position. |

- ■ Please use this function by using 'the first state of the line' in standard mode.
- ■ This function is used only with label paper.
- ■ The paper feed operation ends when no paper is detected in the paper feed to the label peeling position.
- ■ [Position information A] transmitted by Function 48 becomes (bit 0 = 1) when this function is processed. Moreover, the print area of the label paper or black mark paper if there is a print start position right under the label peeling position becomes 'current label.'
