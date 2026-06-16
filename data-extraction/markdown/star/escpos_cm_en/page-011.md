<!-- image -->

## 1-1-4 Timing	for	Transmitting	XON/XOFF

When XON/XOFF control is selected, XON and XOFF are transmitted with the following timings.

The transmission timing varies according to the DIP switch settings or the memory switch settings.

XON code: &lt;11&gt; H

XOFF code: &lt;13&gt; H

For (3) below, XON is not transmitted when the reception buffer is full.

For (6) below, XOFF is not transmitted when the reception buffer is full.

## &lt;XON/XOFF	Transmission	Timing&gt;

|                   | Printer Status                                                                                                                                                                                                                                                          | Busy condition (*1)           | Busy condition (*1)                                 |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|-----------------------------------------------------|
|                   |                                                                                                                                                                                                                                                                         | OFF                           | ON                                                  |
| XON Transmission  | (1) When online for the first time after turning the power on or a reset using the interface (2) When the buffer full status was cancelled for recep - tion buffer (3) When shifting from offline to online (4) When recovered from a recoverable error using a command | Transmission Transmission - - | Transmission Transmission Transmission Transmission |
| XOFF Transmission | (5) When the reception buffer entered buffer full status (6) When shifting from online to offline                                                                                                                                                                       | Transmission -                | Transmission Transmission                           |

(*1) DIPSW Settings: Conditions for BUSY

ON = Reception buffer full or printer is offline (Default)

OFF  =  Reception buffer full

## 1-1-5 Serial	Interface	Connection	Example

- If the other connected party is DCE, be careful so that there is no status without a handshake (where data is flows)  (DTE: Data Terminal Equipment; DCE: Data Circuit Terminating Equipment)
- When transmitting data to the printer, turn on the power to the printer and initialize first.

<!-- image -->

| Host   | Printer   |
|--------|-----------|
| TXD    | RXD       |
| DSR    | DTR       |
| CTS    | RTS       |
| RXD    | TXD       |
| DTR    | DSR       |
| F.G    | F.G       |
| S.G    | S.G       |
