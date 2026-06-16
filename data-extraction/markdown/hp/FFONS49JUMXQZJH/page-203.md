00 (;)

Purpose:

Response:

Used to output features implemented on the plotter.

<!-- image -->

## OP The Output P1 and P2 Instruction

OP (;)

Purpose:

Used to output the plotter unit coordinates of the scaling points P1 and P2.

Response:

Plx, Ply, P2X,P2y [TERM] -four integers in ASCII.

Range -dependent on settings of paper switch.

US

0 &lt; X-coordinate S 10 300

0 S Y-coordinate &lt; 7650

A4

0 &lt; X-coordinate&lt; 10 900

0 &lt; Y-c0ordinate&lt; 7650

## OS The Output Status Instruction

08 (;)

Purpose:

Used to output the p1otter'sstatus.

Response:

status [TERM] -integer in ASCII in the range 0 to 255. Power-onstatus, 24.

## OW The Output Window Instruction Page2-10

OW (;)

Purpose:

Used to output the"plotter unit coordinates of the lower­ left and upper-right corners of the current window.

Response:

Xlower left, Ylowerleft, Xupper right, Yupperright [TERM] - integers in ASCII. Range same as OP.

Page7-8

## Page2-5
