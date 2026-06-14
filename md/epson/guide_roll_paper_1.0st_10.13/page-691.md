## **C O N F I D E N T I A L** 

## **GS ( C** _**pL pH m fn b**_ <Function 3> 

[Name] Transmit capacity of the NV user memory currently being used 

- [Format] 

## [Range] 

   - ASCII GS ( C pL pH m fn b Hex 1D 28 43 03 00 00 fn 00 Decimal 29 40 67 3 0 0 fn 0 (pL + pH × 256) = 3 (pL = 3, pH = 0) 

   - m = 0 fn = 3, 51 b = 0 

- [Description] Transmits the number of bytes of memory used in the NV user memory. 

      - ESC/POS Handshaking Protocol is not required for this function. 

## [Notes] 

- With this function, the printer sends the “Header to NUL” data shown below: 

|**Send data**|**Hex**|**Decimal**|**Data quantity**|
|---|---|---|---|
|Header|37H|55|1 byte|
|Identifier|28H|40|1 byte|
|Capacity Used(*1)|30H−39H|48−57|1−8 bytes|
|NUL|00H|0|1 byte|



- (*1) The quantity of stored data bytes, plus the key code and terminator, equal the capacity being used. The decimal value expressing the capacity being used is converted to ASCII character data and sent from the most significant digit. 

## Example: 

When 120 bytes is used, the number 120 is expressed with three bytes of data (Hexadecimal: 31H, 32H, and 30H / decimal numbers 49, 50, and 48). 

When no memory area is used, the number 0 is expressed with 1 byte of data (Hexadecimal: 30H / decimal number 48). 

- The control information for NV graphics data is included in the capacity in use. 

■ See previous [Notes for transmission process] for process sending data group. 
