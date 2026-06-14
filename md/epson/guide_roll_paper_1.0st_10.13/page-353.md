## **C O N F I D E N T I A L** 

printer has to store ASB status changes to be transmitted, the following 2 sets (8 bytes) of ASB status are changed to special data and transmitted prior to other transmission data when the host enters Reverse Mode: 

- ASB-1: Status information that shows whether status changes occurred 

- ASB-2: The latest ASB status information 

If bits have a different value between (ASB-1) and (ASB-2), this means at least one change has occurred. An example is shown below: 

||**First byte**|**Second byte**|**Third byte**|**Fourth byte**|
|---|---|---|---|---|
|ASB-1|0011 1000|0000 0000|0110 0011|0000 1111|
|ASB-2|0001 0000|0000 0000|0110 0011|0000 1111|



Bit 5 and 3 of the first byte are different from (ASB-1) and (ASB-2). From this information, you can see that [The cover is shutting now and On line though Off line (Bit 3) by cover opening Bit5)]. 

- Basic ASB status can be differentiated by other transmission data by Bit 0, 1, 4, and 7 of the first byte. Process the transmitted data from the printer as ASB status which is consecutive 3 byte if it is "0xx1xx00" [x = 0 or 1]. However, the processing shown in the following is necessary in the identifying processing of ASB status. 

   - When the host communicates with the printer by XON/XOFF control, 4 bytes of data may interrupt  ASB status; therefore, 4-byte code except for the XOFF code, is processed as ASB status. ASB status configuration is different from that of the XOFF code. 

[Model-dependent variations] 

TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60, TM-U230, TM-U220 

## **Program Example for all printers** 

PRINT #1, CHR$(&H1D);"a";CHR$(4); ← Enable "Error" status 
