## For Serial Interface

## DIP Switch Bank 1

| SW   | Function                      | ON                                          | OFF                                         | Factory setting   |
|------|-------------------------------|---------------------------------------------|---------------------------------------------|-------------------|
| 1-1  | Data reception error          | Ignored                                     | Prints '?'                                  | OFF               |
| 1-2  | Receive buffer capacity       | 45 bytes                                    | 4 KB                                        | OFF               |
| 1-3  | Handshaking                   | XON/XOFF                                    | DTR/DSR                                     | OFF               |
| 1-4  | Word length                   | 7 bits                                      | 8 bits                                      | OFF               |
| 1-5  | Parity check                  | Yes                                         | No                                          | OFF               |
| 1-6  | Parity selection              | Even                                        | Odd                                         | OFF               |
| 1-7  | Transmission speed selections | See the ' Transmission speed (DIP switch 1- | See the ' Transmission speed (DIP switch 1- | ON                |
| 1-8  | Transmission speed selections | 7/1-8)' table below.                        | 7/1-8)' table below.                        | OFF               |

For DIP switch 1-2 (Receive buffer capacity), see also DIP switch 2-5 (Setting the release condition of the receive buffer BUSY state).

Transmission speed (DIP switch 1-7/1-8)

| Transmission speed (bps)                                                                                  | SW 1-7   | SW 1-8   |
|-----------------------------------------------------------------------------------------------------------|----------|----------|
| 38400 (Initial value)                                                                                     |          |          |
| 2400, 4800, 9600, 19200, 38400, 57600, 115200 (When setting with a command/Memory Switch Setting Utility) | ON       | ON       |
| 4800                                                                                                      | OFF      | ON       |
| 9600                                                                                                      | ON       | OFF      |
| 19200                                                                                                     | OFF      | OFF      |

bps: b

it s per seco n d
