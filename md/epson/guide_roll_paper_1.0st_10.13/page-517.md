## **C O N F I D E N T I A L** 

- When using parallel interface, the Bit 2 is fixed to 0 “DM-D (Customer display) is not connected.“ 

## <Second byte> 

|**Bit**|**Off/On **|**Hex**|**Decimal**|**Function**|**_... how to use_**<br>**_this table_**|
|---|---|---|---|---|---|
|0 ~ 5|-|-|-|Multi-byte code character (Kanji) is not supported.||
|6|On|40|64|Fixed.||
|7|Off|00|0|Fixed.||



<Third byte> 

|**Bit**|**Off/On **|**Hex**|**Decimal**|**Function**|**_... how to use_**<br>**_this table_**|
|---|---|---|---|---|---|
|0|Off|00|0|No peeler function available.||
||On|01|1|Peeler function available.||
|1 ~ 5|-|-|-|Reserved.||
|6|On|40|64|Fixed.||
|7|Off|00|0|Fixed.||



- When communication with the printer uses XON/XOFF control, the XOFF code may interrupt the “Header to NUL” data string. 

- The printer information A can be differentiated by the header of the block data from other transmission data. After outputting GS I, if the header transmitted from the printer is [Hex = 3DH/Decimal = 61], data is processed up to NUL [Hex = 00H/Decimal = 0] as the data block, according to the header and identifier. 
