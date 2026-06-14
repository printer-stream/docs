## **C O N F I D E N T I A L** 

   - If the starting position is the upper right or lower left of the print area: These commands use horizontal motion units: ESC 3, ESC J, GS $, GS \ These commands use vertical motion units: ESC SP, ESC $, ESC \ 

- The settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off. 

[Model-dependent variations] 

## None 

## **Program Example for all printers** 

PRINT #1, CHR$(&H1B);"L"; ← Select page mode 

PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); PRINT #1, CHR$(&H1B);"W";CHR$(0);CHR$(0);CHR$(0);CHR$(0); CHR$(240);CHR$(0);CHR$(200);CHR$(0); ← Set print area 

- PRINT #1, CHR$(&H1B);"T";CHR$(0); ← Select print direction PRINT #1, "AAAAA"; CHR$(&HA); 

PRINT #1, "BBBBB"; CHR$(&HA); 

**==> picture [132 x 109] intentionally omitted <==**

**----- Start of picture text -----**<br>
Print Sample<br>AAAAA<br>BBBBB<br>← Print area<br>set by<br>ESC W<br>CCCCC DDDDD EEEEE<br>**----- End of picture text -----**<br>


PRINT #1, CHR$(&H1B);"T";CHR$(1); ← Select print direction PRINT #1, "CCCCC"; CHR$(&HA); PRINT #1, "DDDDD"; CHR$(&HA); 

PRINT #1, CHR$(&H1B);"T";CHR$(2); ← Select print direction 

- PRINT #1, "EEEEE"; CHR$(&HC); ← Batch print and return to standard mode 
