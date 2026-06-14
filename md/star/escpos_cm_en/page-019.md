Rev.2.52 

## **2 EXPLANATION OF THE PAGE MODE 2-1 General Description** 

This printer has two print modes: 

The Standard Mode and the Page Mode. 

In the standard mode, the printer prints or performs a paper feed whenever it receives printing or paper feed instructions.  With the Page mode, received printing or paper feed instructions are all performed on the print region in the specified memory, but the printer does not act.  Then, when the ESCFF or FF command is executed, the data is expanded to that print region to print it in batch.  Specifically, when printing or line feeding data of “ABCDEF” <LF>, the status mode prints “ABCDEF” and executes one line feed.  However, with the page mode, “ABCDEF” is written to the specified print region on the memory and one line is moved in the memory position to write the next print data.  The printer enters the page mode using ESCL.  Subsequently received commands are all processed using the page mode.  By executing ESCFF, data that is received is printed in batch.  By executing FF, data that is received is printed in batch, then the printer recovers to the standard mode.  It is possible to return to the standard mode without printing print data in the page mode using ESCS.  However, that print data is cleared. 

<Transition of  Stand Mode Page Mode> 

**==> picture [349 x 115] intentionally omitted <==**

**----- Start of picture text -----**<br>
ESC FF<br>ESC L<br>Standard Mode Page Mode Print<br>ESC S<br>FF<br>Print<br>**----- End of picture text -----**<br>


## **2-2 Settings Using Commands in Standard Mode and Page Mode** 

- The values set using each command are common settings for both the standard mode and the page mode, but the settings of the following commands are set independently for each.  → ESCSP,ESC2,ESC3,FSS 

- In the standard mode, the maximum number of dots are set for the X direction, but in the page mode, the Y direction (the X direction when not rotated) when rotated in either the 90 degree direction or the 270 degree di rection becomes larger.  For details see the print region setting command (ESCW) for the page mode. 

ESC/POS Command Specifications 

19 
