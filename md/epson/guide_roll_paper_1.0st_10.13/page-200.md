## **C O N F I D E N T I A L Program example for GS $ and GS \** 

## **Program Example** 

PRINT #1, CHR$(&H1B);"L"; ← Select page mode PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); PRINT #1, CHR$(&H1B);"W";CHR$(0);CHR$(0);CHR$(0);CHR$(0); CHR$(180);CHR$(0);CHR$(144);CHR$(1); ← Set print area PRINT #1, CHR$(&H1B);"T";CHR$(0); ← Select print direction PRINT #1, "AAAAA"; CHR$(&HA); PRINT #1, "BBBBB"; PRINT #1, CHR$(&H1D);"$";CHR$(90);CHR$(0); ← Set absolute position PRINT #1, "CCCCC"; CHR$(&HA); PRINT #1, "DDDDD"; CHR$(&HA); PRINT #1, "EEEEE"; PRINT #1, CHR$(&H1D);"\";CHR$(90);CHR$(0); ← Set relative position PRINT #1, "FFFFF"; CHR$(&HC); ← Batch print and return to standard mode 

## **Print Sample** 

**==> picture [135 x 91] intentionally omitted <==**

**----- Start of picture text -----**<br>
AAAAA<br>BBBBB<br>90/180 inch<br>CCCCC<br>DDDDD ←  Print<br>area set<br>EEEEE by ESC W<br>90/180 inch<br>FFFFF<br>**----- End of picture text -----**<br>


## TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90 

**The vertical or horizontal motion unit is specified by** GS P **.** 

## TM-P60 

**The vertical or horizontal motion unit is approximately 0.125 mm {1/203 inches}. This value equals one dot pitch.** 
