## **C O N F I D E N T I A L** 

- Roll paper sensor status (n = 4) is as follows: 

|**Bit**|**Off/On**|**Hex**|**Decimal**|**Status**|**_... how to use_**<br>**_this table_**|
|---|---|---|---|---|---|
|0|0|00|0|Not used. Fixed to Off.||
|1|1|02|2|Not used. Fixed to On.||
|2, 3|00|00|0|Roll paper near-end sensor: paper adequate.||
||11|0C|12|Roll paper near-end sensor: paper near end.||
|4|1|10|16|Not used. Fixed to On.||
|5, 6|00|00|0|Roll paper end sensor: paper present.||
||11|60|96|Roll paper end sensor: paper not present.||
|7|0|00|0|Not used. Fixed to Off.||



- Some paper sensors are not present, depending on the printer model. The names of some paper sensors are different, depending on the printer model. 
