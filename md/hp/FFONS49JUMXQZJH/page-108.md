The Output Commanded Position and Pen Status Instruction, OC HL =The output commanded position and pen status instruction, OC, is used to output the X- and Y-coordinates and pen status (up or down) associated with the last valid pen position command. 

| USES | This instruction can be used to determine the pen’s last valid commanded position in plotter units or user units depending on whether scaling is off or on. You might use that information to position a label or figure, or determine the parameters of an instruction which moved the pen to the limits of some window. SUEDE = OC (terminator) eV §=Output is in decimal format, in user units when scaling is in effect, and in plotter units when scaling is off. 

No parameters are used. The instruction will execute even if no terminator is received. 

The pen position and status are output to the computer as decimal numbers in ASCII in the form: 

## X, Y,P [TERM] 

where X is always the X-coordinate in plotter units or user units, Y is always the Y-coordinate in plotter units or user units, P is the pen status (0 = pen up, 1 = pen down), and [TERM] is the output terminator for the interface installed. 

When scaling is off, X- and Y-coordinates are in plotter units. When scaling is on, X- and Y-coordinates are in user units. Ranges of the X-and Y-coordinates are —32 768 to 32 767 whether scaling is on or off. 

NOTE: If you have an HP-IB or RS-232-C plotter that has the serial prefix number 2308a or higher, or if you have an HP-IL plotter, output is in decimal format as described above. All HP-IB or RS-232-C plotters with a lower prefix serial number output integer parameters, as follows. When scaling is on, X- and Y-coordinates are always rounded to the nearest integer value. Thus, while plotting can occur to noninteger values, output of pen position can only be obtained to the nearest integer value. @ 

When the commanded pen position is such that its user unit value would be less than —32 768 or greater than 32 767, the output may not represent the true pen position. If the plotter were scaled with the given instructions as shown in the following illustration, all points in the lightly shaded area will have one coordinate as 32 767, the largest number the plotter can output. All points in the darker shaded area will have both coordinates as 32 767. 

7-4. OBTAINING INFORMATION FROM THE PLOTTER 
