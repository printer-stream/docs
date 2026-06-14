## Setting P1 and P2 Manually 

- P2 moves when P1 is moved manually. If you want P2 to be at a specific location, set P1 first and then P2. If you want to establish an area of a certain size onto which the parameters of a scale instruction will be mapped, you may set P2 in the desired location relative to the current P1, and then move P1. P2 will move to a corresponding location so that both the X- and Y-distances between P1 and P2 remain constant. If such a move means the new location of P2 will be beyond the plotting area, either or both coordinates of P2 are set to the plotting limits. In this case, the size of the rectangle established by P1 and P2 will, of course, not remain the same. A detailed description, including illustrations, is contained in the HP 7470 Operator’s Manual. 

To set Pl or P2 manually: 

1. Move the pen to the desired location using the front panel arrow buttons. 

2. Press ENTER simultaneously with P1 or P2. If ENTER is not held down, the pen will merely move to P1 or P2 and no change in the location of P1 or P2 will occur. 

3. Check the new locations of the scaling points by pressing P1; then press P2. 

The Input P1 and P2 Instruction, IP DESCRIPTION Miwirs input Pl and P2 instruction, IP, provides the means to relocate P1 and P2 through program control. | USES | The IP instruction is often used to ensure that a plot is always the same size, especially when the user and programmer are not the same person. It establishes program control of plot size and label direction. This instruction can also be used to move the scaling points Pl and P2 from their default or current locations; to give mirror images of vectors and. labels; to change the size of a user unit, thus reducing or enlarging an image; to change the size or direction of labels when relative character size or direction is in effect; and to set Pl and P2 back to their default locations. 

## SOIERS =P P1x,Ply (, P2x,P2y) (terminator) or IP (terminator) 

ateEE §=The new coordinates of P1 and P2 are specified in the order shown above and must be in absolute plotter units. Parameters should be > 0 and within the maximum plotting area. This means 0 < X < 10 300 when the paper switch is set to us; 0 < x < 10 900 if the paper switch is set to A4; and 0 < Y < 7650 for either setting. 2-4 ESTABLISHING BOUNDARIES AND UNITS 
