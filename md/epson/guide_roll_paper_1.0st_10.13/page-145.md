## **C O N F I D E N T I A L** 

[Model-dependent variations] None 

## **Program Example for all printers** 

PRINT #1, CHR$(&H1B);"{";CHR$(0); ← Cancel PRINT #1, "ABCDE"; CHR$(&HA); PRINT #1, "BCDEF"; CHR$(&HA); PRINT #1, CHR$(&H1B);"{";CHR$(1); ← Select PRINT #1, "ABCDE"; CHR$(&HA); PRINT #1, "BCDEF"; CHR$(&HA); 

**==> picture [163 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
Print Sample<br>Normal printing<br>ABCDE<br>BCDEF<br>Upside-down<br>printing<br>BCDEF<br>ABCDE<br>**----- End of picture text -----**<br>
