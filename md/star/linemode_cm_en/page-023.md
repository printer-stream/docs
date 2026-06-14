**ESC GS = n1 n2 da1 da2...dak db1 db2...dbk** 

[Name] Write blank code page data [Code] ASCII ESC GS = n1 n2 da1 da2 ... dak db1 db2 … dbk Hex. 1B 1D 3D n1 n2 da1 da2 ... dak db1 db2 … dbk Decimal 27 29 61 n1 n2 da1 da2 ... dak db1 db2 … dbk 

Spec. Aification [Defined Area] n1= 0 n2 = 48 1≤(n1 + n2 x 256) 0≤da≤255      (Font-A data) db = 0            (STAR mode is not installed with Font-B.) k = (n1 + n2 x 256) ÷ 2 [Initial Value] - - - [Function] A blank code page indicates a character code table where character codes from 80h to FFh are all blank. 

A blank code page can be selected using the ESC GS t n command n = 255. The printer is reset when writing with this command is completed. 

Font-A Data Format  Vertical 24 dots x Horizontal 12 dots] 

|~~po~~||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Da1<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da2|●|●|●|●|○|○|○|○|
|Da3<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da4|●|●|●|●|○|○|○|○|
|Da5<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da6|●|●|●|●|○|○|○|○|
|Da7<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da8<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da9<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da10|●|●|●|●|○|○|○|○|
|Da11<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da12|●|●|●|●|○|○|○|○|
|Da13<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da14<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da15<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da16|●|●|●|●|○|○|○|○|
|Da17<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da18|●|●|●|●|○|○|○|○|
|Da19<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da20|●|●|●|●|○|○|○|○|
|Da21<br>~~**p**o~~|●|●|●|●|●|●|●|●<br>~~o~~|Da22<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da23<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da24<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da25<br>~~po~~<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da26<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da27<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da28|●|●|●|●|○|○|○|○|
|Da29<br>~~po~~<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da30|●|●|●|●|○|○|○|○|
|Da31<br>~~po~~<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da32|●|●|●|●|○|○|○|○|
|Da33<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da34|●|●|●|●|○|○|○|○|
|Da35<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da36|●|●|●|●|○|○|○|○|
|Da37<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da38<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da39<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da40|●|●|●|●|○|○|○|○|
|Da41<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da42|●|●|●|●|○|○|○|○|
|Da43<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da44|●|●|●|●|○|○|○|○|
|Da45<br>~~**p**o~~<br>~~Po TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~o~~<br>~~TT~~|Da46<br>~~o~~<br>~~TT~~|●<br>~~o~~<br>~~TT~~|●<br>~~o~~<br>~~TT~~|●<br>~~o~~<br>~~TT~~|●<br>~~o~~<br>~~TT~~|○<br>~~o~~<br>~~TT~~|○<br>~~o~~<br>~~TT~~|○<br>~~o~~<br>~~TT~~|○<br>~~o~~<br>~~TT~~|
|Da47<br>~~Po TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|Da48<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|○<br>~~TT~~|○<br>~~TT~~|○<br>~~TT~~|○<br>~~TT~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-5 
