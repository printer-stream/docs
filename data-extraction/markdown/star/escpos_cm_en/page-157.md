<!-- image -->

## GS r n

Name

Transmission of status

Code

ASCII

GS r n

Hex.

1D 72 n

Decimal 29 114 n

Defined Region

n = 1, 2, 49, 50

Function

Sends the specified status.

- n = 1, 49: Sends paper detector status

- n = 2, 50:   Sends the drawer kick connector status.

Details

- When using a serial interface:

- When in DTR/DSR control:   Sends the status after checking that the host can received data. If the host is not able to receive data, it waits until reception is possible.

- When in XON/XOFF control:  The printer transmits statuses without confirming whether the host computer can receive data.

- Because this command is executed while expanding the reception buffer, there may be a delay between the reception of the command and the status transmission, depending on the reception buffer status.

- When ASB is enabled , the status transmitted by this command and the ASB status must be differentiated. See Appendix-2 for details on how to identify.

Detector Status (n = 1, 49)

|   Bit | Status                       | '0'       | '1'       |
|-------|------------------------------|-----------|-----------|
|     7 | Fixed at '0'                 |           |           |
|     6 | Undefined                    | ---       | ---       |
|     5 | Undefined                    | ---       | ---       |
|     4 | Fixed at '0'                 |           |           |
|     3 | Paper roll end detector      | Has Paper | Paper out |
|     2 | Paper roll end detector      | Has Paper | Paper out |
|     1 | Paper roll near end detector | Has Paper | Paper out |
|     0 | Paper roll near end detector | Has Paper | Paper out |

Bit-2,3:  If the end detector shows there is no paper, the printer will always go offline, so this command is not executed.  Therefore, the status of bit - 2 = 1 or bit - 3 = 1 is not sent.

Drawer Kick Connector Status (n = 2, 50)

|   Bit | Status                       | '0'   | '1'   |
|-------|------------------------------|-------|-------|
|     7 | Fixed at '0'                 |       |       |
|     6 | Undefined                    | ---   | ---   |
|     5 | Undefined                    | ---   | ---   |
|     4 | Fixed at '0'                 |       |       |
|     3 | Undefined                    | ---   | ---   |
|     2 | Undefined                    | ---   | ---   |
|     1 | Undefined                    | ---   | ---   |
|     0 | Drawer kick connector pin #3 | 'L'   | 'H'   |

Reference

DLE EOT, Appendix-2
