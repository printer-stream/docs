**==> picture [109 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
45 DEGREE CHORD ANGLE<br>**----- End of picture text -----**<br>


**==> picture [109 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
30 DEGREE CHORD ANGLE<br>**----- End of picture text -----**<br>


15 DEGREE CHORD ANGLE 

**==> picture [105 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
5 DEGREE CHORD ANGLE<br>**----- End of picture text -----**<br>


The circle instruction includes an automatic pen down feature. When a circle command is received, the pen lifts (if it was down), moves from the center of the circle to the circle starting point on the circumference, lowers the pen, draws the circle, then returns, pen up, to the center of the circle. After drawing the circle, the pen assumes the pen state (up or down) that was in effect prior to the circle command. To avoid drawing lines to the center of the circle, move to and away from the circle’s center with the pen up. 

Circles are drawn within the defined window, with clipping occurring outside the window limits. Drawing circles within the window conforms to the definitions given for plotting under the PA instruction. 

Each chord of the circle is drawn using the currently defined line type. Refer to The Line Type Instruction, LT, in Chapter 4. 

To demonstrate some of the features of the circle instruction, the following strings of HP-GL instructions draw various circles with different line types, radii, and starting points. 

- "IM; SP1;IPZ650,1325,7650,639255" 

"SC-100,100,-100,100;" “PAO,OSLT;CI10, SiLTO;CI-20,5;LT1;C130,5;" "LT23;CI-40,5;LT3;CI50,5;LT4;CI-60,5;LT5; CL1?0,5;LT6;CI8s0,5;" 

3-14. CONTROLLING THE PEN AND PLOTTING 
