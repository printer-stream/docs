## C O N F I D E N T I A L

## FS ( L pL pH fn sm [sa] ; [sb] ; [sc] ; [sd] ; [se] ; [sf] ; &lt;Function 33&gt;

[Name]

Paper layout setting

[Format]

ASCII FS ( L pL pH fn sm [sa] ; [sb] ; [sc] ; [sd] ; [se] ; [sf] ; Hex 1C 28 4C pL pH 21 sm [sa] 3B [sb] 3B [sc] 3B [sd] 3B [se] 3B [sf] 3B Decimal 28 40 76 pL pH 33 sm [sa] 59 [sb] 59 [sc] 59 [sd] 59 [se] 59 [sf] 59

[Range]

TM-P60 :

8 = (

pL

+

pH

×

256)

≤

26 (8

≤

pL

≤

26,

pH

= 0)

fn

= 33

'0'

≤

sm

≤

'3'

Other parameters differ according to sm .

| Parameter   | When ( sm = '0') is specified   | When ( sm = '1') is specified   | When ( sm = '2') is specified   | When ( sm = '3') is specified   |
|-------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
| sa          | '0'                             | '0,' '284' - '1550'             | '0,' '284' - '1550'             | '0,' '284' - '1550'             |
| sb          | '0'                             | '0' - '1500'                    | '-15' - '1500'                  | '-150' - '1500'                 |
| sc          | '0'                             | '0' - '50'                      | '0' - '50'                      | '-290' - '50'                   |
| sd          | '0'                             | '0'                             | '0' - '15'                      | '0'                             |
| se          | '0'                             | '-15' - '0'                     | '-15' - '15'                    | '0'                             |
| sf          | '290' - '600'                   | '290' - '600'                   | '290' - '600'                   | '290' - '600'                   |

- The value may be invalid in combination with the parameter. For details, refer to [Description].

<!-- formula-not-decoded -->

[Default]
