## C O N F I D E N T I A L

- ■ The request of n = 0 can be used in the following online recovery waiting status.
- The roll paper is installed in TM-U230 (See GS z 0 .)
- Online recovery for the TM-L90 with Peeler (See GS z 0 (Peeler)).
- Status waiting for the button to be pressed, while GS ^ is executed.
- ■ ( n = 1) or ( n = 2) is enabled when a recoverable error occurs with the exception of an automatically recoverable error, and is ignored in other cases. Errors recoverable by ( n = 1) or ( n = 2) depend on the printer model.
- ■ Even if the printer is disabled by ESC = , this command can be used.
- ■ With a serial interface model, this command is executed even when the printer is offline or the receive buffer is full.
- ■ With a parallel interface model, this command is not executed in the following statuses, because the printer is busy and unable to receive data from the host computer. The DIP switch (BUSY condition) is different, depending on the printer model.
- Receive buffer is full when DIP switch is set to On.
- Printer is offline or receive buffer is full when DIP switch is set to Off.
- ■ When a recoverable error occurs, after removing the cause of the error, the printer can recover from the error by transmitting DLE ENQ 1 or DLE ENQ 2 without the printer being turned off.
- ■ DLE ENQ 1 or DLE ENQ 2 is enabled only when a recoverable error occurs, with the exception of an automatically recovered error, and is ignored in other cases. Errors recoverable by DLE ENQ 1 or DLE ENQ 2 depend on the printer model.
- ■ DLE ENQ 1 or DLE ENQ 2 is also executed to recover from a recoverable error when the printer is disabled by ESC = .
- ■ In page mode, if the printer recovers from a recoverable error by using DLE ENQ 2 , the printer returns to standard mode after clearing the data in receive and print buffers and changing the values set by ESC W to the default values.
- ■ After processing DLE ENQ 2 , the print position is moved to the left side of the printable area. Printer is in the status 'beginning of the line,' or 'there is not data in the print buffer.'
- ■ This command is disabled while sending the block data 'Header ~ NUL.'
