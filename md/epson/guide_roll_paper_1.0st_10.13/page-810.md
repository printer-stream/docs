## **C O N F I D E N T I A L** 

## **FS ( L** _**pL pH fn sm [sa] ; [sb] ; [sc] ; [sd] ; [se] ; [sf] ;**_ <Function 33> 

[Name] Paper layout setting [Format] ASCII FS ( L _pL pH fn sm [sa] ; [sb] ; [sc] ; [sd] ; [se] ; [sf] ;_ Hex 1C 28 4C _pL pH 21 sm [sa] 3B [sb] 3B [sc] 3B [sd] 3B [se] 3B [sf] 3B_ Decimal 28 40 76 _pL pH 33 sm [sa] 59 [sb] 59 [sc] 59 [sd] 59 [se] 59 [sf] 59_ [Range] TM-P60 **: 8 = (** pL **+** pH × **256)** ≤ **26 (8** ≤ pL ≤ **26,** pH **= 0)** fn **= 33 “0”** ≤ sm ≤ **“3” Other parameters differ according to** sm **.** 

|**Parameter**|**When (**sm **= “0”)**<br>**is specified**|**When (**sm **= “1”)**<br>**is specified**|**When (**sm **= “2”)**<br>**is specified**|**When (**sm **= “3”)**<br>**is specified**|
|---|---|---|---|---|
|sa|“0”|“0,” “284” - “1550”|“0,” “284” - “1550”|“0,” “284” - “1550”|
|sb|“0”|“0” - “1500”|“-15” - “1500”|“-150” - “1500”|
|sc|“0”|“0” - “50”|“0” - “50”|“-290” - “50”|
|sd|“0”|“0”|“0” - “15”|“0”|
|se|“0”|“-15” - “0”|“-15” - “15”|“0”|
|sf|“290” - “600”|“290” - “600”|“290” - “600”|“290” - “600”|



[Default] 

• The value may be invalid in combination with the parameter. For details, refer to [Description]. sm = “1,” sa = “0,” sb = “15,” sc = “15,” sd = “0,” se = “-15,” sf = “580” 
