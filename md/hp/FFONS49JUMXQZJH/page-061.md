- Line 40 moves the pen to the point ~80,—50, draws a 90-degree CCW arc centered 0,80 units relative to the present pen position, then draws a 90-degree arc centered 80,0 units relative to the 0,30 absolute pen position. Note that a pen down command, PD, is required to draw the arc. 

**==> picture [361 x 164] intentionally omitted <==**

**----- Start of picture text -----**<br>
(-80,30) [> (0,30)HOHH HH 77 180,30)<br>{<br>| [|]<br>|<br>|i<br>|<br>\ [|]<br>I<br>||<br>I|<br>| I<br>800) (80,-50)<br>**----- End of picture text -----**<br>


- 1¢ PRINTER IS 10 20 PRINT “IN; SP1;1IP2650, 1325, 7650,6325;" 30 PRINT "SC-100,100,-100,100;" 40 PRINT "PA-100,40;PD;PR60, 0;ARO, -40, -90; AR4O, 0, 90; PREG, 0; PU;" 50 END 

In this example, line 40 moves the pen to the point —100,40, lowers the pen, and plots 60,0 units relative to the previous pen position, —100,40. It then draws a 90-degree CW arc centered at 0,—40 units relative to the new —40,40 pen position, and follows it with a 90-degree CCW arc centered 40,0 units relative to the 0,0 pen position, the endpoint of the first arc. Finally, it plots 60,0 units relative to the pen position 40,—40, the endpoint of the second arc. 

**==> picture [345 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
(-100,40) (-40,40)<br>I<br>I<br>l<br>I<br>l<br>l<br>$ (0,0) (40,0)<br>(-40,0) ¢<br>1<br>I<br>|<br>|<br>! (100,-40)<br>(40,-40)<br>**----- End of picture text -----**<br>


CONTROLLING THE PEN AND PLOTTING 3-21 
