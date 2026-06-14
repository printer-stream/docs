since initialization, pen up is assumed. If no line type has been commanded, a solid line is drawn. 

Arcs are drawn within the defined window, with clipping occurring outside the window limits. Drawing arcs within the window conforms to the definitions given for plotting under the PA instruction. 

All parameters must be integers in the range —32 768 to 32 767. Specifying out-of-range parameters sets error 3 and the command is ignored. 

The following BASIC program demonstrates the use of the AA instruction. 

10 PRINTER IS 10 20 PRINT "IN; SP1;1P2650,1325,7650,6325;" 30 =PRINT "SCO,100,0,100;" 40 PRINT "PAO,20;" 50 PRINT "PDO; PAO, 40;AAO,50,180;PA0,80;" 60 PRINT "AAO, 100,90; PA40, 100; ARSC, 100,180; PRBO, 1 a0;" 70. PRINT "AA100, 100,90; FA100,60;AR100, 50, 180;PA100, 20;" BO PRINT "AA1O0,0,90;PAEO,0;ARSO,0, 180;PA20,0;ARO,0,90;" g0 PRINT “PU; PASO,50;CI30;" 100, END 

- Line 10 defines the select code of the interface; change this statement as necessary for your computer. 

Lines 20 and 30 initialize the plotter and establish user-unit scaling. 

- Lines 40 and 50 move the pen to the point 0,20, lower the pen, and draw to the point 0,40, where a 180-degree.arc is drawn counterclockwise, centered at 0,50. The pen is then instructed to draw to the point 0,80. 

- Lines 60 through 90 continue drawing the figure, clockwise, back to the point 0,20, and finish with the circle centered at the point 50,50. 

3-18 CONTROLLING THE PEN AND PLOTTING 
