Advanced Programming Tips ———— cranes 

Many software packages read P1 and P2 and use these points to define the maximum plotting area. You may want to obtain the largest plot possible on the 7470. This is the area of the default window, as determined by the setting of the paper switch, not the area established by the default settings of P1 and P2. The first three lines of the following listing will read the window size and set P1 and P2 to these points, so that the largest area possible is used for plotting. In order to change the plotting area, this HP-GL routine should precede the PLOTTER IS statement when programming on HP desktop computers in AGL. 

Sometimes you want more than one plot on a page. The rest of the instructions set the window to, and outline four separate areas. A small space has been left between each area by adding or subtracting a constant value from X- and Y-coordinates in the center of the total area. This program could be modified to divide the plotting area into thirds or into areas of any other size. Another application of windowing is shading rectangular areas for bar graphs. See Advanced Programming Tips, Chapter 8. 

"IN; OW" fINSERT LINE TO READ COORDINATES INTO A,B,C,0 "IP" 3A,B,C,D "IW" 3A, B3C/72-100;D/2-100;"SF1;PR";A;B "IW""PD" 5 C/2-100; Bj;C/2-100;D/2-100;A;D“2-100;A;By" PU" "PD" 5 C/2+100; B;C;0/“2-100;"SP2;PU";3C/24+100;B 5C;B;C,0/2-100;C/2+100; "IW" 02-100; C/2+100; Bs "PUM "PD" 5 C/2+100;D/Z+100;C;D;"SP13PA" ;C/2+100;D/2+100 "IW" 5C;D/2+100;C;Dj;C/2+100;D; C“2+100;D/24+100;"PU;" 3A; D/24+100;C/“Z-100;D3"PU; "PD" SP2; PA" 5A; 02+100 3C/2-100;0/2+100;C“2-100;D;A;D3A;D/2+100;"SPO" 

aoe Reduced Plot 

ESTABLISHING BOUNDARIES AND UNITS 2-11 
