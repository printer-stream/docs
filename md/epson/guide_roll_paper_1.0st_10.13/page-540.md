## **C O N F I D E N T I A L** 

■ The maintenance counter can be used for establishing the time for replacing consumed parts or cleaning. 

■ When you use this command, follow these rules. 

   - When the host PC transmits the function data, transmit the next data after receiving the corresponding data (the header ~ NULL) from the printer. 

   - With serial interface printers, be sure to use this function when the host is in the READY state. 

   - With a parallel interface, the data sent by this function [Header ~ NUL], as with other data, is first stored in the send buffer, then output in sequential order when the host computer changes to the reverse mode. Note that the send buffer capacity is 99 bytes, and any data exceeding this volume limit will be lost; therefore, when using this command, it is important to configure the operation so that the host computer’s change to the reverse mode and the subsequent status send/receive process is performed quickly. 

- Types of maintenance counters differ, depending on the printer models. 

- When the host is communicating with the printer by XON/XOFF control, the XOFF code might interrupt [Header ~ NUL]. 

- The maintenance counter data can be identified to other transmission data according to specific data of the transmission data block. When the header transmitted by the header is [hex = 5FH/decimal = 95], treat NUL [hex = 00H/decimal =0] as a data group and identify it according to the header. 

[Model-dependent variations] 

TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60 

## **Program Example** 

PRINT #1, CHR$(&H1D); Ó g2 Ó ;CHR$(0);CHR$(11);CHR$(0); ← Transmit a counter value of print characters 
