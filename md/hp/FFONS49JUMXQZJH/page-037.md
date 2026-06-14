## The Input Window Instruction, IW 

The input window instruction, IW, provides the means to restrict programmed pen motion to a rectangular area of the plotting surface. This area is called the “window.” | USES | The instruction can be used to establish a hard clip area, i.e., restrict plotting to a certain area of the paper. The instruction is especially useful when your data should fall in a certain range but your scaling is larger (perhaps you have left room for labels) and you don’t want lines outside the normal data area. It is also useful when hatching (shading) rectangular areas. 

- IW Xlower left, Yiower left, Xupper right, Yupper right (terminator) or 

- IW (terminator) 

Parameters are always interpreted as plotter units. When four parameters are included, the hard clip limits are set according to the parameters. If no parameters are included, the hard clip limits are set to the maximum plotting area. That area was determined by the setting of the rear-panel paper switch as read when the plotter was last initialized by either power up, front-panel reset, or execution of an IN command. 

The four parameters specify, in absolute plotter units, the X- and Y-coordinates of the lower-left and upper-right corners of the window area. The parameters should be positive and less than or equal to 10 900 or 10 300 for X (depending on the setting of the paper switch) and less than 7650 for Y. Parameters between —32 768 and 0 are set to 0, and parameters larger than the limits of the absolute plotting area but less than 32 767 are set to 10 300 or 10 900 for X and 7650 for Y. If Xlower left is greater than Xupper right Or Yiower left is greater than Yupper right, no error is set but no plotting can occur. 

At power on, or when an IN or DF command is executed, the window is automatically set to the current mechanical limits i.e., maximum plotting area. The window set by DF may not correspond with the current setting of the paper switch if the setting has been changed since power on, a front-panel reset, or the last IN command was executed. 

ESTABLISHING BOUNDARIES AND UNITS 2-9 
