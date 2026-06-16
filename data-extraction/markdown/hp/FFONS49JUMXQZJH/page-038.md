## The Output Window Instruction, OW

DESCRIPTHJNThe output window instruction, OW, provides the means to obtain the X- and Y-coordinates of the lower-left and upper­ right corners of the area in which plotting can currently occur.

The instruction can be used to determine the area in which any plotting will occur. When executed immediately after power on or the execution of a DF or IN command, the command can be used to determine under program control whether the paper switch is set to us or A4. which

SYNTAX OW (terminator)

EXPLANA-'UNNo parameters are used. Output is in plotter units.

After an OWcommand is received, the plotter will output the coordi­ nates of opposite corners of the plotting area in plotter units as four integers in ASCII in the following form:

Xlowerleft, Ylowerleft, Xupper right, Yupperright [TERM]

where [TERM]is the output terminator for your system. See Terms You Should Understand in Chapter 7.

The range of the integers is determined by the setting of the paper switch as shown below:

US

A4

0&lt;X&lt; 10300

O&lt;X&lt;10900

O&lt;Y&lt;7650

0&lt;Y&lt;7650

If Xlowerleft is greater than Xupperright or Y1owe; left is greater than Yupperight,no window exists in which plotting can occur.
