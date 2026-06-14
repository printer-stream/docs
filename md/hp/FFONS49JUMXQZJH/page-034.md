| USES | The instruction can be used to determine the position of P1 and P2 in plotter units. This information can be used with the input window command, IW, to set the window to P1 and P2 under program control, to compute the number of plotter units per user unit when scaling is on, or to determine the numeric coordinates of P1 and P2 when they have been set manually. 

SERS §=OP (terminator) AMEE =After an OP command is received, the plotter will output the coordinates of Pl and P2 in plotter units as four integers in ASCII in the following form: 

Plx,Ply,P2x,P2y [TERM] 

where [TERM] is the output terminator for your system. See Terms You Should Understand in Chapter 7. 

The range of the integers is determined by the setting of the paper switch as shown below: 

US A4 0<X< 10300 0< X< 10 900 0< Y< 7650 0<Y< 7650 

Upon completion of output, bit position 1 of the output status byte is cleared. 

## The Scale Instruction, SC 

NSSHUIMEULE §=The scale instruction, SC, establishes a user-unit coordinate system by mapping values onto the scaling points P1 and P2. | USES | This instruction is used to enable you to plot in user units convenient to your application. For instance, if your X values represent months, then Xmin = 1 and Xmax = 12. If the values for Y-coordinates all lay between 0 and 10, you might use 0 as Ymin and 10 as Ymax. By adjusting your minimum and maximum values, you can provide additional room for labeling. If your plot is a 12-month bar chart with Y- coordinates 0 to 10, you might scale the X-axis 0 to 14 so the first and last bars are not at the edge of the graph, and scale the Y-axis 0 to 12 leaving room for a title at the top. 

SYNTAX SC Xmin,Xmax, Ymin, Ymax (terminator) or SC (terminator) 

2-6 ESTABLISHING BOUNDARIES AND UNITS 
