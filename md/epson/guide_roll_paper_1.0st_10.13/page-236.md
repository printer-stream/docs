## **C O N F I D E N T I A L GS ( L** _**pL pH m fn**_ <Function 48> 

[Name] Transmit the NV graphics memory capacity. 

- [Format] 

ASCII GS ( L pL pH m fn Hex 1D 28 4C 02 00 30 fn Decimal 29 40 76 2 0 48 fn 

- [Range] (pL + pH × 256) = 2 (pL = 2, pH = 0) m = 48 fn = 0, 48 

- [Description] Transmits the entire capacity of the NV graphics area (number of bytes in the NV graphics area). 

   - This function does not require ESC/POS Handshaking Protocol. 

[Notes] 

- This function is used to send the following data groups, beginning with the Header and ending with NUL. 

|**Send data**|**Hexadecimal**|**Decimal**|**Data length**|
|---|---|---|---|
|Header|37H|55|1 byte|
|Identifier|30H|48|1 byte|
|Entire capacity(*1)|30H to 39H|48 to 57|1 to 8 bytes|
|NUL|00H|0|1 byte|



(*1) The entire capacity is the total byte count for that domain. The decimal value for the entire capacity is converted to text data and sent starting from the high order end. 

Example: 

If the entire capacity is 1200 bytes, the “1200” (expressed hexadecimally as 31H, 32H, 30H, and 30H, decimally as 49, 50, 48, and 48) is converted to 4-byte data. 

- When this function is used to send the entire capacity, the entire byte capacity of the domain is sent, regardless of definitions currently entered for NV graphics data. The entire capacity referred to here includes the area used for control information. 

- Note that the NV graphics function cannot be used when the value for the entire capacity is “0” (expressed hexadecimally as 30H and decimally as 48). 

- See previous [Notes for transmission process] for process sending data group. 
