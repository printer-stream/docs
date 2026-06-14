## **C O N F I D E N T I A L** 

|m|**Bar code system**|**Bar code data (“SP” in the table indicates space.)**|**Bar code data (“SP” in the table indicates space.)**|**Bar code data (“SP” in the table indicates space.)**|**Bar code data (“SP” in the table indicates space.)**|
|---|---|---|---|---|---|
|||**Amount**<br>**of data**|**The range of**<br>n|**Characters**|**Data (**d**)**|
|69|CODE39|Can be changed|1≤ n ≤255|0~9, A~Z<br>SP, $, %, *, +, -, ., /|48≤ d ≤57, 65≤ d ≤90,<br>d= 32, 36, 37, 42, 43, 45, 46, 47|
|70|ITF<br>(Interleaved 2 of 5)|Can be changed<br>(even number)|2≤ n ≤255<br>(even number)|0~9|48≤ d ≤57|
|71|CODABAR<br>(NW-7)|Can be changed|1≤ n ≤255|0~9, A~D, a~d<br>$, +, -, ., /, :|48≤ d ≤57, 65≤ d ≤68, 97≤ d ≤<br>100<br>d= 36, 43, 45, 46, 47, 58<br>(65≤ d1 ≤68, 65≤ dn ≤68, 97≤<br>d1 ≤100, 97≤ dn ≤100)|
|72|CODE93|Can be changed|1≤ n ≤255|00H~7FH|0≤ d ≤127|
|73|CODE128|Can be changed|2≤ n ≤255|00H~7FH|0≤ d ≤127<br>[Howeverd1= 123, 65≤ d2 ≤67]|
|74|GS1-128|Can be changed|2≤ n ≤255|NUL~SP(7FH)|0≤ d ≤127|
|75|GS1 DataBar<br>Omnidirectional|Can be changed|n  = 13|0~9|48≤ d ≤57|
|76|GS1 DataBar<br>Truncated|Can be changed|n  = 13|0~9|48≤ d ≤57|
|77|GS1DataBar<br>Limited|Can be changed|n  = 13|0~9|48≤ d ≤57 [Howeverd1= 48, 49]|
|78|GS1 DataBar<br>Expanded|Can be changed|2≤ n ≤255|0~9, A~D, a~d<br>SP, !, ", %, $, ', (,<br>), *, +, ,, -, ., /,<br>:, ;, <, =, >, ?, _, {|48≤ d≤57, 65≤ d≤90, 97≤ d≤<br>122,<br>32≤ d≤34, 37≤ d≤47,<br>58≤ d≤63,d = 95,123<br>[Howeverd1 = 40, 48≤ d2≤57,<br>48≤ d3≤57 when<br>48≤ d1≤57, 48≤ d2≤57]|
