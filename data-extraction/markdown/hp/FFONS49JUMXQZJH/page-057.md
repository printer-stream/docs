## The Arc Absolute Instruction, AA

DESCRIPTIONThe are absolute instruction, AA, provides the means to draw an arc with the center point located at a specified absolute point. The are can be drawn clockwise (CW)or counterclockwise (CCW), subtends the specified are angle, and conforms to the specified or default chord angle. It is only included in the instruction set of RS-232-C plotters that have the serial prefix number 2308A or higher.

M The instruction can be used to draw an arc of any radius, length, and smoothness with a single command. The are is drawn from the current pen position, and its center point is located by absolute X,Y coordinates. |

SYNTAX AA X-coordinate,Y-coordinate, arc angle (, chord angle) terminator

<!-- image -->

EXPLANATIONThe AA instruction requires that both X- and Y­ coordinates be specified (coordinate pair) in integer format. They are interpreted as plotter units if scaling is off or as user units if scaling is on. The X- and Y-coordinateslocate the center of the arc and may be located on or off the plotting surface. The current pen position is the starting point of the arc.

The are angle is in integer format. It is the angle, in degrees, through which the arc is drawn: a positive arc angle draws CCW from the current pen position; a negative arc angle draws CWfrom the current pen position.

The chord angle parameter is in integer format and governs the smoothness of the arc in the same way as defined under the circle instruction, CI. The sign of the parameter is ignored, except to set the maximum in-range limit to -32 768or +82 767.The default chord angle is 5 degrees.

Unlike circles, arcs are drawn using the previously commanded pen state (up or down) and line type. If no pen state has been commanded
