## Scaling Without Using the SC Instruction 

The 7470 plotter movements are in terms of plotter units where a plotter unit = 0.025 mm. While the plotter can be scaled into user units using the SC command, it may be convenient for you to write programs where numbers to be plotted are in some units other than plotter units. These “user units” can be converted into plotter units by the computer using the following equations: 

**==> picture [225 x 68] intentionally omitted <==**

**----- Start of picture text -----**<br>
P2x — Pl P2, — Pl<br>Xscaled = os Ax + Plx - Ulx ox *<br>U2, — Ulx U2x — Ulx<br>P2y - Pl P2y —Pl<br>Yscaled = a“y_ oy Ay + Ply _ Uly oy TY<br>**----- End of picture text -----**<br>


where: Ax is the X-coordinate of the desired point in user units, Ay is the Y-coordinate of the desired point in user units, Pix is the X-coordinate of P1 in plotter units, Ply is the Y-coordinate of P1 in plotter units, P2x is the X-coordinate of P2 in plotter units, P2y is the Y-coordinate of P2 in plotter units, U1x is the X-coordinate of P1 in user units, Uly is the Y-coordinate of P1 in user units, U2x is the X-coordinate of P2 in user units, and U2y is the Y-coordinate of P2 in user units. 

To demonstrate the use of the scaling equations, let’s go through an example. 

## Example 1: 

## Problem 

Scale the platen area (P1 = 250,279 and P2=10 250,7479) into user units where P1 =0,0 and P2= 25 000,18 000. At the center point (X = 12500, Y = 9000), draw a circle with radius 2500 as follows: 

C-2. REFERENCE MATERIAL 
