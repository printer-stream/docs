## **C O N F I D E N T I A L** 

## **GS ( E** _**pL pH fn a**_ <Function 4> 

[Name] Transmit the settings of the memory switch 

- [Format] ASCII GS ( E pL pH fn _**a**_ Hex 1D 28 45 02 00 04 a Decimal 29 40 69 2 0 4 a 

- [Range] (pL + pH × 256) = 2 (pL = 2, pH = 0) fn = 4 

TM-J2000/J2100, TM-T90 **:** a **= 1, 2, 8** 

   - TM-L90 **:** a **= 1, 7, 8 (** TM-L90 **with Peeler)** a **= 1, 2, 8 (** TM-L90 **models without Peeler)** 

   - TM-P60 **:** a **=  8** TM-U220 **:** a **= 2, 8** TM-T20 **: 1** ≤ a ≤ **5** 

- [Description] 

   - Transmits the setting value of the memory switch specified by a. 

      - "ESC/POS transmission handshake" is unnecessary with this function. 

- [Notes] 

- This function works both in user setting mode and during normal printer operation. 

- The printer transmits the “Header to NUL” data shown below: 

|**Transmit data**|**Hex**|**Decimal**|**Data quantity**|
|---|---|---|---|
|Header|37H|55|1 byte|
|Identifier|21H|33|1 byte|
|Settingvalue|30H or 31H|48 or 49|8 byte|
|NUL|00H|0|1 byte|



- The value of the memory switch is transmitted from bit 8 to bit 1. 

Example: The transmit data when bits 8 and 7 are On and the other bits are Off is 11 bytes of [Hexadecimal = 37H, 21H, 31H, 31H, 30H, 30H, 30H, 30H, 30H, 30H, 00H/Decimal = 55, 33, 49, 49, 48, 48, 48, 48, 48, 48, 0]. 

- See description of <Function 3> of this command for details of memory switch. 

- See [Notes for the processing to transmit data] for description of the processing to transmit data. 
