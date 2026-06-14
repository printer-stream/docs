Rev.2.52 

<Example 2: Sample Program using Basic> 

|100|PRINT|#1, CHR$(&H1B); “L”;|
|---|---|---|
|110|PRINT|#1, CHR$(&H1B); “W”; CHR$(0); CHR$(0); CHR$(0); CHR$(0);|
|120|PRINT|#1, CHR$(200); CHR$(0); CHR$(144); CHR$(1);|
|130|PRINT|#1, CHR$(&H1B); “T”; CHR$(0);|
|140|PRINT|#1, “Page mode lesson 2 CAN command”|
|150|PRINT|#1, CHR$(&HA);|
|160|PRINT|#1, “ABCDEFGHIJKLMNOPQRST1234567890”|
|170|PRINT|#1, CHR$(&HC);|



Initially, send ESC L to switch to page mode (line number 100).  Next, use ESC W to send eight arguments from xL to dyH to ensure the print region.  In this example, to ensure a printer region of the size of 200 in the x direction and 400 in the y direction from the origin (0,0), send arguments in the order of 0,0,0,0,200,0,144,1.  (Line numbers 110 to 120) Also, specify using ESC T.  Specify the print direction with 0.  (Line number 130)   These settings send the print data “Page mode lesson 2 CAN command” and “ABCDEFGHIJKLMNOPQRST1234567890” (line numbers 140 to 160).  By sending FF, (line number 170), the following will be printed. 

**==> picture [401 x 87] intentionally omitted <==**

**----- Start of picture text -----**<br>
(0,0)<br>200 Print Paper<br>Page mode lesson<br>2 CAN command<br>ABCDEF    JKLMNO<br>      400 PQRST1234567890<br>Print Region<br>**----- End of picture text -----**<br>


It is possible to delete a portion of the data by adding the next program before sending FF. 170 PRINT #1, CHR$(&H1B); “W”; CHR$(72); CHR$(0); CHR$(120); CHR$(0); 180 PRINT #1, CHR$(36); CHR$(0); CHR$(48); CHR$(0); 190 PRINT #1, CHR$(&H18); 200 PRINT #1, CHR$(&HC); 

The character string GHI, in the figure below, is deleted as a result of adding the program above.  Also, if deleting using the CAN command, a space is used without filling the deleted portion. 

**==> picture [395 x 93] intentionally omitted <==**

**----- Start of picture text -----**<br>
(0,0)  __ Print Paper<br>200<br>Page mode lesson<br>2 CAN command<br>ABCDEFGHIJKLMNO<br>       400 PQRST1234567890 Print Region<br>**----- End of picture text -----**<br>


ESC/POS Command Specifications 

291 
