The loop to draw the axis and the statements to set character and tick length and to label and title the X-axis are: 

50 PRINT "SI.2,.3;7TL1.5,0" 60 FOR X=1 TO 12 70 PRINT "PA" ;X,",0; X73" 80 READ R$ 390 PRINT "CP-.33,-1;LB"j;A%;"5" 100 NEXT X 110 PRINT "PA6.5,0;CP-7,-2.5; LECALENDAR MONTH&" 400 DATA "J" ; wpa ; pq , ue , Wopyt : wou ; wpe : noe : wou , wou : i : wpe 

The Y-axis is created in a similar manner, except the loop’s index is used for the label value and two different CP commands are used for labels of three digits and labels of less than three digits. The Y-axis title is centered above the axis. 

Following the axis routine is the command which labels the regions for the legend. It is drawn now while the label size is small and the narrow pen is installed. Note that the label statements contain the spaces necessary to space the legend across the top of the graph. These lines were inserted near the end of the creation process and involved trial and error to achieve satisfactory results. The lines for the legend will be drawn later as each line of data is plotted. The lines which draw the Y-axis, label it, and draw the legend labels follow: 

120 FOR Y=0 TO 150 STEF 25 130 PRINT "PA 1,",7,"7T;3" 140 IF Y<100 THEN PRINT "CF-3,-.25;LB"575" 5" 150 IF Y>99 THEN PRINT "CF-4,-.25; LE" 3 V5" &" 160 NEXT ¥ 170 PRINT "PA1,150 CP-3.5,¢ LBSALES $&CP-9,-1" 190 PRINT "LB( THOUSANDS} UNITED STATES 5" 190 PRINT "LBEUROPE JAPAN SOUTH AMERICAS" 

8-4. PUTTING THE COMMANDSTO WORK 
