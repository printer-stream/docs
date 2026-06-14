## **C O N F I D E N T I A L FS ( L** <Function 48 > 

[Name] Transmit the positioning information 

[Format] 

ASCII FS ( L pL pH fn m Hex 1C 28 4C 02 00 30 m Decimal 28 40 76 2 0 48 m 

[Range] (pL + pH × 256) = 2 (pL = 2, pH = 0) m = 48 fn = 80 

- [Description] Transmits the positioning information for the label or black mark paper. 

[Notes] ■ Header to NUL shown in the following is transmitted in this function. 

|**Transmission data**|**Hex**|**Decimal**|**Number of data**|
|---|---|---|---|
|Header|37H|55|1 byte|
|Identifier|38H|56|1 byte|
|Position information A|40H to 7FH|64 to 127|1 byte|
|Position information B|40H to 7FH|64 to 127|1 byte|
|NUL|00H|0|1 byte|
