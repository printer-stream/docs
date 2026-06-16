## C O N F I D E N T I A L

[Notes]

- ■ This is a real-time command that the printer executes upon receiving it. Take the following into consideration:
- If this command interrupts the code string of another command, this command is processed as a parameter of the other command; therefore, the print result will not be correct.
- If a command such as graphics data or defined data has a code string that is the same as a code string in a parameter, the printer processes and then continues with the bit-image or other command.
- ■ With a serial interface model, this command is executed even when the printer is offline, the receive buffer is full, or an error occurs.
- ■ With a parallel interface model, this command is not executed in the following conditions, because the printer is busy and unable to receive data from the host computer. The DIP switch (BUSY condition) is different, depending on the printer model.
- Receive buffer is full when DIP switch or memory switch (BUSY condition) is set to On.
- Printer is offline, an error occurs, or receive buffer is full when DIP switch or memory switch (BUSY condition) is set to Off.
- ■ This command can be used when the printer is disabled by ESC = .
- ■ This command is ignored when transmitting block data (Header ~ NUL).
- ■ Each status equals 1 byte.
