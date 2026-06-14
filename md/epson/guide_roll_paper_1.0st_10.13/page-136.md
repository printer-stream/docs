## **C O N F I D E N T I A L** 

[Model-dependent variations] 

## TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90 

**==> picture [592 x 200] intentionally omitted <==**

**----- Start of picture text -----**<br>
Program Example for all printers Print Sample<br>PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); Character spacing<br>PRINT #1, CHR$(&H1B);" ";CHR$(20); ←  Set character spacing<br>PRINT #1, CHR$(&H1B);"3";CHR$(15); ←  Set line spacing<br>PRINT #1, CHR$(&H1B);"V";CHR$(1); ←  Select Linespacing ESC V 1<br>  PRINT #1, "AAAAA"; CHR$(&HA);<br>A A A A A A Line<br>  PRINT #1, "BBBBB"; CHR$(&HA); B B B B B B spacing ESC V 0<br>  PRINT #1, "CCCCC"; CHR$(&HA); C C C C C C<br>PRINT #1, CHR$(&H1B);"2"; ←  Set line spacing<br>PRINT #1, CHR$(&H1B);"V";CHR$(0); ←  Cancel<br>  PRINT #1, "AAAAA"; CHR$(&HA); Character spacing<br>  PRINT #1, "BBBBB"; CHR$(&HA);<br>  PRINT #1, "CCCCC"; CHR$(&HA);<br>ABC ABC ABC ABC ABC ABC<br>**----- End of picture text -----**<br>


## TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70,TM-L90 

**These printers don’t support the 90** ° **clockwise rotation mode (1.5-dot character spacing). The printer models use** n **as follows.** 

|n|**Function**|
|---|---|
|**0, 48**|**Turns off 90**° **clockwise rotation mode.**|
|**1, 49**<br>**2, 50**|**Turns on 90**° **clockwise rotation mode (1-dot character spacing).**|
