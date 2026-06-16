plotting without a pen until it encounters an SP command. You can lessen the manual intervention by storing the pen using SPOas the last HP-GL instruction before any pause, and by issuing a pen select command as the first HP-GL instruction after the pause.

Program lines to pause, change pens, and title the graph using a wide pen follow. Remember when you run the complete program to remove the old pens and load wide pens directly into the left and right stalls when the message appears. The SP1 command here, the first command after the program pause, assures that the pen holder is loaded so all subsequent lines will be drawn.

```
200 PRINT 'SPO;' 210 UISP 'CHHNGE TU NIUE FEMS' 220 PHUSE 230 DISP " ' 240 PRINT"SP1 PH6,15O SI.4,.B CF-S.S,2.0' 250 PRINT 'LB1S81 SHLES BY REGIUNE'
```

## Plotting YourData

We are now ready to draw lines. Each of the four data lines on this graph is drawn using a different technique. The first two lines are drawn by plot commands with parameters included when the program was written. Hence, if the data changes, it will be necessary to change the plot commands in the program.

The first line (the bottom-most line on the graph) is drawn with pen 1 using a dashed line type. The program takes full advantage of the plotter's relatively free syntax and uses spaces to delineate parameters. Send the character strings to the plotter exactly as shown. Be sure to enter those spaces; if the spaces are removed, the plotter will try to plot one very large number and you won't plot the line.

After drawing the line, the pen moves to the legend area below the graph title and draws a short line. The PU command causes the line type pattern to begin again at the beginning of this line.

The second line is also plotted using plot commands with fixed parame­ ters. These plot commands use the stricter syntax of the 9872 or 7225 plotters and would be accepted by any HP plotter programmed in HP-GL. The line type used consists of long and short dashes; the line is drawn with pen 2. After the data are plotted, the corresponding line is drawn in the legend.
