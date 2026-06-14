## **C O N F I D E N T I A L** 

- Some paper sensors are not present, depending on the printer model. The names of some paper sensors are different, depending on the printer model. 

## ■ The status to be transmitted is as follows: 

- Drawer kick-out connector status (n = 2, 50) 

|**Bit**|**Binary**|**Hex**|**Decimal**|**Status**|
|---|---|---|---|---|
|0|0|00|0|Drawer kick-out connector pin 3 is LOW.|
||1|01|1|Drawer kick-out connector pin 3 is HIGH.|
|1-3|—|—|—|Undefined.|
|4|0|00|0|Not used. Fixed to Off.|
|5, 6|—|—|—|Undefined.|
|7|0|00|0|Not used. Fixed to Off.|



_**... how to use this table**_ 

## ■ The status to be transmitted is as follows: 

- Ink status (n = 2, 50) 

|**Bit**|**Binary**|**Hex**|**Decimal**|**Function**|
|---|---|---|---|---|
|0|0|00|0|Ink end not detected (1st color)|
||1|01|1|Ink end detected (1st color)|
|1|0|00|0|Ink end not detected (2nd color)|
||1|02|2|Ink end detected (2nd color)|
|2, 3|-|-|-|Undefined.|
|4|0|00|0|Not used. Fixed to Off.|
|5, 6|-|-|-|Undefined.|
|7|0|00|0|Not used. Fixed to Off.|



_**... how to use this table**_ 

## ■ When you use this command, obey the following rules. 
