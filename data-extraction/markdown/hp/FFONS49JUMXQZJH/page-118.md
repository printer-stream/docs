The loop to draw the axis and the statements to set character and tick length and to label and title the X-axis are:

```
50 PRINT'SI.2,.3;TL1.5,0' 80 FOR X=1 TD 12 70 PRINT "PH';X,',O; XT;' 80 REHD H3 90 PRINT'CP-.33,-1;LB';P$;'E' 100 NEXT X 110 PRINT 'PHB.5,0;CP-?,-2.5; LBCHLENDHR MUNTHE' IIJIIJIIFII'|IMII'I|H||,||[».-1||V'|l'J|I'|lJI|:IlHIIISIISII'||Ul|,||t.\ll|-.l|DlI 400 5;
```

The Y-axis is created in a similar manner, except the lo0p's index is used for the label value and two different CP commands are used for labels of three digits and labels of less than three digits. The Y-axis title is centered above the axis.

Following the axis routine is the command which labels the regions for the legend. It is drawn now while the label size is small and the narrow pen is installed. Note that the label statements contain the spaces nec­ essary to space the legend across the top of the graph. These lines were inserted near the end of the creation process and involved trial and error to achieve satisfactory results. The lines for the legend will be drawn later as each line of data is plotted.

The lines which draw the Y-axis, label it, and draw the legend labels follow:

```
120 FOR Y=O T0 150 STEP 25 130 PRINT 'PH 1,',Y,'YT;' 140 IF Y<1OOTHENPRINT 'CP-3,-.25;LE';Y;"E" 150 IF Y>S9 THENPRINT 'CP-4,-.35; LB';Y;'§' 180 NEXT Y 170 PRINT 'PH1,15O CP-3.5,2 LBSHLES$§CP-S,-1' 180 PRINT "LBiTHDUSHNUS) UNITED STHTES E' 190 PRINT 'LBEURDPE JHPHN SOUTH HMERICHE'
```
