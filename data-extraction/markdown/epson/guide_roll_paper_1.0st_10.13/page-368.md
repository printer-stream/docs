## C O N F I D E N T I A L

- After the host PC transmits the function data, the printer will send response data or status data back to the PC. Do not transmit more data from the PC until the response data or status data are received from the printer.
- When operating with a serial interface, be sure to configure operation so that the host computer uses the printer only when it is READY.
- With a parallel interface, a real-time status is stored in the transmission buffer of the printer temporarily the same as the other transmission data (except for ASB status), and when the host enters reverse mode, data is transmitted in order from the beginning of the transmission buffer. The transmission buffer is 99 bytes; therefore, data that exceeds 99 bytes is ignored. When using this command, the host should be changed to the reverse mode immediately and execute a receive processing of status.
- ■ After the print changing line operation ends, paper sensor status ( n = 1, 49) is transmitted. Therefore if use GS r 1 according to the printing instruction, host recognizes the print completion by receiving paper sensor status.
- ■ Normal status can be differentiated by the information of bits 4, and 7 from other transmission data. If the data transmitted from the printer after outputting GS r to the printer is '0xx1xx10'(x = 0 or 1), process the data as a normal status.

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 , TM-U230 , TM-U220

## Program Example for all printers

PRINT #1, CHR$(&amp;H1D);"r";CHR$(1); ← Transmits paper sensor status

## TM-J2000/J2100

- ■ Paper sensor status ( n = 1, 49)
- When the roll paper end sensor detects a paper-end, the printer goes offline and does not execute this command. Therefore, bits 2 and 3 of the paper sensor status do not transmit a paper-end status.
- ■ Ink status ( n = 4, 52)
- The function of bit 1 is not supported in TM-J2000 (Single color).
