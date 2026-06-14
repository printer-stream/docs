. ; 

**==> picture [186 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
(0.80)<br>CIRCLE CENTER<br>(50,50)<br>+180° ARC@ @<br>(0,50)<br>(0,40)<br>START<br>(0,20)<br>**----- End of picture text -----**<br>


The Arc Relative Instruction, AR WHE §=6The arc relative instruction, AR, provides the means to draw an arc with the center point located relative to the present pen position. The are can be drawn clockwise (CW) or counterclockwise (CCW), with a specified arc angle and chord angle. It is only included in the instruction set of RS-232-C plotters that have the serial prefix number 2308A or higher. 

| USES | The instruction can be used to draw an arc of any radius, length, and smoothness with a single command. The arc is drawn from the current pen position, and its center point is located by relative X,Y coordinates. 

SYNTAX We X-increment, Y-increment, arc angle (, chord angle) terminator 

**==> picture [315 x 92] intentionally omitted <==**

**----- Start of picture text -----**<br>
CHORD ooeee | Y- 7 ——— CHORD<br>INCREMENT d<br>Y- INCREMENT aN<br>ANcre-y COORDINATE = (anc CENTER)<br>\ {ARC CENTER) y CHORDANGLE<br>**----- End of picture text -----**<br>


CONTROLLING THE PEN AND PLOTTING 3-19 
