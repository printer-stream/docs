PA X1coordinate, Y1coordinate (X2coordinate, Y2coordinate, . . ., Xn coordinate, Yncoordinate) (;) ...,

or

PA (;)

Purpose:

Parameters:

Plots to the X,Ycoordinates in the order listed using the current pen up/ down status. PA; sets absolute plotting.

Pairs of integers representing plotter units if scaling not in effect, otherwise user units, integers or decimals.

## PD The Pen Down Instruction

- PD (;)

OI'

PD X1coordinate, Y1coordinate ( , . . . Xn, Yn coordinates) (;)

Purpose:

Programmatically lowers the pen. Parameters may be included as in PA or PR.

## PR The Plot Relative Instruction

Page 3-8

- PR X1increment, Y1increment (,X2 increment, Y2increment, . . ., Xn increment, Ynincrement) (;) ...,

or

PR (;)

Purpose:

Parameters:

Plots, in order, to the points indicated by the X,Yincre­ ments, relative to the previous pen position. PR; sets rela­ tive plotting for PU or PD with parameters.

Pairs of integers representing plotter units if scaling is not in effect, otherwise user units, integers or decimals.

## PU The Pen Up Instruction

- PU (;)

or

PU X1coordinate, Y1coordinate( , . . . Xn, Yncoordinates) ( ; )

Programmatically raises the pen. Parameters may be in­

cluded as in PA or PR. Purpose:

Page3-2

Page3-2
