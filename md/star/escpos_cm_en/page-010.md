Rev.2.52 

## **1-1-3 Signal Array and Explanations According to Interface Connector Pin** 

<Signal Array and Functions> 

|**Pin**<br>**No.**|**Signal**<br>**Name**|**Signal**<br>**Dir.**|**Function**|
|---|---|---|---|
|1|FG|-|Frameground|
|2|TXD|Output|Transmission Data|
|3|RXD|Input|Reception Data|
|4|RTS|Output|Same as DTR signal|
|6|DSR|Input|Signal indicating whether host can receive data.<br>The SPACE status indicates the host can receive data; the MARK status indicates that the host<br>cannot receive data.  When DTR/DSR control is selected, the status of this signal is checked to<br>transmit data.   (Excludes data transmissions using DLEEOT .)<br>When XON/XOFF control is selected, the status of this signal is not checked.  This signal can<br>be used to reset the printer according by switching the DIP switches or the memory switches.|
|7|SG|-|Signal ground|
|20|DTR|Output|(1) When DTR/DSR control is selected:<br>Indicates whether the printer is BUSY.<br>The SPACE status indicates the printer is READY; the MARK status indicates that the printer<br>is BUSY.<br>The DIP switch or the memory switch settings change the conditions for the printer to be BUSY.<br>(*1)<br>The following conditions are required to enter aBUSY (MARK)state.<br>(2) XON/XOFF control is selected:<br>Indicates whether the printer is connected normally and is ready to receive data from the host.<br>A SPACE status indicate that the printer is connected normally and that data can be received.<br>The SPACE status is always entered except for the following cases.<br>• The time after initializing the mechanism when turning on the power until communication is<br>possible.<br>• While executinga self-test<br>Printer Status<br>Busycondition(*1)<br>OFF<br>ON<br>• During the period from when the power is turned<br>on (including resetting using the interface) to<br>when the printer is ready to receive data.<br>BUSY<br>BUSY<br>• When executing a self-test<br>BUSY<br>BUSY<br>• When the cover is open<br>-<br>BUSY<br>• When printing stopped because of paper out<br>-<br>BUSY<br>• When waiting to switch at macro execution<br>-<br>BUSY<br>• While there is a temporary error in the power<br>-<br>BUSY<br>• When there is an error<br>-<br>BUSY<br>• When reception bufer is full(*2)BUSY<br>BUSY<br>BUSY<br>OFFLINE|
|25|INIT|Input|This signal can be used to reset the printer according by switching the DIP switches or the<br>memoryswitches.|



## (*1) DIPSW Settings: Conditions for BUSY 

ON = Reception buffer full or printer is offline  (Default) OFF = Reception buffer full (*2) When the reception buffer empty region is 0 bytes, received data is ignored. 

ESC/POS Command Specifications 

10 
