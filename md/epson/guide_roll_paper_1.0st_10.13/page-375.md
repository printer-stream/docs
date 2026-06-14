## **C O N F I D E N T I A L** 

■ HRI characters are printed at the position specified by GS H **.** 

■ HRI character is Human Readable Interpretation character indicated with bar code. 

[Model-dependent variations] TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60 

## **Program Example for all printers** 

PRINT #1, CHR$(&H1D);"h";CHR$(80); ← Set height PRINT #1, CHR$(&H1D);"H";CHR$(2); ← Select print position PRINT #1, CHR$(&H1D);"f";CHR$(0); ← Select font PRINT #1, CHR$(&H1D);"k";CHR$(2); ← Print bar code PRINT #1, "496595707379";CHR$(0); PRINT #1, CHR$(&HA); PRINT #1, CHR$(&H1D);"f";CHR$(1); ← Select font PRINT #1, CHR$(&H1D);"k";CHR$(2); ← Print bar code PRINT #1, "496595707379";CHR$(0); 

**==> picture [163 x 121] intentionally omitted <==**

**----- Start of picture text -----**<br>
Print Sample<br>←  Font A<br>4965957073797<br>←  GS H  3<br>←  Font B<br>4965957073797 4  9  6  5  9  5  7  0  7  3  7  9  7<br>**----- End of picture text -----**<br>


## TM-J2000/J2100, TM-T90, TM-L90 

**[Other than Japanese model] Character configurations: Font A: 12** × **24 Font B: 9** × **17** 

**[Japanese model] Character configurations:** 

**Font A: 12** × **24 Font B: 10** × **24 Font C: 8** × **16** 
