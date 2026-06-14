The Output Actual Position and Pen Status Instruction, OA 

DESCRIPTION Mies output actual position and pen status instruction, OA, is used to output the X- and Y-coordinates and pen status (up or down) associated with the actual pen position. UNS = This instruction can be used to determine the pen’s current position in plotter units. You might use that information to position a label or figure, or determine the parameters of some desired window. SYNTAX Mey (terminator) SAMUEL §=Output is always in plotter units. 

No parameters are used. The instruction will execute even if no terminator is received. 

~ 

The pen position and status are output to the computer as integers in ASCII in the form: 

## X,Y,P [TERM] 

## where 

X is always the X-coordinate in plotter units, Y is always the Y-coordinate in plotter units, P is the pen status (0 = pen up, 1 = pen down), and [TERM] is the output terminator for the interface installed. 

The ranges of the X- and Y-coordinates are the current mechanical limits determined by the setting of the paper switch. 

US A4 0< X< 10300 0< X< 10900 0< Y< 7650 0< Y< 7650 

No positive sign is output. 

OBTAINING INFORMATION FROM THE PLOTTER 7-3 
