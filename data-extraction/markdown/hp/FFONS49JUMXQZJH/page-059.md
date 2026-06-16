The Arc Relative Instruction, AR

<!-- image -->

DESCRIPTHJNThe are relative instruction, AR, provides the means to draw an arc with the center point located relative to the present pen position. The are can be drawn clockwise (CW) or counterclockwise (CCW),with a specified are angle and chord angle. It is only included in the instruction set of RS-232-C plotters that have the serial prefix number 2308A or higher.

M The instruction can be used to draw an arc of any radius, length, and smoothness with a single command. The are is drawn from the current pen position, and its center point is located by relative X,Y coordinates. |

SYNTAX

AR

X-increment, Y-increment, arc angle

(, chord angle)

terminator

<!-- image -->
