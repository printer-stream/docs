## **C O N F I D E N T I A L** 

[Model-dependent variations] 

TM-U220 **Program Example for all printers Print Sample** PRINT #1, CHR$(&H1B);"-";CHR$(1); ← Select AAAAA ← Underline (1-dot thick) turned on PRINT #1, "AAAAA"; CHR$(&HA); BBBBB ← Underline turned off PRINT #1, CHR$(&H1B);"-";CHR$(0); ← Cancel PRINT #1, "BBBBB"; CHR$(&HA); 

## TM-U220 

**When (n = 1, 2, 49, 50), this command specifies the underline mode (1 dot thick).** 
