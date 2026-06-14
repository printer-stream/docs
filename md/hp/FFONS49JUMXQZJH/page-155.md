- 4, The clock pulse must be a logic on of +2 V< V < 25 V anda logic off of -25 V< V <+0.8 V (3.5 kO input impedance). 

5. Care should be taken to keep the transmission lines as short as possible to minimize transmission line reflection noise. 

## Stop Bits 

The plotter is configured to automatically verify or generate one or two stop bits, depending on the setting of the plotter’s baud rate switches. Refer to the 7470A Operator’s Manual for more information. 

Transmission Errors Transmission errors occur when communication between the computer. and plotter is incomplete or does not conform to what is expected or required by either party. 

## Transmission errors include: 

- e Framing error — the plotter does not detect a valid stop bit at the end of every character. 

- e Parity error — the plotter does not detect the expected parity (odd or even). 

- ¢ Overrun error — a plotter instruction writes over another instruction. 

- e Buffer overflow error — the plotter receives more bytes of data than it has space for in the buffer. 

When the plotter detects a framing, parity, or overrun error, it turns on the front panel ERROR light and sets error code 15. This error code generally indicates that the communication incompatibility is hardware related (incorrect stop bit jumper installation, wrong parity selection, incompatible or incorrectly set baud rates, etc.). 

When the plotter detects a buffer overflow, it turns on the front panel ERROR light and sets error code 16. The last HP-GL data that caused the overflow will be lost. Error code 16 generally indicates an improperly established handshake protocol. The ERROR light remains on until either the user interrogates the plotter via an output extended error command, ESC. E, and the plotter responds with the appropriate error code, or the user turns the plotter off, or an HP-GL initialization instruction, IN, is processed, or a front-panel reset occurs. 

A complete list of error codes is included with the discussion of the ESC. E instruction. 

RS-232-C/CCITT V.24 INTERFACING 10-13 
