Rev.2.52 

## **1-1-4 Timing for Transmitting XON/XOFF** 

When XON/XOFF control is selected, XON and XOFF are transmitted with the following timings. The transmission timing varies according to the DIP switch settings or the memory switch settings. XON code: <11> H 

XOFF code: <13> H 

For (3) below, XON is not transmitted when the reception buffer is full. For (6) below, XOFF is not transmitted when the reception buffer is full. 

## **<XON/XOFF Transmission Timing>** 

||**Printer Status**|**Busy condition(*1)**|**Busy condition(*1)**|
|---|---|---|---|
|||OFF|ON|
|XON<br>Transmission|(1) When online for the frst time after turning the power<br>on or a reset using the interface<br>(2) When the bufer full status was cancelled for recep-<br>tion bufer<br>(3) When shifting from ofine to online<br>(4) When recovered from a recoverable error using a<br>command|Transmission<br>Transmission<br>-<br>-|Transmission<br>Transmission<br>Transmission<br>Transmission|
|XOFF<br>Transmission|(5) When the reception bufer entered bufer full status<br>(6) When shifting from online to ofine|Transmission<br>-|Transmission<br>Transmission|



## (*1) DIPSW Settings: Conditions for BUSY 

ON = Reception buffer full or printer is offline (Default) OFF = Reception buffer full 

## **1-1-5 Serial Interface Connection Example** 

• If the other connected party is DCE, be careful so that there is no status without a handshake (where data is flows)  (DTE: Data Terminal Equipment; DCE: Data Circuit Terminating Equipment) • When transmitting data to the printer, turn on the power to the printer and initialize first. 

|Host<br>TXD<br>DSR<br>CTS<br>RXD<br>DTR<br>F.G<br>S.G|Printer<br>TXD<br>DTR<br>RTS<br>RXD<br>DSR<br>F.G<br>S.G|
|---|---|



ESC/POS Command Specifications 

11 
