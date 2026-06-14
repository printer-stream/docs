## **C O N F I D E N T I A L** 

## [Notes for transmission process] 

- Data send operations are performed using Function 34 and 48. When you use the functions, obey the following rules. 

   - When the host PC transmits the function data, transmit the next data after receiving the corresponding data from the printer. 

   - When operating with a serial interface, be sure to configure operation so that the host computer uses the printer only when it is READY. 

   - When operating with a parallel interface, the data sent by this function (starting with Header and ending with NUL), as with other data, is first stored in the send buffer, then output in sequential order when the host computer changes to the reverse mode. Note that the send buffer capacity is 99 bytes, and any data exceeding this volume limit will be lost; therefore, when using this command, it is important to configure the operation so that the host computer’s change to the reverse mode and the subsequent status send/receive process is performed quickly. 

- When communication with the printer uses XON/XOFF control with serial interface, the XOFF code may interrupt the “Header to NUL” data string. 

- The information for each function can be identified to other transmission data according to specific data of the transmission data block. When the header transmitted by the printer is [hex = 37H/decimal =55], treat NUL [hex = 00H/decimal =0] as a data group and identify it according to the combination of the header and the identifier. 

## **Program Example 1 (Two or more labels are printed while peeling off one piece.)** 

GOSUB *Label.Print ← Send a sheet of print data. 

PRINT #1, CHR$(&H1C);"(L";CHR$(2);CHR(0);CHR$(65);CHR$(49); ← Paper feed to label peeling position <Function 65> I$=INPUT$(1) ← Waiting for inputting (The key is pushed after the label is peeled off.) PRINT #1, CHR$(&H1C);"(L";CHR$(2);CHR(0);CHR$(67);CHR$(50); ← Putting out the head of the current label <Function 67> GOSUB *Label.Print ← Send a sheet of print data. PRINT #1, CHR$(&H1C);"(L";CHR$(2);CHR(0);CHR$(65);CHR$(49); ← Paper feed to label peeling position <Function 65> I$=INPUT$(1) ← Waiting for inputting (The key is pushed after the label is peeled off.) 

PRINT #1, CHR$(&H1C);"(L";CHR$(2);CHR(0);CHR$(67);CHR$(50); ← Putting out the head of the current label <Function 67> 
