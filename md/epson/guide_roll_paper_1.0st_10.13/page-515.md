## **C O N F I D E N T I A L** 

- With a parallel interface printer, data (printer ID, printer information) sent with this command is temporarily stored in the printer send buffer like other transmitted data (except ASB). When the host goes into reverse mode, the printer then sends the data sequentially from the beginning of the send buffer. Send buffer capacity is 99 bytes. Data exceeding this amount is lost; therefore, when using this command, promptly change into reverse mode to start the data receive process. 

## [Notes for printer ID] 

- Each printer ID is composed of 1 byte of data (when 1 ≤ n ≤ 3, 49 ≤ n ≤ 51). 

- Printer model ID differs, depending on the printer model (when n = 1, 49). 

## ■ Transmits specified printer information, as follows: 

|**Bit**|**Off/On**|**Hex**|**Decimal**|**Function**|
|---|---|---|---|---|
|0|Off|00|0|Multi-byte character codes are not<br>supported.|
||On|01|1|Multi-byte character codes are supported.|
|1|Off|00|0|Autocutter not installed.|
||On|02|2|Autocutter installed.|
|2|Off|00|0|DM-D (customer display) is not installed.|
||On|04|4|DM-D (customer display) is installed.|
|3|--|--|--|Reserved.|
|4|Off|00|0|Not used. Fixed to Off.|
|5|--|--|--|Reserved.|
|6|Off|00|0|E/P (Endorse printer) not installed|
|7|Off|00|0|Not used. Fixed to Off.|



## _**... how to use this table**_ 

   - For the parallel interface model, bit2 is “DM-D (customer display) is not installed.” 

- There is a one to one correspondence between the version ID and the firmware version when n = 3, 51. The details differ, depending on the printer model. 
