```
320 PRINT 'LT' 330 F0R x=1 T0 12 340 REHD Y 350 PRINT 'PH';X;Y;'PU' 350 NEXT x 3?0 PRINT 'PU5,1S5PD?.1,1ESPU' 380 PRINT 'SP1;LT4,B' 390 @0503 1000 _ IIJH'||Fl|'||M||,l|H||',l|r.1|l-!|l_JlI'!||J||'|lF1||'llS||,I|Ul|'||t\lI|JHDII 410 DRTH 55,s0,s3,s2,5s,54.50,45,4?,49,53,se 420 STOP 1000 1 PLUTTING SUBRUUTIHE 1010 REHDX,Y,P 1020 IF P=1 THEN PRINT 'PU';H;Y 1030 IF P=0 THENPRINT "Pu';H;Y 1040 IF P=3 THEN 1090 1050DRTH 1,as,0,2,100,1,3,102,1,4,105,1,s,10?,1,e,110,1 1060 DHTH ?,125,1,e,112,1,9,115,1,10,125,1,11,130,1 1070 DHTH 12,122,1,0,0,3 1080 GDTU 1010 1080 PRINT "LT4,B PU3.2,1Ei5 PB-4.?,'1Ei5EiF'0;" 1100 RETURN 1110 END %3¥ ,3
```

## Advanced Programming Tips

## Filling and Hatching

Twokinds of area fill are commonly used in bar graphs and pie charts; solid fill and hatching. Solid fill totally covers the area with color, whereas hatching fills the area with evenly spaced parallel lines. If there are lines in two directions at 90 degree angles, we call the hatching crosshatching. Sometimes a graph will have both narrow and wide hatching or crosshatching, the wide hatching having more space between the lines than the narrow.

## Filling a Bar

The following two program segments, together with lines 10 to 100and 400 of this chapter's program, will each fill a bar which represents the March data for line 1, i.e., 3, 18 (see line 260, in the program). To create an aesthetically pleasing and easily comprehendible bar graph, the bar is centered over the X data point and is slightly wider than one-half the distance between data points on the X-axis. The increment variable P depends on pen width. A Value of P = 20 plotter units is suitable for a wide pen and 10for a narrow pen.

The first program segment should be used when plotting on paper. Notice the pen does not lift; the routine is faster and prolongs pen-tip life by limiting up/down moves. The second segment should be used when plotting on transparency film to achieve uniform ink distribution.

## 8-10 PUTTING THE COMMANDS TO WORK
