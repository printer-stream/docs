## The Circle Instruction, CI 7

DESCRIPHDN The circle instruction, CI, provides the means to draw a circle of a specified radius and chord angle. It is only included in the instruction set of RS-232-Cplotters that have the serial prefix number 2308Aor higher.

USES The instruction can be used to generate circles with a single command. All computations are internal to the plotter to reduce com­ puter overhead.

SYNTAX CI radius (, chord angle) terminator

<!-- image -->

EXPLANATIONThe radius parameter can be a positive or negative number in integer format. Its sign defines the starting point of the Circle:a circle with a positive radius starts at the 0-degree point; a circle with a negative radius starts at the 180-degree point. The current pen position is the Center of the circle. If scaling is off, the radius is in plotter units. If scaling is on, the radius is in user units. If user units are not the same size in the X-and Y-directions, ellipses will be drawn.

The chord angle parameter is in integer format and governs the smoothness of the circle. It is interpreted as degrees and sets the maximum angle subtended by a chord that is drawn to represent an arc segment of the circle, as shown below. The actual angle used may be changed by the plotter so that all chords are the same length. The sign of the parameter is ignored, except to set the maximum 1n-range limit to -32768 or +32 767.
