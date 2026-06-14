## **C O N F I D E N T I A L GS ( k** <Function 482> 

- [Name] Composite Symbology: Transmit the size information of the symbol data in the symbol storage area 

- [Format] ASCII GS ( k pL pH cn fn m Hex 1D 28 6B 03 00 34 52 30 Decimal 29 40 107 3 0 52 82 48 

- [Range] (pL + pH × 256) = 3 (pL = 3, pH = 0 ) cn = 52 fn = 82 

   - m = 48 

- [Description] Transmits the size information for the encoded Composite Symbology in the symbol storage area using the process of <Function 480>. 

- [Notes] ■ In standard mode, use this function when the printer is “at the beginning of a line,” or “there is no data in the print buffer.” 

   - Size information is the size of the symbol that is printed by <Function 481> of this command, and is the sum of the following data. 

      - Line element and 2D composite element 

      - Line element and 2D composite element separator 

      - When HRI characters are designated to be added, the height of the HRI characters and the space between the symbol and HRI characters 

## ■ The size information for each data is as follows; 

|**Send data**|**Hex**|**Decimal**|**Data**|
|---|---|---|---|
|Header|37H|55|1 byte|
|Identifier|50H|80|1 byte|
|Horizontal size(*1)|30H−39H|48−57|1−5 byte|
|Separator|1FH|31|1 byte|
|Vertical size(*1)|30H−39H|48−57|1−5 byte|
