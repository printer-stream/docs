Page 3-19 

## AR* The Arc Relative Instruction 

   - AR X-increment,Y-increment,arc angle(,chord angle); Purpose: Draws arc of specified number of degrees with specified smoothness; centered relative to current pen position, using current pen status (up or down). 

   - Parameters: X- and Y-increments — integer, in plotter units unless scaling in effect; then in user units. arc angle — integer, negative value specifies clockwise arc, positive value specifies counterclockwise arc. chord angle — integer, defines arc smoothness in degrees. Default is 5 degrees. 

- CA The Designate Alternative Character Set Instruction 

**==> picture [39 x 13] intentionally omitted <==**

**----- Start of picture text -----**<br>
Page 5-4<br>**----- End of picture text -----**<br>


   - CA n(;) Purpose: Designates the alternate character set. Parameter: integer 0 through 4; default set 0. 

- CI* The Circle Instruction Page 3-12 CI radius(,chord angle); Purpose: Draws a circle of specified radius centered at current pen position. 

- Parameters: radius — integer, in plotter units unless scaling in effect; then in user units. Starting point at 0 degrees with positive parameter; 180 degrees with negative parameter. chord angle — integer, defines circle smoothness in degrees. Default is 5 degrees. 

- CP The Character Plot Instruction 

   - Page 5-18 

- CP spaces, lines; Purpose: Move the pen the number of spaces and lines specified. Parameters: spaces — decimal, = —128 and < 128, number of CP spaces, positive value moves pen in current label direction, negative value moves pen in opposite direction. lines — decimal, = —128 and < 128, number of CP lines, positive value moves pen up, negative value moves pen down in relation to current label direction. 

Omitting parameters causes carriage return, line feed. 

- *Available only with RS-232-C plotters that have the serial prefix number 2308A or higher. 

B-2 INSTRUCTION SYNTAX 
