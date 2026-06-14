## **C O N F I D E N T I A L GS ( k** <Function 382> 

- [Name] 2-dimensional GS1 DataBar: Transmit the size information of the symbol data in the symbol storage area 

- [Format] 

   - ASCII GS ( k pL pH cn fn m Hex 1D 28 6B 03 00 33 52 30 Decimal 29 40 107 3 0 51 82 48 

- [Range] (pL + pH × 256) = 3 (pL = 3, pH = 0 ) cn = 51 fn = 82 

   - m = 48 

- [Description] Transmits the size information for the encoded 2-dimensional GS1 DataBar symbol data in the symbol storage area using the process of <Function 380>. 

- [Notes] ■ In standard mode, use this function when the printer is “at the beginning of a line,” or “there is no data in the print buffer.” 

   - Size information of this command  shows the size of the  symbol which is printed with <Function 381>. 

   - The size information for each data is as follows: 

|**Send data**|**Hex**|**Decimal**|**Data**|
|---|---|---|---|
|Header|37H|55|1 byte|
|Identifier|4FH|79|1 byte|
|Horizontal size(*1)|30H−39H|48−57|1−5 byte|
|Separator|1FH|31|1 byte|
|Vertical size(*1)|30H−39H|48−57|1−5 byte|
|Separator|1FH|31|1 byte|
|Fixed value|31H|49|1 byte|
