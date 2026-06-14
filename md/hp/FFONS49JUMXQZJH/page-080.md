The Absolute Direction Instruction, DI WHEE =The absolute direction instruction, DI, specifies the direction in which characters are lettered. 

UNS The instruction can be used to change the direction of labeling to a new absolute direction; by absolute we mean independent of P1,P2 settings. It is especially useful for labeling a Y-axis or labeling a vertical graph. 

## SYNTAX 

Bipayg run, rise terminator or 

DI terminator 

Ae §=Run and rise are in decimal format, 0 to +127.9999, and specify the direction according to the relationship: 

**==> picture [287 x 127] intentionally omitted <==**

**----- Start of picture text -----**<br>
_<br>@= tan Can)_,/rise<br>where:<br>ay<br>4 7 "<br>a a ise = SIN (8)<br>| rs run = COS (8)<br>7 ; L RUN;<br>**----- End of picture text -----**<br>


At least one parameter must be effectively nonzero, i.e., | = 0.0004}. 

A DI command with a rise parameter of zero will produce horizontal labeling. A DI command with a run parameter of zero will produce vertical labeling. 

A DI command with no parameters will default to the values DI1,0 (horizontal). A DI command with only one or more than two parameters will set an error condition and the instruction will be ignored. 

A change in the orientation of P1 and P2 will not affect the direction of labeling. A DI command remains in effect until another DI, DR, IN, or DF command is executed, or the plotter is initialized from the front panel. 

A DI command updates the carriage-return point to the current pen position. 

When the angle, 6, necessary to establish the desired label direction is known, the command DI cosé, siné can be used to establish label direction. 

5-10 LABELING 
