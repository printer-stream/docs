When an OE command is received, the plotter converts the last HP-GL error to a positive integer in ASCII, which is output in the form: 

## error number [TERM] 

## The error number is defined as follows: 

|Error||
|---|---|
|Number|Meaning|
|0|No error|
|1|Instruction not recognized|
|2|Wrong number ofparameters|
|3|Out-of-range parameters, or illegal character|
|4|Not used|
|5|Unknown character set|
|6|Position overflow|
|vi|Not used|
|8|Vectorreceivedwhilepinchwheelsraised|



## [TERM] is the output terminator for the interface installed. 

In an HP-IB or an HP-IL system after the carriage return has been sent, and in an RS-232-C system after the output is complete, bit position 5 of the status byte is cleared (if set), and the ERROR LED (if lit) is turned off (unless there is an RS-232-C error which has not been cleared by an ESC . E command). 

You should note that anytime the plotter receives an unpaired alphabetic character, error 1 will be set. Thus, an alphabetic parameter or three alphabetic characters in a row will generate error 1. When you encounter error 1, look for a misplaced alphabetic character. 

Once your plotting programs are debugged, you may want to remove most output error instructions from your program to reduce your computer’s I/O operations and maximize plotting speed. 

## The Output Factors Instruction, OF 

HME =The output factors instruction, OF, is used to output the number of plotter units per millimetre in each axis. 

Wid) =6This instruction enables the plotter to be used with software which must know the size of a plotter unit. SMAUERG «OF (terminator) ee EMULE =No parameters are used. The instruction will execute even if no terminator is received. 

7-6 OBTAINING INFORMATION FROM THE PLOTTER 
