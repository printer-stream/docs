## **C O N F I D E N T I A L** 

## [Note] Only if ESC 4 is selected or paper stop printing sensor is not selected. 

- Basic ASB status is 4-byte configuration [first byte - fourth byte]. 

- The status to be transmitted are as follows: 

- First byte (printer information) 

|**Bit**|**Binary**|**Hex**|**Decimal**|**Status for ASB**|
|---|---|---|---|---|
|0|0|00|0|Not used. Fixed to Off.|
|1|0|00|0|Not used. Fixed to Off.|
|2|0|00|0|Drawer kick-out connector pin 3 is LOW.|
||1|04|4|Drawer kick-out connector pin 3 is HIGH.|
|3|0|00|0|Online.|
||1|08|8|Offline.|
|4|1|10|16|Not used. Fixed to On.|
|5|0|00|0|Cover is closed.|
||1|20|32|Cover is open.|
|6|0|00|0|Paper is not being fed by the paper feed button.|
||1|40|64|Paper is being fed by the paper feed button.|
|7|0|00|0|Not used. Fixed to Off.|



_**... how to use this table**_ 

## ■ Second byte (printer information) 

|**Bit**|**Binary**|**Hex**|**Decimal**|**Status for ASB**|
|---|---|---|---|---|
|0|0|00|0|Not waiting for online recovery.|
||1|01|1|Waiting for online recovery.|
|1|0|00|0|Paper feed button is not pushed (off)|
||1|02|2|Paper feed button is pushed (on)|



_**... how to use this table**_ 
