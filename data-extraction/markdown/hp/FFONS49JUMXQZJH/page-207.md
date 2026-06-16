## UC*The User Defined Character Instruction Page 5-19

UC (pen control ,) X-increment, Y-increment(,...) (, pen control) (, . . .) ;

Purpose:

Draws characters or symbols defined by user.

Parameters:

pen control -2 +99 pen down or &lt; -99 pen up.

X-increment, Y-increment in grid units, range, i 98 grid units.

Omitting parameters causes the pen to move one character-space field to the right.

## VS The VelocitySelect Instruction

Page 3-3

VS pen velocity (;)

Sets the pen velocity.

decimal, Oto 127.9999.

Purpose:

Parameters:

pen velocity -- 1 through 38.1 interpreted as cm/ s. De­ faults to velocity of 38.1 cm/s, acceleration of 2 g. Any velocity parameter slows acceleration to 0.5 g.

## XT The X-Tick Instruction

- XT (;)

Purpose:

Page4-2

Draws a vertical tick mark of the length specified by the TL instruction at the current pen position.

## YT The Y-Tick Instruction

- YT (;)

Purpose:

Page4-2

Draws a horizontal tick mark of the length specified by the TL instruction at the current pen position.

*Not available with Option O03.
