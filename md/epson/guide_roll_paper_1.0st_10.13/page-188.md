## **C O N F I D E N T I A L** 

[Model-dependent variations] None 

## **Program Example for all printers** 

FOR n=0 TO 2 PRINT #1, CHR$(&H1B);"a";CHR$(n); PRINT #1, "ABC"; CHR$(&HA); PRINT #1, "ABCD"; CHR$(&HA); PRINT #1, "ABCDE"; CHR$(&HA); NEXT n 

**==> picture [214 x 105] intentionally omitted <==**

**----- Start of picture text -----**<br>
Print Sample<br>ABC<br>ABCD ESC a 0<br>ABCDE<br>ABC<br>ABCD ESC a 1<br>ABCDE<br>ABC<br>ESC a 2 ABCD<br>ABCDE<br>**----- End of picture text -----**<br>
