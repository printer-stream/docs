## **C O N F I D E N T I A L GS ( k** <Function 182> 

- [Name] QR Code: Transmit the size information of the symbol data in the symbol storage area 

- [Format] 

   - ASCII GS ( k pL pH cn fn m Hex 1D 28 6B 03 00 31 52 m Decimal 29 40 107 3 0 49 82 m 

- [Range] (pL + pH × 256) = 3 (pL = 3, pH = 0 ) cn = 49 fn = 82 

   - m = 48 

- [Description] Transmits the size information for the encoded QR Code symbol data in the symbol storage area using the process of <Function 180>. 

- [Notes] ■ In standard mode, use this function when the printer is “at the beginning of a line,” or “there is no data in the print buffer.” 

## ■ The size information for each data is as follows; 

|**Send data**|**Hex**|**Decimal**|**Data**|
|---|---|---|---|
|Header|37H|55|1 byte|
|Identifier|36H|54|1 byte|
|Horizontal size(*1)|30H−39H|48−57|1−5 byte|
|Separator|1FH|31|1 byte|
|Vertical size(*1)|30H−39H|48−57|1−5 byte|
|Separator|1FH|31|1 byte|
|Fixed value|31H|49|1 byte|
|Separator|1FH|31|1 byte|
|Other information(*2)|30H or 31H|48 or 49|1 byte|
|NUL|00H|0|1 byte|
