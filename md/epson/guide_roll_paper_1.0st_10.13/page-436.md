## **C O N F I D E N T I A L** 

- Battery status differs depending on printer model. 

- The construction of battery status depends on printer model. 

- This command is effective when the printer is disabled by ESC = (select peripheral device). 

- With a serial interface, the printer executes this command when it is in offline, or in receive buffer-full status. 

- When you use this command, obey the following rules. 

   - After the host PC transmits the function data, the printer will send response data or status data back to the PC. Do not transmit more data from the PC until the response data or status data are received from the printer. 

   - When operating with a serial interface, be sure to configure operation so that the host computer uses the printer only when it is READY. 

   - When operating with a parallel interface, the data sent by this function (starting with Header and ending with NUL), as with other data, is first stored in the send buffer, then output in sequential order when the host computer changes to the reverse mode. Note that the send buffer capacity is 99 bytes, and any data exceeding this volume limit will be lost; therefore, when using this command, it is important to configure the operation so that the host computer’s change to the reverse mode and the subsequent status send/receive process is performed quickly. 

- With a parallel interface, if the printer is in BUSY condition, this command cannot be used in the following status conditions. 

   - When DIP switch or memory switch (BUSY condition) is on: receive buffer-full. 

   - When DIP switch or memory switch (BUSY condition) is off: offline, receive buffer-full, or error status. 

[Model-dependent variations] TM-P60 

## **Program Example for all printers** 

PRINT #1, CHR$(&H10);CHR$(&H14);CHR$(7);CHR$(1) 
