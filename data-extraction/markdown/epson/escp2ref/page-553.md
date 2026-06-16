## Internal Serial Interface Six-pin DIN connector type

Connector pin assignment

|   Pin Number | Signal   | Signal   | Dir.Description                                |
|--------------|----------|----------|------------------------------------------------|
|            1 | TXD      | Out      | Transmits data for Xon/Xoff                    |
|            2 | REV      | Out      | Whether or not the printer is ready to receive |
|            3 | RXD      | In       | Receive data                                   |
|            4 | NC       | -        | Not Used                                       |
|            5 | SG       | -        | Signal Ground                                  |
|            6 | FG       | -        | Frame Ground                                   |

## Synchronization

Asynchronous

Data format 1 start bit Data word length: 8 bits Odd, even, or no parity 1 stop bit

## Baud rate

300-19,200 bps, depending on printer

Signal level Mark (1) -3V to -27V

Space (0) +3V to +27V

Handshaking Handshaking by DTR signal or X-on/X-off. When the number of free bytes in the input buffer drops below 256, the DTR signal changes to 'mark', signifying the printer is not ready to receive data. When the number of free bytes rises above 528, the DTR signal changes to 'space,' specifying that the printer is now ready to receive data.
