## **C O N F I D E N T I A L** 

- Transmits specified printer information A, using n as follows: 

|n|**Printer ID**|**Specification**|
|---|---|---|
|33|Type information|Supported functions|
|35, 96,<br>110|See [Printer information]|See [Printer information]|



## • Transmits specified printer information B, using n as follows: 

|n|**Printer ID**|**Specification**|
|---|---|---|
|65|Firmware version|Firmware version|
|66|Maker name|“EPSON”|
|67|Printer model|Printer model|
|68|Serial No|Serial No of the printer|
|69|Font of Language for each country|Japanese model: “KANJI JAPANESE”|
|||Simplified Chinese model: “CHINA<br>GB2312” or “CHINA GB18030”|
|||Traditional Chinese model: “TAIWAN<br>BIG-5”|
|||Korean model: “KOREA C-5601C”|
|||South Asia model: “THAI 1 PASS”|
|111|See model-dependent variations|See model-dependent variations|
|112|See model-dependent variations|See model-dependent variations|



## [Notes] 

## ■ When you use this command, obey the following rules. 

- When the host PC transmits the function data, transmit next data after receiving the corresponding ID from the printer. 

- With a serial interface printer, be sure to use this function when the host can receive data. 
