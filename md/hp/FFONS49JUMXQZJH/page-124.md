320 PRINT "LT" 330 FOR X=1 TO 12 340 READ Y 350 PRINT "PA"; X;¥;" PD" 360 NEXT X 370 PRINT "PUB,165P07.1, 165FU" 380 PRINT "SP1;LT4,6" 390 GOSUB 1000 400 DATA wy FY Pane yA" ache: gt ag" Rt isi » "oO" uN" ‘ wy 410 DATA 55,60,63,62,59,54,50,46,47,49,53,58 420 STOP 1000 ! PLOTTING SUBROUTINE 1010 READ *,',F 1020 IF P21 THEN PRINT "PI" 5%; 1030 IF FP=O THEN PRINT "PU" %3¥ 1040 IF P=3 THEN 1090 1050 DATA 1,98,0,2,100,1,3,102,1,4,105,1,5,107,1,6,110,1 1060 DATA 7,125,1,8,112,1,9,115,1,10,125,1,11,130, 1070 DATA 12,122,7,0,0,3 1 1080 GOTO 19010 1090 PRINT "LT4,6 PU3.2,165 PO4.7,1655P0;" 1100 RETURN 1110 END 

## Advanced Programming Tips —————————ee 

## Filling and Hatching 

Two kinds of area fill are commonly used in bar graphs and pie charts; solid fill and hatching. Solid fill totally covers the area with color, whereas hatching fills the area with evenly spaced parallel lines. If there are lines in two directions at 90 degree angles, we call the hatching crosshatching. Sometimes a graph will have both narrow and wide hatching or crosshatching, the wide hatching having more space between the lines than the narrow. 

## Filling a Bar 

The following two program segments, together with lines 10 to 100 and 400 of this chapter’s program, will each fill a bar which represents the March data for line 1, i.e., 3, 18 (see line 260, in the program). To create an aesthetically pleasing and easily comprehendible bar graph, the bar is centered over the X data point and is slightly wider than one-half the distance between data points on the X-axis. The increment variable P depends on pen width. A value of P = 20 plotter units is suitable for a wide pen and 10 for a narrow pen. 

The first program segment should be used when plotting on paper. Notice the pen does not lift; the routine is faster and prolongs pen-tip life by limiting up/down moves. The second segment should be used when plotting on transparency film to achieve uniform ink distribution. 

8-10 PUTTING THE COMMANDS TO WORK 
