Connector pin assignment

| Pin Number   | Signal   | Signal   | Dir.Description                                                                                             |
|--------------|----------|----------|-------------------------------------------------------------------------------------------------------------|
| 2            | TXD      | Out      | Transmits data for Xon/Xoff                                                                                 |
| 20           | DTR      | Out      | Indicates that the printer is ready to receive not.                                                         |
| 11           | REV      | Out      | Connected directly to the DTR signal                                                                        |
| 4            | RTS      | Out      | Request to send. Always SPACE level when the printer is powered on. Pulled up to +12V via 4.7Kohm resistor. |
| 3            | RXD      | In       | Receive data                                                                                                |
| 7            | SG       | -        | Signal Ground                                                                                               |
| 1            | FG       | -        | Frame Ground                                                                                                |
| Other        | NC       | -        | Not Used                                                                                                    |

Synchronization

Asynchronous

Data format

1 start bit Data word length: 7 or 8 bits Odd, even, or no parity 1 stop bit

Baud rate

300-19,200 bps, depending on printer

Signal level

EIA-232D Mark (1) -3V to -25V Space (0) +3V to +25V

## Handshaking DTR signal and XON/XOFF

The DTR signal is MARK and an XOFF code (DC3, 13H) is transmitted when the available input buffer space drops to 256 bytes. The DTR signal is SPACE and an XON (DC1, 11H) is transmitted when the available input buffer space returns to 256 bytes.

## ETX, ACK/NAK d

At the time the printer receives an ETX (03H) command, if the available buffer space is more than 256 bytes, the printer sends an ACK (06H) code in reply, or if the available buffer space is less than 256 bytes, the printer sends NAK (15H) and 'd' (64H) codes continuously. The ETX- ACK handshaking protocol can be enabled or disabled altering the default settings.

Error handling

When a parity error is detected, the received byte is changed to the '*' character code. Overrun errors and framing errors are ignored.
