Appendix 

## Functions of each connector pin 

|Pin no.|Signal name|Signal direction|Function|
|---|---|---|---|
|1|FG|—|Frame ground|
|2|TXD|Output|Transmission data|
|3|RXD|Input|Reception data|
|4|RTS|Output|Equivalent to DTR signal (pin 20)|
|6|DSR|Input|This signal indicates whether the host computer can<br>receive data.<br>SPACE indicates that the host computer can receive<br>data. MARK indicates that the host computer<br>cannot receive data.<br>When DTR/DSR control is selected, the printer<br>transmits data after confirming this signal (except if<br>transmitted using some ESC/POS commands).<br>When XON/XOFF control is selected, the printer does<br>not check this signal.<br>Changing DIP switch 2-7 lets this signal be used as a<br>printer reset signal.<br>When you use this signal as the printer’s reset signal,<br>the printer is reset when the signal remains MARK for<br>a pulse width of 1 ms or more.|
|7|SG|—|Signal ground|
|20|DTR|Output|1) When DTR/DSR control is selected, this signal<br>indicates whether the printer is BUSY.<br>• SPACE status<br>Indicates that the printer is ready to receive data.<br>• MARK status<br>Indicates that the printer is BUSY. Set BUSY conditions<br>with DIP switch 2-1.<br>2) When XON/XOFF control is selected, the signal<br>indicates that the printer is properly connected and<br>ready to receive data from the host. The signal is<br>always SPACE, except in the following cases:<br>• During the period from when power is turned on to<br>when the printer is ready to receive data.<br>• During the self-test.|
|25|INT|Input|Changing DIP switch 2-8 enables this signal to be<br>used as a reset signal for the printer. The printer is<br>reset if the signal remains at SPACE for a pulse width<br>of 1 ms or more.|



**105** 
