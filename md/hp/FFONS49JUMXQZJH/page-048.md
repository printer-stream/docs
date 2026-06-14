This final example scales a square plotting area from 0 to 1 in each axis and draws a unit circle. This program should run on most BASIC systems. Change line 10 as necessary for your computer to define the plotter as the system printer. Also, if PI is not a function recognized by your computer, add a line before line 30 to define PI as a variable (PI = 8.1416). Lines 60 and 65 are necessary to limit the number of digits in the X- and Y-coordinates. This prevents the possibility of coordinates being sent to the plotter in scientific notation, which sets an error in the plotter. 

- 10 PRINTER IS 705,80 

- 20 PRINT "IN; IP4000, 3000, 5000, 4000;5P1;5C0,1,0,1;" 30 FOR T=O TO 2#PI+PI¢20 STEP PI720 40 *=COSCT) 50 YeSIN(T) BO PRINT USING 65;"PA",%,7,"PD;" 6S IMAGE 2A,2(MD.0DDD),3A 70 NEXT T 80 PRINT "PU;SPO;" 30 END 

The Plot Relative Instruction, PR DESCRIPTION ives plot relative instruction, PR, moves the pen relative to its current location by the number of units specified by the X- and Y-increment parameters. 

| USES | The plot relative instruction can be used as PA to draw lines and move to a point. However, with PR, pen movement 1s relative to the current pen position. The instruction can be executed without parameters to establish relative plotting as opposed to absolute plotting for PU or PD commands with parameters. It is often used to draw multiple occurrences of some figure on a plot, for example, to draw several rectangles of the same size. 3-8 CONTROLLING THE PEN AND PLOTTING 
