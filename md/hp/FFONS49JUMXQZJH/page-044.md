A default instruction, DF, or an initialize instruction, IN, will also reset the velocity and acceleration to the values 38.1 cm/s and 2 g. 

The Plot Absolute Instruction, PA DESCRIPTION Miawers plot absolute instruction, PA, moves the pen to the point(s) specified by the X- and Y-coordinate parameters. | USES | The instruction can be used together with PD to draw lines or with PU to move the pen to a specific point on the plot. The instruction can be executed without parameters to establish absolute plotting, as opposed to relative plotting for PU or PD commands with parameters. In this case, the parameters of PU and PD are interpreted as absolute XY coordinates until any PR command is received. 

## SMES 

   - §=PA Xi coordinate,Y1 coordinate (,X2 coordinate,Y2 coordinate,...,Xn coordinate, Yn coordinate)(terminator) or 

- PA (terminator) 

- ie LEU }=Recommended parameters are decimal numbers be- 

- tween —32 768.0000 and 32 767.9999. When scaling is off, parameters are truncated to integers as follows: e For positive numbers, the fractional portion is discarded and the integer portion remains unchanged. For example, both 1234.4 and 1234.9 become 1234. 

- e For negative numbers, the fractional portion is discarded and the integer portion is changed to the next more negative integer. For example, both —1234.4 and —1234.9 become —1235. Since you cannot plot to negative values unless scaling is on, (in which case decimal portions of parameters are used), the only time you will observe this is when you use the output commanded position and pen status instruction, OC, and the last X- and/or Y-parameter sent was negative. 

NOTE: If you have an HP-IB or RS-232-C plotter that has the serial prefix number 2308, or higher, or if you have an HP-IL plotter, you will not observe this truncation with the OC instruction. In these plotters, the OC instruction returns decimal parameters instead of integer parameters when scaling is in effect. m 

When scaling is on, any fractional portion of a parameter is used. 

A PA command without parameters sets absolute plotting mode for PU and PD commands with parameters. 

When parameters are included with a PA command, both coordinates of an XY coordinate pair must be given. An odd number of parameters 3-4 CONTROLLING THE PEN AND PLOTTING 
