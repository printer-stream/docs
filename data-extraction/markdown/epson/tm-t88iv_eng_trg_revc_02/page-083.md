## Appendix

## Specifications of Interface and Connector

<!-- image -->

For detailed information about LAN or wireless LAN, see one of the following:

- LAN: UB-E02 Technical Reference Guide
- Wireless LAN: UB-R02/R03 Technical Reference Guide

## RS-232C Serial Interface

## Interface board specifications (RS-232C-compliant)

| Item                                      | Item                                      | Specifications                                                                                                                                                     |
|-------------------------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data transfer method                      | Data transfer method                      | Serial                                                                                                                                                             |
| Synchronization                           | Synchronization                           | Asynchronous                                                                                                                                                       |
| Handshake                                 | Handshake                                 | Select one of the following with DIP switch 1-3: • DTR/DSR • XON/XOFF                                                                                              |
| Signal level                              | MARK                                      | -3V to -15V logic '1'/OFF                                                                                                                                          |
| Signal level                              | SPACE                                     | +3V to +15V logic '0'/ON                                                                                                                                           |
| Bit length                                | Bit length                                | Select one of the following with DIP switch 1-4: • 7 bit • 8 bit                                                                                                   |
| Transmission speed [bps: bits per second] | Transmission speed [bps: bits per second] | • Select one of the following with DIP switch 1-7/1-8: 4800/9600/19200bps • Select one of the following with commands: 2400/4800/9600/19200/38400/57600/115200 bps |
| Parity check                              | Parity check                              | Select one of the following with DIP switch 1-5: • Yes • No                                                                                                        |
| Parity selection                          | Parity selection                          | Select one of the following with DIP switch 1-6: • Even • Odd                                                                                                      |
| Stop bit                                  | Stop bit                                  | 1 or more bits However, the stop bit for data transfer from the printer is fixed to 1 bit.                                                                         |
| Connector                                 | Printer side                              | DSUB 25-pin (female) connector                                                                                                                                     |
