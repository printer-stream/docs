## **C O N F I D E N T I A L** 

[Model-dependent variations] TM-U230, TM-U220 

**==> picture [614 x 102] intentionally omitted <==**

**----- Start of picture text -----**<br>
Program Example for all printers Print Sample<br>AAAAACCCCC<br>PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); BBBBB                       ESC K used to print one line and then reverse<br>PRINT #1, "AAAAA"; CHR$(&HA);<br>feed the paper by 30/180 inch<br>PRINT #1, "BBBBB"; CHR$(&H1B);"K";CHR$(30);<br>PRINT #1, "     CCCCC"; CHR$(&HA);<br>**----- End of picture text -----**<br>


## TM-U230, TM-U220 

**This command must not be executed consecutively more than two times.** 

**Reverse direction paper feeding causes the following problems:** 

- **Paper feed pitch is incorrect.** 

- **Printer noise is louder than normal.** 

- **The paper may rub against the ribbon and become dirty.** 

**The vertical motion unit is 0.176 mm {1/144 inch}. This value equals a half dot pitch. In the reverse direction, the maximum paper feed amount is 8.467 mm {48/144 inch}. If the specified amount exceeds 8.467 mm {48/144 inch}, the printer only prints the data and does not feed the paper.** 
