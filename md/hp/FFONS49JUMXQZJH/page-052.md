The Circle Instruction, CI STH §=The circle instruction, CI, provides the means to draw a circle of a specified radius and chord angle. It is only included in the instruction set of RS-232-C plotters that have the serial prefix number 2308A or higher. 

UNS = The instruction can be used to generate circles with a single command. All computations are internal to the plotter to reduce computer overhead. SYNTAX B@aetstuts (, chord angle) terminator 

**==> picture [331 x 182] intentionally omitted <==**

**----- Start of picture text -----**<br>
90°<br>CIRCLE<br>STARTING POINT:<br>RADIUS +<br>180° —— —- 0”<br>STARTINGCIRCLEPOINT: TS<br>RADIUS -<br>| CURRENT PEN POSITION<br>270°<br>**----- End of picture text -----**<br>


MeL §=The radius parameter can be a positive or negative number in integer format. Its sign defines the starting point of the circle: a circle with a positive radius starts at the 0-degree point; a circle with a negative radius starts at the 180-degree point. The current pen position is the center of the circle. If scaling is off, the radius is in plotter units. If scaling is on, the radius is in user units. If user units are not the same size in the X- and Y-directions, ellipses will be drawn. 

The chord angle parameter is in integer format and governs the smoothness of the circle. It is interpreted as degrees and sets the maximum angle subtended by a chord that is drawn to represent an are segment of the circle, as shown below. The actual angle used may be changed by the plotter so that all chords are the same length. The sign of the parameter is ignored, except to set the maximum in-range limit to —32 768 or +32 767. 

3-12 CONTROLLING THE PEN AND PLOTTING 
