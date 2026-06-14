Page 5-19 

## UC* The User Defined Character Instruction 

- UC (pen control ,) X-increment, Y-increment (,...) (, pen control) (...) 5 

Purpose: Draws characters or symbols defined by user. Parameters: pen control — > +99 pen down or < —99 pen up. 

X-increment, Y-increment in grid units, range, + 98 grid units. 

Omitting parameters causes the pen to move one character-space field to the right. 

## VS The Velocity Select Instruction 

Page 3-3 

VS pen velocity (;) Purpose: Sets the pen velocity. 

Parameters: decimal, 0 to 127.9999. 

pen velocity — 1 through 38.1 interpreted as cm/s. Defaults to velocity of 38.1 cm/s, acceleration of 2 g. Any velocity parameter slows acceleration to 0.5 g. 

## XT The X-Tick Instruction 

- XT 

- (;) 

## Page 4-2 

Purpose: Drawsa vertical tick mark of the length specified by the TL instruction at the current pen position. 

## YT The Y-Tick Instruction 

## Page 4-2 

YT (;) Purpose: Draws a horizontal tick mark of the length specified by the TL instruction at the current pen position. 

*Not available with Option 003. 

INSTRUCTION SYNTAX B-11 
