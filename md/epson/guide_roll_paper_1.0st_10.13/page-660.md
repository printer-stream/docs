## **C O N F I D E N T I A L** 

## [Notes for UPC-E (0 not omitted (11 digits) version)] 

   - Transmit the data except for the modular check character from the host. 

   - The first data (d1) is processed as a number system character (NSC). Always specify 0. 

- [Notes for GS1 DataBar Omnidirectional, GS1 DataBar Truncated, GS1 DataBar Stacked, GS1 DataBar Stacked Omnidirectional, and GS1 DataBar Limited] 

   - Transmit the 13-digit product identification number, excluding the application identifier (AI) and check digit, from the host. 

## [Notes for GS1 DataBar Expanded] 

- Transmit the 2-byte data shown in the following table ([Hexadecimal = 7BH / Decimal = 123] + character code) from the host for the special character (FNC1) and symbol data "(", ")". ("+" in the table is not included in the transmission data)] 

|**Data**|**Transmission data from host**|**Transmission data from host**|**Transmission data from host**|
|---|---|---|---|
||**ASCII**|**Hexadecimal**|**Decimal**|
|FNC1|{ + 1|7B + 31|123 + 49|
|(|{ + (|7B + 28|123 + 40|
|)|{ + )|7B + 29|123 + 41|



- The special characters ("(", ")") have the functions shown in the table below. 

|■The special characters ("(", ")") have the functions shown in the table below.|■The special characters ("(", ")") have the functions shown in the table below.|■The special characters ("(", ")") have the functions shown in the table below.|■The special characters ("(", ")") have the functions shown in the table below.|
|---|---|---|---|
|**Special characters**||||
|**Characters**|**Hexadecimal**|**Decimal**|**Functions**|
|(|28|40|Each character is inserted for the HRI character. It makes<br>the HRI characters look nice when used to enclose the AI.<br>The data does not constitute encoded data.|
|)|29|41||
