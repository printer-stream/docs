The Pen Instructions, PU and PD DESCRIPTION Miawers pen up instruction, PU, and the pen down instruction, PD, raise and lower the pen. 

- | USES | The instructions are used to raise and lower the pen during plotting. They may be used with parameters to plot or move to the points specified by the parameters. SAIEYS PU (terminator) or 

- PD (terminator) and 

PU X....)\(terminator) or PD XNv....)\(terminator) EEE )=When no parameters are included, the pen up instruction, PU, raises the pen without moving it to a new location. The pen down instruction, PD, lowers the pen without moving it to a new location, if the pen is within the window. If parameters are included, the pen will move, in order, to the X,Y coordinates specified. The coordinates are interpreted as plotter units if scaling is off and user units if scaling is on. Moves are either relative or absolute, depending on whether a PA or PR was the last plot command executed. 

If parameters are included, both coordinates of an XY coordinate pair must be given. An odd number of parameters will set an error condition, but all X,Y pairs which precede the unmatched parameter will be plotted. For a description of the PU and PD commands with parameters, refer to The Plot Absolute Instruction, PA, and The Plot Relative Instruction, PR, which follow. 

NOTE: The plotter has an automatic pen lift feature which will lift the pen after it has been in the pen-down state for 55 seconds and no pendown plot commands or label commands have been sent to the plotter or no front-panel pen-down moves have been made for 55 seconds. @ The Select Pen Instruction, SP SHULMAN =The select pen instruction, SP, selects and/or stores one of the two pens. | USES | The instruction is used to load a pen into the pen holder so that drawing will occur. It can be used to select a pen of a different color or width, during the plotting program. It can be used with a zero parameter or no parameter to store the pen currently in the pen holder into its stall at the end of a program. 3-2. CONTROLLING THE PEN AND PLOTTING 
