## The Arc Absolute Instruction, AA 

SHEL §=The arc absolute instruction, AA, provides the means to draw an arc with the center point located at a specified absolute point. The arc can be drawn clockwise (CW) or counterclockwise (CCW), subtends the specified arc angle, and conforms to the specified or default chord angle. It is only included in the instruction set of RS-232-C plotters that have the serial prefix number 2308a or higher. 

. 

| USES } The instruction can be used to draw an arc of any radius, length, and smoothness with a single command. The arc is drawn from the current pen position, and its center point is located by absolute X,Y coordinates. 

SYNTAX BW) X-coordinate, Y-coordinate, arc angle (, chord angle) terminator 

**==> picture [330 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
COORDINATES (ARC CENTER)<br>cr CURRENT [POSITION]  PEN ABSOLUTE X, ¥<br>ANGLE<br>[ CHORD ARCANGLE<br>fN ABSOLUTE X,<br>COORDINATES CURRENT<br>(ARC CENTER) PEN<br>POSITION<br>ANGLE<br>\ CHORD<br>Ga Y<br>**----- End of picture text -----**<br>


Ae EUE §=The AA instruction requires that both X- and Y- coordinates be specified (coordinate pair) in integer format. They are interpreted as plotter units if scaling is off or as user units if sealing is on. The X- and Y-coordinates locate the center of the arc and may be located on or off the plotting surface. The current pen position is the starting point of the arc. 

. 

The arc angle is in integer format. It is the angle, in degrees, through which the arc is drawn: a positive are angle draws CCW from the current pen position; a negative arc angle draws CW from the current pen position. 

The chord angle parameter is in integer format and governs the smoothness of the arc in the same way as defined under the circle instruction, CI. The sign of the parameter is ignored, except to set the maximum in-range limit to —32 768 or +32 767. The default chord angle is 5 degrees. 

Unlike circles, arcs are drawn using the previously commanded pen state (up or down) and line type. If no pen state has been commanded 

CONTROLLING THE PEN AND PLOTTING 3-17 
