2. have not executed an output error instruction; and
3. the error light is not on at the end of your plot.

(The fact that the error light is on does not necessarily mean out-ofrange data has been encountered; an error in any HP-GL command will turn the light on.)

The following strings of HP-GL instructions, if sent to the plotter using a suitable output statement such as PRINT or OUTPUT, will draw two triangles and then move to the point 10900, 7650with the pen up.

<!-- image -->

The next strings of HP-GL instructions scale the plotting area into user units 0 to 100in each axis and again draws two triangles. Use an out­ put statement implemented on your computer to send the strings to the plotter.

- 'IN;SP1;SCO,1U0,0,1DO;' "F'Fl2Cl, 15, F'ElV,O,1'EiV,EiCJ\_,35,20, 'l5\_,F'|\_|\_,;-'-\_'5\_,15';" 'PHPn45,15,25,35,25,15,Pu;'

<!-- image -->
