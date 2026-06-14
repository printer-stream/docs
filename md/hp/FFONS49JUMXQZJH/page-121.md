The program lines which plot the two lower lines and the corresponding legend lines are: 

260 PRINT "SP1;LT3,6;PA1 23FD2 25 3 18 4 22 5 23" 270 PRINT "PD6 2? 7 2? 8 25 9 24 10 28 11 27 12 Z2°?PU" 280 PRINT "PA?7.8,165 POS.3,165 PU" 290 PRINT "SP2;LT6,8;PA1,45;PD;PAZ,50,3,52,4,53,5,52" 300 PRINT "PD6,51,7,55,8,56,9,56,10,58,11,58,12,60PU" 310 PRINT "PA10.1,165 P011.6,165 Pu" 

The third line is plotted from data read by the program at execution time using a FOR...NEXT loop and a READ statement. This technique would be used to plot a graph that will be replotted often with new data. If the necessary file statements were added, the data could be on a tape or disk file instead of in a DATA statement as shown here. The line type for this line is the default solid line, reverted to by the LT command with no parameters. Since we are using variables as plot parameters, you need to be sure they are sent to the plotter with a space between numeric variables. Computers often send a leading and/or trailing blank or allow for a sign space before numeric variables. The 7470 will treat a blank, comma, or sign as a separator between numeric parameters. Know your computer before sending variables with plot commands. As with the two previously drawn lines, after the line is plotted, the corresponding line is placed in the legend. 

The loop to plot this third line and the statements to place a line in the legend are: 

320 PRINT "LT" 330 FOR X=1 TO 12 340 READ Y 350 PRINT "PA"; X39; "PD" 360 NEXT X 370 PRINT "PU6,165PD7.1,165PU" 410 DATA 55,60,63,62,59,54,50,46,47,49,53,58 

The last line is drawn using a subroutine. The subroutine is designed to read data that have been stored with a third value for pen control. This third value controls a branch to two different plot statements, one with the pen up and the other with the pen down. In this program, a zero as a pen control parameter results in a pen up move, a 1 causes plotting with the pen down, and 3 signifies the end of the data. The legend line is drawn at the end of the subroutine, completing the graph. 

PUTTINGTHE COMMANDS TO WORK 8-7 
