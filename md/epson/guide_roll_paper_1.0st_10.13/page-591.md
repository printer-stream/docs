## **C O N F I D E N T I A L** 

   - After the host PC transmits the function data, the printer will send response data or status data back to the PC. Do not transmit more data from the PC until the corresponding data is received from the printer. 

   - When operating with a serial interface, be sure to configure operation so that the host computer uses these functions only when it is READY. 

   - With a parallel interface, a [Header ~ NUL] is stored at first in the transmission buffer of the printer with the other transmission data (except for ASB status). When the host enters Reverse Mode, the data is transmitted in order from the beginning. Data that exceeds the transmission buffer size (99 bytes) is ignored. When using the command, the host should enter Reverse Mode immediately and execute receive processing of status. 

- When communication with the printer uses XON/XOFF control with serial interface, the XOFF code may interrupt the “Header to NUL” data string. 

- The information for each function can be identified to other transmission data according to specific data of the transmission data block. When the header transmitted by the printer is [hex = 37H/decimal =55], treat NUL [hex = 00H/decimal =0] as a data group and identify it according to the combination of the header and the identifier. 

## [Model-dependent variations] TM-T90, TM-T20, TM-T88IV, TM-T70, TM-T88V, TM-L90, TM-P60 

## **Program Example1 (Print a symbol repeatedly)** 

>PRINT #1, CHR$(&H1D);"(k";CHR$(13);CHR$(0);CHR$(48);CHR$(80);CHR$(48);"TEST PRINT"; ← Save data <Function080> >PRINT #1, CHR$(&H1D);"(k";CHR$(3);CHR$(0);CHR$(48);CHR$(81);CHR$(48); ← Print symbol <Function081> >PRINT #1, CHR$(&H1D);"(k";CHR$(3);CHR$(0);CHR$(48);CHR$(81);CHR$(48); ← Print symbol <Function081> 

## **Program Example2 (Print a symbol which module width is different)** 

>PRINT #1, CHR$(&H1D);"(k";CHR$(13);CHR$(0);CHR$(48);CHR$(80);CHR$(48);"TEST PRINT"; ← Save data <Function080> >PRINT #1, CHR$(&H1D);"(k";CHR$(3);CHR$(0);CHR$(48);CHR$(67);CHR$(3); ← Set module width to 3 <Function067> >PRINT #1, CHR$(&H1D);"(k";CHR$(3);CHR$(0);CHR$(48);CHR$(81);CHR$(48); ← Print symbol <Function081> >PRINT #1, CHR$(&H1D);"(k";CHR$(3);CHR$(0);CHR$(48);CHR$(67);CHR$(5); ← Set module width to 5 <Function067> >PRINT #1, CHR$(&H1D);"(k";CHR$(3);CHR$(0);CHR$(48);CHR$(81);CHR$(48); ← Print symbol <Function081> 
