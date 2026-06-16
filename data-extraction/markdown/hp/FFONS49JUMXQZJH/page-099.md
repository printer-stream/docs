SYNTAX DP (terminator)

EXPLANAHUNNo parameters are used. The instruction will execute even if no terminator is received.

When the DP command is received, automatic pen lift is suppressed and the plotter is ready to have a digitized point entered by pressing ENTER on the front panel.

When ENTER is pressed, the X- and Y-coordinates of that point and pen up/ down status are stored for retrieval by the OD command. Pressing ENTER sets bit position 2 of the status byte, indicating a digitized point is available for output.

After ENTER has been pressed, automatic pen lift is reactivated.

## The Digitize Clear Instruction, DC

DESCRIPTIONThe digitize clear instruction, DC, provides a means to terminate digitize mode.

M This instruction can be used to terminate digitizemode with­ out entering a point. If you are using an interrupt routine in a digitiz­ ing program to branch to some other plotting function, you could use DCto clear digitize mode immediately after branching. |

SYNTAX DC (terminator)

EXPLANAHUNNo parameters are used. The instruction will execute even if no terminator is received.

When the DC command is received, digitize mode is terminated. Auto­ matic pen lift is reactivated.

## The Output Digitized Point and Pen Status Instruction, OD

DESCNP-'UN The output digitized point and pen status instruction, OD, is used to output the X-and Y-coordinates and pen up/ down status associated with the last digitized point.

USES This instruction is used after DP and ENTER in all digitizing applications to return the coordinates of the digitized point to the computer. |

SYNTAX OD (terminator)

EXPLANATIONNo parameters are used. The instruction will execute even if no terminator is received.
