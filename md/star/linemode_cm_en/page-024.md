Spec. B. 

[Defined Area] n1 = 0 n2 = 48 1 ≤ (n1 + n2 x 256) 0 ≤ da ≤ 255 (Font-A data) 0 ≤ db ≤ 255 (Font-B data) k = (n1 + n2 x 256) ÷ 2 --- 

[Initial Value] --[Function] A blank code page indicates a character code table where character codes from 80h to FFh are all blank. 

A blank code page can be selected using the ESC GS t n command n = 255. The following is the data written to the blank code page. Font-A: 1 character = 48 bytes   6144 bytes = 48 bytes x 128 characters Font-B: 1 character = 48 bytes   6144 bytes = 48 bytes x 128 characters Send Font-A and Font-B data continuously. 

The printer is reset when writing with this command is completed. 

## [Font-A Data Format  Vertical 24 dots x Horizontal 12 dots] 

|~~po~~||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Da1<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da2|●|●|●|●|○|○|○|○|
|Da3<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da4|●|●|●|●|○|○|○|○|
|Da5<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da6|●|●|●|●|○|○|○|○|
|Da7<br>~~**p**o~~|●|●|●|●|●|●|●|●<br>~~o~~|Da8<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da9<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da10<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da11<br>~~po~~<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da12<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da13<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da14|●|●|●|●|○|○|○|○|
|Da15<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da16|●|●|●|●|○|○|○|○|
|Da17<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da18<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da19<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da20|●|●|●|●|○|○|○|○|
|Da21<br>~~po~~<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da22|●|●|●|●|○|○|○|○|
|Da23<br>~~po~~<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da24|●|●|●|●|○|○|○|○|
|Da25<br>~~po~~<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da26|●|●|●|●|○|○|○|○|
|Da27<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da28|●|●|●|●|○|○|○|○|
|Da29<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da30|●|●|●|●|○|○|○|○|
|Da31<br>~~**p**o~~|●|●|●|●|●|●|●|●<br>~~o~~|Da32<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da33<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da34<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da35<br>~~po~~<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da36<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da37<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da38|●|●|●|●|○|○|○|○|
|Da39<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da40|●|●|●|●|○|○|○|○|
|Da41<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da42<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da43<br>~~po~~<br>~~po~~|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|Da44<br>|●<br>|●<br>|●<br>|●<br>|○<br>|○<br>|○<br>|○<br>|
|Da45<br>~~po~~<br>~~po~~|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|Da46<br>|●<br>|●<br>|●<br>|●<br>|○<br>|○<br>|○<br>|○<br>|
|Da47<br>~~poPo~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|Da48<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|○<br>~~Po~~|○<br>~~Po~~|○<br>~~Po~~|○<br>~~Po~~|



• = Data region/ ○ =Zero data 

## [Font-B Data Format  Vertical 24 dots x Horizontal 9 dots] 

|~~**p**o~~||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Da1<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da2|●|○|○|○|○|○|○|○|
|Da3<br>~~**p**o~~|●|●|●|●|●|●|●|●<br>~~o~~|Da4<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da5<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da6<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da7<br>~~po~~<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da8<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da9<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da10|●|○|○|○|○|○|○|○|
|Da11<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da12|●|○|○|○|○|○|○|○|
|Da13<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da14<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da15<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da16|●|○|○|○|○|○|○|○|
|Da17<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da18|●|○|○|○|○|○|○|○|
|Da19<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da20<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da21<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da22|●|○|○|○|○|○|○|○|
|Da23<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da24|●|○|○|○|○|○|○|○|
|Da25<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da26|●|○|○|○|○|○|○|○|
|Da27<br>~~**p**o~~|●|●|●|●|●|●|●|●<br>~~o~~|Da28<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da29<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da30<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da31<br>~~po~~<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da32<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da33<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da34|●|○|○|○|○|○|○|○|
|Da35<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da36|●|○|○|○|○|○|○|○|
|Da37<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da38<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da39<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da40|●|○|○|○|○|○|○|○|
|Da41<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da42|●|○|○|○|○|○|○|○|
|Da43<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da44<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da45<br>~~po~~<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~SG~~|●<br>~~SG~~|●<br>~~NGG~~|Da46<br>~~NGG~~|●<br>~~NGG~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~NG~~|○<br>~~NG~~|○<br>~~GO~~|
|Da47<br>~~po~~<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~SG~~|●<br>~~SG~~|●<br>~~NGG~~|Da48<br>~~NGG~~|●<br>~~NGG~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~NG~~|○<br>~~NG~~|○<br>~~GO~~|



• = Data region/ ○ =Zero data 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-6 
