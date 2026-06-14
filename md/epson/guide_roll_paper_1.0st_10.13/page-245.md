## **C O N F I D E N T I A L** 

(*2) If the number of NV graphics data groups is 40 or less, they are sent in a single batch, with the Identification status byte (byte 3) set to hexadecimal value 40H and decimal value 64. 

(*3) The data groups are arranged according to the key codes. 

■ When no key codes are present, the data shown below (beginning with Header and ending with NUL) is sent. 

|sent.||||
|---|---|---|---|
|**Send data**|**Hexadecimal**|**Decimal**|**Data length**|
|Header|37H|55|1 byte|
|Identifier|72H|114|1 byte|
|Identification status|40H|64|1 byte|
|NUL|00H|0|1 byte|



- Do not use this function in conjunction with NV bit images (FS q). 

- See previous [Notes for transmission process] for process sending data group. 

- See previous [Notes for ESC/POS Handshaking Protocol] for ESC/POS Handshaking Protocol. 
