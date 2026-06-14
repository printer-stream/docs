## **C O N F I D E N T I A L** 

## **GS r** 

EXECUTING COMMAND 

[Name] Transmit status [Format] ASCII GS r n Hex 1D 72 n Decimal 29 114 n [Range] TM-J2000/J2100 **:** n **= 1, 2, 4, 49, 50, 52** 

TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-U230, TM-U220 **:** n **= 1, 2, 49, 50** TM-P60 **:** n **= 1, 49** 

- [Printers not featuring this command] None 

- [Description] Transmits the status using n as follows: 

|n|**Function**|
|---|---|
|1, 49|Transmits paper sensor status|
|2, 50|Transmits drawer kick-out connector status|
|4, 52|Transmits ink status|



## [Notes] 

## ■ Each status is 1 byte. 

## ■ The status to be transmitted is as follows: 

- Paper sensor status (n = 1, 49) 

|**Bit**|**Binary**|**Hex**|**Decimal**|**Status**|
|---|---|---|---|---|
|0, 1|00|00|0|Roll paper near-end sensor: paper adequate.|
||11|03|3|Roll paper near-end sensor: paper not present.|
|2, 3|00|00|0|Roll paper end sensor: paper present.|
||11|0C|12|Roll paper end sensor: paper not present.|
|4|0|00|0|Not used. Fixed to Off.|
|5,6|—|—|—|Undefined.|
|7|0|00|0|Not used. Fixed to Off.|



_**... how to use this table**_ 
