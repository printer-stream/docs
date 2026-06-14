## **C O N F I D E N T I A L** 

## **ESC u** 

EXECUTING COMMAND 

[Name] Transmit peripheral device status [Format] ASCII ESC u n Hex 1B 75 n Decimal 27 117 n 

[Range] n = 0, 48 

[Printers not featuring this command] TM-J2000/J2100, TM-T90, TM-L90, TM-P60, TM-U230 [Description] Transmits the peripheral device status as 1 byte of data. 

[Recommended Functions] 

This command is supported only by some printer models but will not be supported by future models. It is recommended to use GS r 2 to check the status and GS r to transmit the peripheral device status. 

## [Notes] 

■ ESC u is not a recommended command. ESC u will not be included in future products. ■ The peripheral device status to be transmitted is as follows: 

|**Bit**|**Binary**|**Hex**|**Decimal**|**Status**|
|---|---|---|---|---|
|0|0|00|0|Drawer kick-out connector pin 3 is LOW.|
||1|01|1|Drawer kick-out connector pin 3 is HIGH.|
|1-3|—|—|—|Undefined.|
|4|0|00|0|Not used. Fixed to Off.|
|5, 6|—|—|—|Undefined.|
|7|0|00|0|Not used. Fixed to Off.|



_**... how to use this table**_ 

[Model-dependent variations] None 

## **Program Example for all printers** 

PRINT #1,CHR$(&h1B);"u";CHR$(0); 
