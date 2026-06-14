The first routine performs the following tasks: 

1. Obtains, in plotter units, the coordinates of the corners of the bar. 

2. Turns scaling off so plotting is in plotter units. This routine can, therefore, be used in any program, and there is no need to recompute the increment P for different scaling in different graphs. 

3. Beginning at the X,Ymin value, draws a line to the top of the bar, moves over slightly less than one pen width, and draws to the bottom of the bar. 

4. Increments the X-value one pen width and repeats step 3 until the bar is filled. 

5. Rescales the plot to the original scaling. 

The second routine repeatedly moves with the pen up to the X-coordinate at the base of the bar and drawsa line to the top of the bar. All fill lines are drawn in the same direction. 

## Segment 1 — Plotting on Paper 

120 PRINT "PAZ.7,0,PD,2.7,18,3.3,18,3.3,0,2.7,0;PUs" 130 PRINT "CA;" 140 ENTER 705 ; A,B,C 150 PRINT "PA2.7,18;0A;" 160 ENTER 705 ; L,€,F 170 PRINT “PA3.3,18;0R;" 180 ENTER 705 3; G,H,I 190 PRINT "PAZ. ?,0;5C;" 200 P20 210 FOR *=A TO G-P STEP 2*P 230220 PRINTPRINT "PI""PO"SX;3x4+P3E3X+P3BB;X;€ 240 NEXT & Z50 PRINT "PU;SC1,12,0,150;" 2 — Plotting on — Plotting on Plotting on on Transparency Film Film 120 PRINT "PAZ.7,0,PU,2.7,18,9.3,18,3.3,0,2.7,0;PU;" 130 PRINT "GA;" 140 ENTER 705 ; A,B,C 150 PRINT "PA2.7,18;0A;" 160 ENTER 705 ; D,€,F 170 PRINT "PA3.3,18;0R;" 180 ENTER 705 ; G,H,I 190 PRINT "PR2.7,0;SC;" 200 P=20 210 FOR X=R TO G STEP P 220 PRINT "PU"; X;B3"PD" 3 X3E 230 NEXT X 240 PRINT "PU;SC1,12,0,150;" 

## Segment 2 — Plotting on — Plotting on Plotting on on Transparency Film Film 

PUTTING THE COMMANDS TO WORK 8-11 
