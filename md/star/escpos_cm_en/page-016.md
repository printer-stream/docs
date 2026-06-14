Rev.2.52 

## **1-2-4 Data Reception Timing (Compatibility Mode)** 

**==> picture [424 x 217] intentionally omitted <==**

**----- Start of picture text -----**<br>
Data  Data  n  Data  n+1<br>tHold-1<br>nStrobe<br>tSetup  tSTB  tHold-2<br>Busy<br>Peripheral Busy<br>tReady  tBusy<br>nACK<br>tReply  tACK  tnBUSY<br>tNext<br>**----- End of picture text -----**<br>


|||**Standards**|**Standards**|
|---|---|---|---|
|||**Minimum[ns]**|**Maximum[ns]**|
|Data Hold Time(host)|tHold-1|-|500|
|Data Hold Time(printer)|tHold-2|-|-|
|Data SetupTime|tSetup|-|500|
|STROBE Pulse Width|tSTB|-|500|
|READY Cycle Idle Time|tReady|-|-|
|BUSY Output DelayTime|tBUSY|0|500|
|Data ProcessingTime|tReply|0|∞|
|ACKNLG Pulse Width|tACK|1usec/9usec(*1)|-|
|BUSY Cancel Time|tnBUSY|0|∞|
|ACK Cycle Idle Time|tNext|-|0|



(*1) Memory Switch Setting: ACK Pulse Width 

ON   = 9usec 

OFF = 1usec (Default) 

ESC/POS Command Specifications 

16 
