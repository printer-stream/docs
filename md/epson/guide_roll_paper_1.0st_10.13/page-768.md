## **C O N F I D E N T I A L** 

|**D E N T I A L**||||
|---|---|---|---|
|Separator|1FH|31|1 byte|
|Setting value (*2)|30H–39H|48–57|1–5 byte|
|NUL|00H|0|1 byte|



(*1) Communication condition transmits the value of a is converted into character data epressed by decimal numbers. Example: When [Communication condition] is the baud rate (a = 1), it is 1-byte data of “1” [Hexadecimal = 31H/Decimal = 49]. 

(*2) “Setting value” is set by Function 11. It might differ from the current communication condition before executing Function 2 or depending on the setting of the DIP switch. Example: When the baud rate is 9600 bps, it is 4-byte data of “9600” [Hexadecimal = 39H, 36H, 30H, 30H/Decimal = 57, 54, 48, 48]. 

■ This function is used to confirm whether Function 11 ends normally before executing Function 2. 

■ See previous [Notes for transmission process] for process sending data group. 
