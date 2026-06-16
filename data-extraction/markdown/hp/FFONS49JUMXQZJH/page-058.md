since initialization, pen up is assumed. If no line type has been commanded, a solid line is drawn.

Arcs are drawn within the defined window, with clipping occurring outside the window limits. Drawing arcs within the window conforms to the definitions given for plotting under the PA instruction.

All parameters must be integers in the range -32 768to 32767.Specify­ ing out-of-rangeparameters sets error 3 and the command is ignored.

The following BASIC program demonstrates the use of the AA instruction.

```
10 PRINTER IS 10 20 PRINT'IN;SP1;IP2E50,1325,?ESO,B325;' 30 PRINT'sco,1oo,o,1o0;' 40 PRINT 'PHO,20;' 50 PRINT'Pu;PPo,40;PRo,5o,1e0;PP0,so;' so PRINT 'HHD,100,SO;PH4U,100;HH50,100,130;PHBO,100;' ?0 PRINT"P9100,1oo,9o;PP1oo,so;PP1oo,50,1eo;PP1oo,2o;' 30 PRINT"PR1oo,o,9o;PP5o,o;RP5o,o,1ao;PP2o,o;aao,o,9o;" so PRINT'PU;PH50,50;CI30;' 100 END
```

Line 10 defines the select code of the interface; change this statement as necessary for your computer.

Lines 20 and 30initialize the plotter and establish user-unit scaling.

Lines 40 and 50 move the pen to the point 0,20,lower the pen, and draw to the point 0,40, where a 180-degree.arc is drawn counterclockwise, centered at 0,50.The pen is then instructed to draw to the point 0,80.

Lines 60 through 90continue drawing the figure, clockwise,back to the point 0,20, and finish with the circle centered at the point 50,50.
