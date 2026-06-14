## **C O N F I D E N T I A L** 

[Model-dependent variations] 

TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60 

## **Program Example for all printers** 

PRINT #1, CHR$(&H1B);"L"; ← Select page mode PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); PRINT #1, CHR$(&H1B);"W";CHR$(0);CHR$(0);CHR$(0);CHR$(0);CHR$(180); CHR$(0);CHR$(44);CHR$(1); ← Set print area PRINT #1, CHR$(&H1B);"T";CHR$(0); ← Select print direction PRINT #1, "AAAAA"; CHR$(&HA); PRINT #1, "BBBBB"; CHR$(&HA); PRINT #1, CHR$(&H1B);"T";CHR$(2); ← Select print direction PRINT #1, "CCCCC"; CHR$(&HA); PRINT #1, "DDDDD"; CHR$(&HC); ← Batch print and return to standard mode 

**==> picture [134 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
Print Sample<br>AAAAA<br>BBBBB<br>← Print<br>area set<br>by  ESC W<br>DDDDD<br>CCCCC<br>**----- End of picture text -----**<br>
