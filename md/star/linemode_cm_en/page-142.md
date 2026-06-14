## **ESC GS x I** 

[Name] Get PDF417 bar code expansion information [Code] ASCII ESC GS x I Hex. 1B 1D 78 49 Decimal 27 29 120 73 

[Defined Area] --[Initial Value] --[Function] When printing a bar code with the current settings and at the print starting position using this command, error information is sent to the printer.  Therefore, it is possible to check whether it is possible to print before actually printing, by using this command. 

If an error occurs, this command is discarded even if the print command (<ESC> <GS> “x” “P”) is sent. 

If the following errors occur, “Error” information is sent to the printer. 

• When an error is generated when generating a bar code, due to the combination of the bar code setting commands. 

- When the bar code data that is generated exceeds the printable size of PDF417. 

- When the print data exceeds the currently set print region 

Transmission format: <ESC> <GS> “x” “I” n 

|n||
|---|---|
|0|No Error|
|1|Error|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-124 
