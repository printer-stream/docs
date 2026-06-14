2. have not executed an output error instruction; and 

3. the error light is not on at the end of your plot. 

(The fact that the error light is on does not necessarily mean out-ofrange data has been encountered; an error in any HP-GL command will turn the light on.) 

The following strings of HP-GL instructions, if sent to the plotter using a suitable output statement such as PRINT or OUTPUT. will draw two triangles and then move to the point 10 900, 7650 with the pen up. 

"IN; SP1 3" "PAZOOO, 1500, PB,0,1500, 2000, 3500, 2000, 1500, PL, 2500, 1500;" "PRAPD4500, 1500, 2500, 3500, 2500, 1500,FU, 19900, 7650;" 2000 , 3500 2500,, 3500 ZL NN > 1500 2000 T6500 2500 , 1500 4500 %600 

The next strings of HP-GL instructions scale the plotting area into user units 0 to 100 in each axis and again draws two triangles. Use an output statement implemented on your computer to send the strings to the plotter. 

"IN; SP1;SC0,100,0,100;" "PAZO,15,PD,0,15,20,35,20,15,PU,25,15;" "PAPD45,15,25,35,25,15,PU;" 

CONTROLLING THE PEN AND PLOTTING 3-7 
