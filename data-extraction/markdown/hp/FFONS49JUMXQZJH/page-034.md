[BE The instruction can be used to determine the position of P1 and P2 in plotter units. This information can be used with the input window command, IW, to set the window to P1 and P2 under program control, to compute the number of plotter units per user unit when scaling is on, or to determine the numeric coordinates of P1 and P2 when they have been set manually. |

SYNTAX OP (terminator)

EXPLANATIONAfter an OP command is received, the plotter will out­ put the coordinates of P1 and P2 in plotter units as four integers in ASCII in the following form:

<!-- formula-not-decoded -->

where [TERM]is the output terminator for your system. See Terms You Should Understand in Chapter 7.

The range of the integers is determined by the setting of the paper switch as shown below:

<!-- formula-not-decoded -->

Upon completion of output, bit position 1 of the output status byte is cleared.

## The Scale Instruction, SC

DESCRIPHUN The scale instruction, SC, establishes a user-unit coordi­ nate system by mapping values onto the scaling points P1 and P2.

This instruction is used to enable you to plot in user units con­ venient to your application. For instance, if your X values represent months, then Xmin= 1 and Xmax= 12. If the values for Y-coordinates all lay between 0 and 10, you might use 0 as Yminand 10 as Ymax.By adjusting your minimum and maximum values, you can provide addi­ tional room for labeling. If your plot is a 12-month bar chart with Y­ coordinates 0 to 10, you might scale the X-axis 0 to 14 so the first and last bars are not at the edge of the graph, and scale the Y-axis Oto 12 leaving room for a title at the top. con-

## SYNTAX

SC Xmin,Xmax,Ymin,Ymax(terminator)

or

SC (terminator)
