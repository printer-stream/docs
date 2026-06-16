A default instruction, DF, or an initialize instruction, IN, will also reset the velocity and acceleration to the values 38.1 cm/s and 2 g.

## The Plot Absolute Instruction, PA

DESCRIPHDN The plot absolute instruction, PA, moves the pen to the point(s) specified by the Xand Y-coordinate parameters.

M The instruction can be usedtogether with PD to draw lines or with PU to move the pen to a specific point on the plot. The instruction can be executed without parameters to establish absolute plotting, as opposed to relative plotting for PU or PD commands with parameters. In this case, the parameters of PU and PD are interpreted as absolute X,Ycoordinates until any PR command is received. |

PA

X1coordinate,Y1 coordinate (,X2 CO0I'dinate,Y2 coordinate,...,Xn coordinate, Yncoordinate)(terminator) or Y2

PA (terminator)

EXPLANATIONRecommended parameters are decimal numbers be­ tween -32768.0000 and 32 767.9999. When scaling is off, parameters are truncated to integers as follows:

- 0 For positive numbers, the fractional portion is discarded and the in­ teger portion remains unchanged. For example, both 1234.4 and 1234.9 become 1234.
- 0 For negative numbers, the fractional portion is discarded and the in­ teger portion is changed to the next more negative integer. For ex­ ample, both -1234.4and -1234.9 become -1235. Since you cannot plot to negative values unless scaling is on, (in which case decimal portions of parameters are used), the only time you will observe this is when you use the output commanded position and pen status instruction, OC, and the last X-and/ or Y-parameter sent was negative.

NOTE: If you have an HP-IB or RS-232-Cplotter that has the serial prefix number 2308A, or higher, or if you have an HP-IL plotter, you will not observe this truncation with the OC instruction. In these plotters, the OC instruction returns decimal parameters instead of integer parameters when scaling is in effect.I

When scaling is on, any fractional portion of a parameter is used.

APAcommand without parameters sets absolute plotting mode for PU and PD commands with parameters.

When parameters are included with a PA command, both coordinates of an X,Ycoordinate pair must be given. An odd number of parameters

## 3-4 CONTROLLING THE PEN AND PLOTTING
