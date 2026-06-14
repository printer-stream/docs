## **C O N F I D E N T I A L** 

## ■ The macro is defined by GS :. 

- Macro function is useful to print the same data repeatedly. To define a macro definition, send GS : just before and after the data desired to be repeated. And then execute macro by using GS ^ to print the same data repeatedly. Macro function eliminates the need for sending all the print data every time. 

- [Model-dependent variations] TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-L90 

## **Program example for GS : and GS ^** 

## **Program Example** 

PRINT #1, CHR$(&H1D);":"; PRINT #1, CHR$(&H1B);"a";CHR$(1); PRINT #1, "*** Hello"; PRINT #1, CHR$(&H1D);"!";CHR$(17); PRINT #1, "EPSON"; PRINT #1, CHR$(&H1D);"!";CHR$(0); PRINT #1, "World! ***"; PRINT #1, CHR$(&HA); CHR$(&HA); PRINT #1, CHR$(&H1B);"a";CHR$(0); PRINT #1, CHR$(&H1B);"-";CHR$(1); PRINT #1, "No.                       "; CHR$(&HA); PRINT #1, "Name                      "; CHR$(&HA); PRINT #1, "Address                   "; CHR$(&HA); PRINT #1, CHR$(&H1B);"d";CHR$(5); PRINT #1, CHR$(&H1B);"-";CHR$(0); PRINT #1, CHR$(&H1D);":"; PRINT #1, CHR$(&H1D);"^";CHR$(2);CHR$(0);CHR$(0); 

**==> picture [38 x 18] intentionally omitted <==**

**----- Start of picture text -----**<br>
Defines<br>a macro<br>**----- End of picture text -----**<br>


**==> picture [73 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
Print Sample<br>**----- End of picture text -----**<br>


**==> picture [124 x 46] intentionally omitted <==**

**----- Start of picture text -----**<br>
*** Hello EPSON World! ***<br>No.<br>Name<br>Address<br>**----- End of picture text -----**<br>


**==> picture [124 x 46] intentionally omitted <==**

**----- Start of picture text -----**<br>
*** Hello EPSON World! ***<br>No.<br>Name<br>Address<br>**----- End of picture text -----**<br>


## TM-J2000/J2100 

**When** m **= 1, the PAPER OUT LED indicator blinks during a macro waiting state. When** m **= 1, the PAPER FEED can be Paper feed button.** 
