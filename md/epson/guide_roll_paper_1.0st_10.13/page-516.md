## **C O N F I D E N T I A L** 

■ Printer ID is distinguished from other send data by bits 4 and 7. When the data sent from printer after printing GS I is "0xx0xxxx" (x = 0, 1), the printer processes the data as printer ID. 

[Notes for printer information A] 

- Printer information A (n = 33, 96) consists of [Header ~ NUL] as shown in the following table: 

|**Transmitted data**|**Hex**|**Decimal**|**Data quantity**|
|---|---|---|---|
|Header|3DH|61|1 byte|
|Identifier(*1)|20H ~ 2FH|32 ~ 47|1 byte|
|Printer information A|Depends on printer model|Depends on printer model|0 ~ 80 bytes|
|NUL|00H||1 byte|



(*1) The identifier is transmitted as the transmitted parameter n of this command. 

Example: When type information is specified (n = 33), the identifier is [hex = 21H/decimal = 33]. 

The printer information A of type information (n = 33) is either 1-byte of [First byte], 2 bytes of [First byte] and [Second byte], or 3 bytes of [First byte] to [Third byte] depending on the modes. 

<First byte>. 

|**Bit**|**Off/On **|**Hex**|**Decimal**|**Function**|**_... how to use_**<br>**_this table_**|
|---|---|---|---|---|---|
|0|Off|00|0|Multi-byte code character (Kanji) is not<br>supported.||
||On|01|1|Multi-byte code character (Kanji) is supported.||
|1|Off|00|0|Autocutter is not installed.||
||On|02|2|Autocutter is installed.||
|2|Off|00|0|DM-D (Customer display) is not connected.||
||Off|04|4|DM-D (Customer display) is connected.||
|3 ~ 5|-|-|-|Reserved.||
|6|On|40|64|Fixed.||
|7|Off|00|0|Fixed.||
