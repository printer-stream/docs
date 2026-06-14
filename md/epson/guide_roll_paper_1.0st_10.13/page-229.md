## **C O N F I D E N T I A L** 

(*2) Processing According to Response Code (When Send Data Remains (indicated by identification status of send data group)) 

|send data group))||
|---|---|
|**Response code**|**Description**|
|ACK|Initiates operation to send next data.|
|NAK|Resends the just-received data.|
|CAN|Cancels processing initiated by this command.|



(*3) Processing According to Response Code (When No More Send Data Remains (indicated by identification status of send data group)) 

|**Response code**|**Description**|
|---|---|
|ACK, CAN|Cancels procedure initiated by this command.|
|NAK|Resends the just-received data.|



■ When codes other than the ACK, NAK, or CAN codes are received, the CAN procedure is executed. 
