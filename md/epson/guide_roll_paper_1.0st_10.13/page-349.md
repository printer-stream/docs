## **C O N F I D E N T I A L** 

## ■ The basic ASB statuses, corresponding to each bit for n are as follows: 

|n|n|**ASB status**|**ASB status**|
|---|---|---|---|
|**Bit**|**Function**|**Bit**|**Status**|
|0|Drawer kick-out<br>connector status.|Bit 2 of the first byte|Drawer kick-out connector<br>pin 3 status.|
|1|Online/offline<br>status.|Bit 3 of the first byte|Online/ offline status.|
|||Bit 5 of the first byte|Cover status.|
|||Bit 6 of the first byte|Paper is being fed by paper<br>feed button status.|
|||Bit 0 of the second byte|Waiting for online recovery<br>status.|
|||Bit 0 and 1 of the third byte<br>[Note]|Roll paper near-end sensor<br>status.|
|||Bit 2 and 3 of the third byte<br>[Note]|Roll paper end sensor status.|
|2|Error status.|Bit 2 of the second byte|Recoverable error status.|
|||Bit 3 of the second byte|Autocutter error status.|
|||Bit 5 of the second byte|Unrecoverable error status.|
|||Bit 6 of the second byte|Automatically recoverable<br>error status.|
|3|Roll paper sensor<br>status.|Bits 0 and 1 of the third byte|Roll paper near-end sensor<br>status.|
|||Bits 2 and 3 of the third byte|Roll paper end sensor status.|
|6|Panel switch<br>status.|Bit 1 of the second byte|Paper feed status|



_**... how to use this table**_ 
