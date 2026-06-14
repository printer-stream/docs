## **C O N F I D E N T I A L** 

- When communication with the printer uses XON/XOFF control with serial interface, the XOFF code may interrupt the “Header to NUL” data string. 

- The information for each function can be identified to other transmission data according to specific data of the transmission data block. When the header transmitted by the printer is [hex = 37H/decimal =55], treat NUL [hex = 00H/decimal =0] as a data group and identify it according to the combination of the header and the identifier. 

## [Notes for ESC/POS Handshaking Protocol] 

- It will be necessary to perform the ESC/POS Handshaking Protocol procedures listed below when using Functions 64 and 80. 

|**Procedure **|**Host operation**|**Printer operation**|
|---|---|---|
|1|This command sends<br>Function 64.|Function 64 is initiated.|
|2|Data is received from printer.|Key code list is sent.|
|3|Response code (*1) is sent.|Procedures (*2 and *3) are performed<br>according to response code.|



## (*1) Response Code 

|**ASCII**|**Hexadecimal**|**Decimal**|**Request definition**|
|---|---|---|---|
|ACK|06|6|Send next data group.|
|NAK|15|21|Resend just-received data group.|
|CAN|18|24|Cancel send operation.|
