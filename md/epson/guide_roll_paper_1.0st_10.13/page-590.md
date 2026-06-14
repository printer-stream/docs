## **C O N F I D E N T I A L** 

   - The same symbol can be printed by executing <Function 381> repeatedly after executing <Function 380> of this command. 

   - Using <Function 382> of this command, the size of the symbol printed with <Function 381> can be acquired. 

- [Notes for Composite Symbology processing (when cn = 52 is specified)] 

   - The composite symbol (line element/2D composite element) symbol data specified by <Function 480> of this command (d1...dk) is temporarily stored in the archive area of the printer and is printed by <Function 481>. 

   - The setting value of <Function 467> and <Function 472> is used when processing <Function 481> and <Function 482> of this command. Furthermore, the setting value of <Function 471> is used when processing GS1 DataBar Expanded Stacked. If the printing area is narrow, it may not be possible to print the symbol. 

   - The same symbol can be printed by executing <Function 481> repeatedly after executing <Function 480> of this command. 

   - Composite Symbology with a different combination can be printed by resending other symbol data with either of the line element or 2D composite element as it is. 

Step 1) Specify <Function 480: (a = 49, b = 65)>, and send the 2D composite element data. 

Step 2) Specify <Function 480: (a = 48, b = 70)>, and send the line element data. 

Step 3) Print Composite Symbology of which GS1 DataBar Omnidirectional is the line element with <Function 481>. 

Step 4) Specify <Function 480: (a = 48, b = 74)>, and send the line element data. 

Step 5) Print Composite Symbology of which GS1 DataBar Limited is the line element with <Function 481>. 

- Using <Function 482> of this command, the size of the symbol printed with <Function 481> can be acquired. 

[Notes for transmission process] 

- Transmission process is performed by <Function 082>, <Function 182>, <Function 282>, <Function 382>, and <Function 482>. When you use this command, follow these rules. 
