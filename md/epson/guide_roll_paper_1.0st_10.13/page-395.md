## **C O N F I D E N T I A L** 

[Model-dependent variations] 

TM-J2000/J2100, TM-T90, TM-L90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-P60 

## TM-J2000/J2100 

**With UPC-E (** m **= 1, 66), 11 or 12 bytes can be used for the amount of data to process. Only capital letters (ASCII = A ~ D/Hexadecimal = 41H ~ 44H/Decimal = 65 ~ 68) can be used for the start/stop character with CODABAR (** m **= 6, 71).** 

## TM-T90, TM-L90 

**With UPC-E (** m **= 1, 66), 11 or 12 bytes can be used for the amount of data to process.** 

**Only capital letters (ASCII = A ~ D/Hexadecimal = 41H ~ 44H/Decimal = 65 ~ 68) can be used for the start/stop character with CODABAR (** m **= 6, 71).** 

**When printing ladder bar code (bar code rotated by 90 degrees in page mode) the printer starts actual printing after it reaches control speed for printing ladder bar code. It is needed to feed paper amount of 10 dots or less in this operation.** 

**If the memory switch [Msw 8-5] is ON, the printer inserts a space data automatically. Therefore, the print area is [bar code data + space of the dots as following table] when executing this command.** 

|**command.**||||
|---|---|---|---|
|**Model**|**Right spacing **|**Left spacing **|**Notes**|
|**TM-T90 (other than Japanese model) **|**15 dots**|**15 dots**|**15 dots = approximately 2.12 mm**<br>**[15/180 inch]**|
|**TM-T90 (Japanese model)**|**19 dots**|**19 dots**|**19 dots = approximately 2.38 mm**<br>**[19/180 inch]**|
|**TM-L90**|**19 dots**|**19 dots**|**19 dots = approximately 2.38 mm**<br>**[19/180 inch]**|
