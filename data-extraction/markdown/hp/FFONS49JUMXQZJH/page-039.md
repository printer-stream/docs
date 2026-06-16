## AdvancedProgramming Tips

Many software packages read P1 and P2 and use these points to define the maximum plotting area. Youmay want to obtain the largest plot possible on the 7470. This is the area of the default window, as deter­ mined by the setting of the paper switch, not the area established by the default settings of P1 and P2. The first three lines of the following listing will read the window size and set P1 and P2 to these points, so that the largest area possible is used for plotting. In order to change the plotting area, this HP-GL routine should precede the PLOTTER IS statement when programming on HP desktop computers in AGL.

Sometimes you want more than one plot on a page. The rest of the instructions set the window to, and outline four separate areas. A small space has been left between each area by adding or subtracting a constant value from Xand Y-coordinates in the center of the total area. This program could be modified to divide the plotting area into thirds or into areas of any other size. Another application of windowing is shading rectangular areas for bar graphs. SeeAdvanced Programming Tips, Chapter 8.

```
'IN;DN' !INSERT LINE T0 REHD CUDRDIHHTES INTO H,B,C,D 'IP';H,B,C,D 'IN';H,E;C/2-100;D/2-100;'SP1;PH';H;B 'PD';C/2-100;B;C/2-100;D/2-100;H;p/2-100;H;B;'PU' 'IN';C/2+100;B;C;D/2-100;'SP2;PU';C/2+100;B 'PD';C;B;C,D/2-100;C/2+100;D/2-100;C/2+100;B;'PU' 'IN';C/2+100;D/2+100;C;D;'SP1;PH';C/2+100;Dx2+10O 'PD';C;D/2+100;C;D;C/2+100;D;C/2+100;D/2+100;'PU;' 'IN';H;D/2+100;C/2-100;D;'PU;SP2;PH';H;D/2+10O 'PD';C/2-100;D/2+100;C/2-100;U;H;D;H;D/2+100;'SPO;'
```

<!-- image -->

Reduced Plot
