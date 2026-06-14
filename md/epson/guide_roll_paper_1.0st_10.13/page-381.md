## **C O N F I D E N T I A L** 

|m|**Bar code system**|**Bar code data (“SP” in the table indicates space.)**|**Bar code data (“SP” in the table indicates space.)**|**Bar code data (“SP” in the table indicates space.)**|**Bar code data (“SP” in the table indicates space.)**|
|---|---|---|---|---|---|
|||**Amount**<br>**of data**|**The range of**<br>k|**Characters**|**Data (**d**)**|
|2|JAN13 (EAN13)|Fixed|k= 12, 13|0~9|48≤ d ≤57|
|3|JAN8 (EAN8)|Fixed|k= 7, 8|0~9|48≤ d ≤57|
|4|CODE39|Can be changed|1≤ k|0~9, A~Z<br>SP, $, %, *, +, -, ., /|48 £  d £  57, 65 £  d £  90,<br>d= 32, 36, 37, 42, 43, 45, 46, 47|
|5|ITF<br>(Interleaved 2 of 5)|Can be changed|1≤ k(even<br>number)|0~9|48≤ d ≤57|
|6|CODABAR<br>(NW-7)|Can be changed|1≤ k|0~9, A~D, a~ d<br>$, +, -, ., /,:|48≤ d ≤57, 65≤ d ≤68, 97≤ d ≤<br>100<br>d= 36, 43, 45, 46, 47, 58<br>(65≤ d1 ≤68, 65≤ dk ≤68, 97≤<br>d1 ≤100, 97≤ dk ≤100)|



- k indicates the number of bytes of bar code data . k is an explanation parameter; therefore it does not need to be transmitted. 

- d specifies the character code data of the bar code data to be printed. 

## <Function B> 

|m|**Bar code system**|**Bar code data (“SP” in the table indicates space.)**|**Bar code data (“SP” in the table indicates space.)**|**Bar code data (“SP” in the table indicates space.)**|**Bar code data (“SP” in the table indicates space.)**|
|---|---|---|---|---|---|
|||**Amount**<br>**of data**|**The range of**<br>n|**Characters**|**Data (**d**)**|
|65|UPC-A|Fixed|n= 11, 12|0~9|48≤ d ≤57|
|66|UPC-E|Fixed|6≤ n ≤8<br>n= 11, 12|0~9|48≤ d ≤57 [However,d 1 = 48<br>whenn= 7, 8, 11, 12 is specified] )|
|67|JAN13 (EAN13)|Fixed|n= 12, 13|0~9|48≤ d ≤57|
|68|JAN8 (EAN8)|Fixed|n= 7, 8|0~9|48≤ d ≤57|
