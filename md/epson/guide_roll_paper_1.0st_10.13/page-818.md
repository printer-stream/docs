## **C O N F I D E N T I A L FS ( L** _**pL pH fn n**_ <Function 34> 

[Name] 

[Format] 

Paper layout information transmission 

ASCII FS ( L pL pH fn n Hex 1C 28 4C _02 00 22_ n Decimal 28 40 76 _2 0 34_ n 

[Range] (pL + pH × 256) = 2 (pL = 2, pH = 0) fn = 34 

- n = 64,80 

[Description] 

Transmits paper layout information specified by n. 

|n|Paper layout information type|
|---|---|
|64|Paper layout setting value (unit: 0.1 mm)|
|80|Paper layout effective value (unit: dots)|



## [Notes] 

## ■ With this function, the [Header - NUL] shown below is transmitted. 

|**Transmission data**|**Hex**|**Decimal**|**Amount of data**|
|---|---|---|---|
|Header|37H|55|1 byte|
|Identifier|4BH|76|1 byte|
|Information type(*1)|30H - 39H|48 - 57|2 bytes|
|Separator|1FH|31|1 byte|
|Layout information(*2)||||
|Layout reference (sm)|30H - 33H|48 - 51|0 or 1 byte|
|Separator|1FH|31|1 byte|
|Vertical layout (sa)|30H - 39H|48 - 57|0 - 5 bytes|
|Separator|1FH|31|1 byte|
