Additional Connector Pin Allocations 

||RS-232-C||CCITTV.24 ||Function/Signal Level|
|---|---|---|---|
|1|AA|101|Protective ground|
|4|CA|105|RequestTo Send from the|
||||plotter|
||||Always High =ON = “0”|
||||=+12V|
|17|DD|115|External Clock Input|
||||High= ON = +2.4V to|
||||+5V|
||||Low=OFF = 0.0V to|
||||+0.4V|
|20|CD|108.2|DataTerminal Ready to|
||||modem|
||||High =ON = “0”|
||||=412V|
||||Low = OFF = “1”|
||||=-12V|
|14*|SBA|118|Secondary Transmit Data|
||||Data linefrom plotter to|
||||terminal|
|16*|SBB|119|Secondary Received Data|
||||Data line to plotter from|
||||terminal|



*Used to establish monitor mode with special Y-cable (Part No. 17455A). 

## Output Baud Rate 

The plotter is designed to operate in an asynchronous mode with switch-selectable baud rates of 75, 110, 150, 200, 300, 600, 1200, 2400, 4800, and 9600. See the 7470A Operator’s Manual for instructions on setting the baud rate. However, setting all BAUD switches to zero and connecting an external clock input to pin 17 of the connector allows operation of the plotter at any intermediate baud rate up to 9600 baud. Both the receiver (RRC) and transmitter (TRC) clocks will operate at the same clock rate. Requirements for the clock signal are as follows: 

1. The clock frequency must be 16 times the desired baud rate. 

2. The baud rate must not exceed 9600. 

3. The duty cycle of the clock pulse should be close to 50%. 

10-12 RS-232-C/CCITT V.24 INTERFACING 
