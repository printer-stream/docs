SAGES =DP (terminator) 

EXPLANATION Bing parameters are used. The instruction will execute even if no terminator is received. 

When the DP command is received, automatic pen lift is suppressed and the plotter is ready to have a digitized point entered by pressing ENTER on the front panel. 

When ENTER is pressed, the X- and Y-coordinates of that point and pen up/down status are stored for retrieval by the OD command. Pressing ENTER sets bit position 2 of the status byte, indicating a digitized point is available for output. 

After ENTER has been pressed, automatic pen lift is reactivated. 

## The Digitize Clear Instruction, DC SHEE §=6The digitize clear instruction, DC, provides a means to 

terminate digitize mode. 

| USES | This instruction can be used to terminate digitize mode without entering a point. If you are using an interrupt routine in a digitizing program to branch to some other plotting function, you could use DC to clear digitize mode immediately after branching. 

## SYNTAX Maye (terminator) 

EXPLANATION BiBxpe parameters are used. The instruction will execute even if no terminator is received. 

When the DC command is received, digitize mode is terminated. Automatic pen lift is reactivated. 

## The Output Digitized Point and Pen Status Instruction, OD 

DESCRIPTION Suis output digitized point and pen status instruction, OD, is used to output the X- and Y-coordinates and pen up/down status associated with the last digitized point. | USES | This instruction is used after DP and ENTER in all digitizing applications to return the coordinates of the digitized point to the computer. SYNTAX Miteyp) (terminator) 

SYNTAX Miteyp) (terminator) EXPLANATION BiBNga parameters are used. The instruction will execute even if no terminator is received. 

DIGITIZING 6:3 
