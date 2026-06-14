will set an error condition but all X,Y pairs which precede the unmatched parameter will be plotted. 

The X-coordinate specifies, in either plotter units or user units, the absolute X-location to which the pen will move. The Y-coordinate specifies, in either plotter units or user units, the absolute Y-location to which the pen will move. If scaling is on, coordinates are in user units. If scaling is off, coordinates are in plotter units. 

The mnemonics PU and PD can be included ahead of, between, or after XY coordinate pairs. PU lifts the pen; PD lowers the pen. ; 

Any number of coordinate pairs, as well as PU or PD mnemonics, can be listed after a PA instruction. (This is limited only by the ability of the controller to output without a line feed character which is an instruction terminator.) The pen will move to each point in the order given. Commas, spaces, or a sign are required between numeric parameters and are optional after two-letter mnemonics. The last entry is followed by the terminator. In the following examples, commas are used to show optional and required separators. Optional commas or spaces which can be used between each letter of the mnemonics are not shown. The semicolon is used to indicate the terminator. 

**==> picture [221 x 127] intentionally omitted <==**

If no pen control parameter is given, the pen will assume the pen state (up or down) of the previous statement. The PU or PD mnemonics can also be substituted for the PA (or PR) mnemonic. This is equivalent to having PU; or PD; preceding the PA or PR instruction. Therefore, PU and PD with parameters are interpreted to be in place of PA or PR, depending upon which mnemonic, PA or PR, was last specified. PA is specified by any of the following: 

## © power-up, 

e execution of an IN command, 

CONTROLLING THE PEN AND PLOTTING 3-5 
