AR X-increment,Y-increment,arc angle(,chord angle);

Purpose:

Draws arc of specified number of degrees with specified smoothness; centered relative to current pen position, using current pen status (up or down).

Parameters:

X- and Y-increments -integer, in plotter units unless scaling in effect;then in user units.

are angle -integer, negative value specifies clockwise are, positive value specifies counterclockwise arc.

chord angle -integer, defines arc smoothness in degrees. Default is 5 degrees.

## CA The Designate Alternative Character Set

## Instruction Page 5-4

CA n( ;)

Purpose:

Designates the alternate character set.

Parameter:

integer 0 through 4; default set 0.

## CI* The Circle Instruction

CI radius(,chord angle);

Purpose:

Draws a circle of specified radius centered at current pen position.

Parameters:

radius -integer, in plotter units unless scaling in effect; then in user units. Starting point at 0 degrees with positive parameter; 180degrees withnegative parameter.

chord angle -integer, defines circle smoothness in de­ grees. Default is 5 degrees.

## CP TheCharacter Plot Instruction

CP spaces, lines;

Movethe pen the number of spaces and lines specified.

spaces -decimal, 2 -128 and &lt; 128, number of CP spaces, positive value moves pen in current label direc­ tion, negative value moves pen in opposite direction.

lines -- decimal, 2 -128 and &lt; 128, number of CP lines, positive value moves pen up, negative value moves pen down in relation to current label direction.

Purpose:

Parameters:

Omitting parameters causes carriage return, line feed.

*Available only with RS-232-Cplotters that have the serial prefix number 2308Aor higher.

Page 5-13

Page 3-12
