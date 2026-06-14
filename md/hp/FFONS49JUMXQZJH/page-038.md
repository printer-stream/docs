## The Output Window Instruction, OW 

DESCRIPTION Miwies output window instruction, OW, provides the means to obtain the X- and Y-coordinates of the lower-left and upperright corners of the area in which plotting can currently occur. | USES | The instruction can be used to determine the area in which any plotting will occur. When executed immediately after power on or the execution of a DF or IN command, the command can be used to determine under program control whether the paper switch is set to us or Aa. 

## SYNTAX Moh (terminator) AEE §=No parameters are used. Output is in plotter units. 

After an OW command is received, the plotter will output the coordinates of opposite corners of the plotting area in plotter units as four integers in ASCII in the following form: 

Xlower left, Ylower left, Xupper right, Yupper right [TERM] 

where [TERM] is the output terminator for your system. See Terms You Should Understand in Chapter 7. 

The range of the integers is determined by the setting of the paper switch as shown below: 

US A4 0<X< 10 300 0<X< 10 900 0< Y< 7650 0<Y< 7650 

If Xlower left is greater than Xupper right or Ylower left is greater than Yupper right, no window exists in which plotting can occur. 

2-10 ESTABLISHING BOUNDARIES AND UNITS 
