LB c . . . c t

Purpose:

Draws the character string using the currently selected character set.

Parameters:

c...c -ASCII characters which may include control characters.

Terminator:

t -- label terminator defined by DT. Default is ETX, decimal 3.

## LT The Line Type Instruction

LT pattern number (,pattern length) (;)

Purpose:

Sets the line type used in drawing lines.

Parameters:

pattern number -integer between 0 and +6. Omitting parameter causes solid line.

0-specifies dots only at the points that are plotted.

<!-- image -->

pattern length -decimal, 0 to 127.9999,a percentage of diagonal distance between P1 and P2. Default 4%.

0A The Output Actual Position and Page 7-3

## Pen Status Instruction

0A (;)

Purpose:

Used to output the pen's physical position at time of command.

Response:

X,Y,P [TERM] -integers, in ASCII.

X,Y-in plotter units within current window.

P -0, pen up or 1, pen down.

Page4-6
