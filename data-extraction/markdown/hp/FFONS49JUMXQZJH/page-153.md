## Minimum Interface Connector Pin Allocations

|   Pin No. | RS-232-C   |   CCITTV.24 | Function/ Signal Level                                                              |
|-----------|------------|-------------|-------------------------------------------------------------------------------------|
|         2 | BA (TDATA) |         103 | Data line from plotter High = ON = '0' = +12 V = SPACE Low = OFF = '1'= -12V = MARK |
|         3 | BB (RDATA) |         104 | Data line to plotter High = ON = 'O'= +3 V to +25 V Low= OFF = '1'= -3 V to -25 V   |
|         7 | AB (SGND)  |         102 | Signal ground (Return line)                                                         |

In addition to the minimum requirements for communication, six more lines are connected as shown in the following table. These lines are required to implement full duplex communication, intermediate baud rate, hardwired handshake mode, and monitor mode. All remaining pins make no internal connection.

Pins 14 and 16 are wired in the special Y-cable, available as Option 16, to implement monitor mode. The Y-cableschematic is shown below.

NOTE:Hardwire handshake cannot be used to prevent buffer overflow when the Y-cable is connected. This is because pin 20 is connected between the COMPUTER and TERMINAL connectors, but not to the PLOTTER connector. I

PINS 4, 5, 6, AND 8 THROUGH 25 ARE DIRECTLY CONNECTED BETWEEN THE COMPUTER AND TERMINAL CONNECTORS.

<!-- image -->

Y-cableSchematic
