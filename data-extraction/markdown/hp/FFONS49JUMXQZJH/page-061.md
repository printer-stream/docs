Line 40 moves the pen to the point ~80,*50, draws a 90-degree CCW are centered 0,80 units relative to the present pen position, then draws a 90-degree are centered 80,0 units relative to the 0,30 absolute pen posi­ tion. Note that a pen down command, PD, is required to draw the arc.

-l (80,30)

<!-- image -->

In this example, line 40 moves the pen to the point -100,40, lowers the pen, and plots 60,0 units relative to the previous pen position, -100,40. It then draws a 90-degree CW are centered at 0,-40 units relative to the new -40,40pen position, and follows it with a 90-degreeCCW are centered 40,0 units relative to the 0,0 pen position, the endpoint of the first arc. Finally, it plots 60,0 units relative to the pen position 40,-40, the endpoint of the second arc.

<!-- image -->
