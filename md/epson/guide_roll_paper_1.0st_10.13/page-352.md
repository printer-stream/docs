## **C O N F I D E N T I A L** 

## ■ Third byte (paper sensor information) 

|**Bit**|**Binary**|**Hex**|**Decimal**|**Status for ASB**|
|---|---|---|---|---|
|0, 1|00|00|0|Roll paper near-end sensor: paper adequate.|
||11|03|3|Roll paper near-end sensor: paper near end.|
|2, 3|00|00|0|Roll paper end sensor: paper present.|
||11|0C|12|Roll paper end sensor: paper not present.|
|4|0|00|0|Not used. Fixed to Off.|
|5,6|—|—|—|Undefined|
|7|0|00|0|Not used. Fixed to Off.|



_**... how to use this table**_ 

   - Some paper sensors are not present, depending on the printer model. The names of some paper sensors are different, depending on the printer model. 

- Fourth byte (paper sensor information) 

|**Bit**|**Binary**|**Hex**|**Decimal**|**Status for ASB**|**_... how to use_**<br>**_this table_**|
|---|---|---|---|---|---|
|0-3|—|—|—|Undefined||
|4|0|00|0|Not used. Fixed to Off.||
|5,6|—|—|—|Undefined||
|7|0|00|0|Not used. Fixed to Off.||



- During Block data [header - NUL] transmission, ASB is disabled temporarily. Therefore you cannot get the printer status change through ASB status when block data [header - NUL] is transmitted. 

- With a serial interface, the printer transmits a 4-byte ASB status message without confirming whether the host can receive data. 

- With a parallel interface, when ASB status is used, it is desirable for the host to be in a reverse idle state. However, if the host computer cannot always be in the reverse idle state, it is necessary to enter Reverse Mode regularly to watch for ASB status. If the host is not in the Reverse Mode for a long time, and the 
