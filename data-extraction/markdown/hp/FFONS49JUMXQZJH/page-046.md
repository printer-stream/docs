- 0 execution of a DF command, or
- 0 execution of a PA instruction with or without parameters.

The pen moves and draws lines only within the currently defined window. Refer to The Input Window Instruction, IW,in Chapter 1.

The plotter discards parameters which are out of range. Error 3 will be set (parameter out of range). A PA command with out-of-range param­ eters will still establish plot absolute mode for future occurrences of PU or PD with parameters. When scaling is off, in-rangeparameters are greater than or equal to -32 768and less than or equal to 32 767.When scaling is on, both the parameters and their plotter unit equivalent must also be in that same range. Tofind the plotter unit equivalent, use the equations in the section Scaling Without Using the SC Instruction in Appendix C.

There are four types of vectors that can be drawn with a PA command from a given last point to some new point.

## LAST POINT

## NEW POINT

- inside window area to inside window area
- inside window area to outside window area \_ \_
- outside window area to inside window area .C'°.N'!'
4. outside window area to outside window area

In type one, the pen moves from the last point to the new point with the pen up or down as programmed.

In type two, the pen moves from the last point toward the new point and stops where the line between the two points intersects the current window. The pen up/ down condition is as programmed until the inter­ section is reached. Then, the pen is raised.

In type three, the pen moves with the pen up, to the point where the straight line between the last and new point intersects the window limit. When the pen reaches this point, the pen assumes its programmed (up or down) position. The pen then moves to the new point.

In type four, no pen movement occurs unless the straight line between the last and new point intersects the window. The Xand Y-coordinates of the current pen position are updated. If part of the vector is in the window area, the pen moves, pen up, to the point where the line be­ tween the last and the new point first intersects the window limit. The pen moves under programmed pen up/ down control to the intersection of the vector and the other window limit. At this point, the pen stops and lifts.

Since out-of-range points are discarded, the plotter will draw a line be­ tween the two points on either side of discarded points. Youcan be sure all lines on your plot represent actual data if you:

1. have not changed the error mask from its default setting;

## 3-6 CONTROLLING THE PEN AND PLOTTING
