Additional Connector Pin Allocations

| Pin No.   | RS-232-C   |   CCITT V.24 | Function/ Signal Level                                                 |
|-----------|------------|--------------|------------------------------------------------------------------------|
|           | AA         |          101 | Protective ground                                                      |
|           | CA         |          105 | Request To Send from the plotter Always High = ON = 'O' 2 +12V         |
| 17        | DD         |          115 | External ClockInput High = ON = +2.4 V to +5 V Low= OFF =00 Vto +0.4 V |
| 20        | CD         |        108.2 | Data Terminal Ready to modem High = ON = 'O' '=~+12 V Low = OFF = '1'  |
| 14*       | SBA        |          118 | SecondaryTransmit Data Data line from plotter to terminal              |
| 16*       | SBB        |          119 | Secondary ReceivedData Data line to plotter from terminal              |

## Output Baud Rate

The plotter is designed to operate in an asynchronous mode with switch-selectable baud rates of 75, 110, 150, 200, 300, 600, 1200, 2400, 4800, and 9600. See the 7470A Operator's Manual for instructions on setting the baud rate. However, setting all BAUD switches to zero and connecting an external clock input to pin 17 of the connector allows operation of the plotter at any intermediate baud rate up to 9600baud. Both the receiver (RRC) and transmitter (TRC) clocks will operate at the same clockrate. Requirements for the clock signal are as follows:

1. The clock frequency must be 16times the desired baud rate.
2. The baud rate must not exceed 9600.
3. The duty cycle of the clock pulse should be close to 50%.
