Minimum Interface Connector Pin Allocations 

||RS-232-C||CCITTV.24|||Function/Signal Level|
|---|---|---|---|---|
|2|BA|103||Data line from plotter|
||(TDATA)|||High =ON= “0” =+12V|
|||||=SPACE|
|||||Low = OFF = “1” = -12 V|
|||||= MARK|
|3|BB|104||Data line to plotter|
||(RDATA)|||High =ON = “0” =+3V|
|||||to +25 V|
|||||Low = OFF = “1” =-3 V|
|||||to —25 V|
|7|AB|102||Signal ground (Return|
||(SGND)|||line)|



In addition to the minimum requirements for communication, six more lines are connected as shown in the following table. These lines are required to implement full duplex communication, intermediate baud rate, hardwired handshake mode, and monitor mode. All remaining pins make no internal connection. 

Pins 14 and 16 are wired in the special Y-cable, available as Option 16, to implement monitor mode. The Y-cable schematic is shown below. 

NOTE: Hardwire handshake cannot be used to prevent buffer overflow when the Y-cable is connected. This is because pin 20 is connected between the COMPUTER and TERMINAL connectors, but not to the PLOTTER connector. Hf 

**==> picture [318 x 164] intentionally omitted <==**

**----- Start of picture text -----**<br>
comms PDL EEE)<br>|<br>|<br>att3 ||<br>|<br>rept !|<br>notre a, aL<br>reswnae[> [>][+Ts[<br>PINS oe<br>4,5, 6, AND 8 THROUGH 25 ARE DIRECTLY CONNECTED BETWEEN THE<br>COMPUTER AND TERMINAL CONNECTORS.<br>**----- End of picture text -----**<br>


Y-cable Schematic 

RS-232-C/CCITT V.24 INTERFACING 10-11 
