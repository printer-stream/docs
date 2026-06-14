## **C O N F I D E N T I A L** 

|a|b|**Function**|
|---|---|---|
|1|0, 48|DisableDLE DC4 (fn= 1) (does not execute the process)|
||1, 49|EnableDLE DC4 (fn= 1) (executes the process)|
|2|0, 48|DisableDLE DC4 (fn= 2) (does not execute the process)|
||1, 49|EnableDLE DC4 (fn= 2) (executes the process)|



## [Notes] 

- The printer processes each real-time command that is enabled (b=1, 49) upon receiving it. 

- A real-time command specified as disabled (b=0, 48) is not processed. 

- The setting of this command is effective until ESC @ is executed, the printer is reset, or the power is turned off. 

- If you transmit a command for graphics data or defined data that contains the sequence DLE DC4, be sure to disable real-time command (b=0, 48) processing before transmitting the graphics data or defined data command. Then the printer will process the sequence DLE DC4 as image data. 

## **Program Example** 

PRINT #1, CHR$(&H1D); Ó (D Ó ;CHR$(3);CHR$(0);CHR$(20);CHR$(2);CHR$(0); ← Set disabled PRINT #1, CHR$(&H1B); Ó ✻ Ó ;CHR$(0);CHR$(9);CHR$(0);CHR$(240);CHR$(15); PRINT #1, CHR$(16);CHR$(20);CHR$(2);CHR$(1);CHR$(8); ← Process as  image data PRINT #1, CHR$(15);CHR$(240); Ó END Ó ;CHR$(&HA); ← Execute print and line feed PRINT #1, CHR$(&H1D); Ó (D Ó ;CHR$(3);CHR$(0);CHR$(20);CHR$(2);CHR$(1); ← Set enabled PRINT #1, CHR$(16);CHR$(20);CHR$(2);CHR$(1);CHR$(8); ← Execute power off GOSUB *RECEIVE ← Confirmation Ò power off notice Ò 
