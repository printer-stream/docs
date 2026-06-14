The User Defined Character Instruction, UC WHat §=The user defined character instruction, UC, provides the means to draw characters of your own design. It is not included in the instruction set of the 7470 plotter with an HP-IL interface. | USES | This instruction can be used to create symbols not included in the plotter’s character sets, to draw logos, or to create your own character fonts. ; SYNTAX Mitavel (pen control,) X-increment, Y-increment,(pen control,) (X-increment, Y-increment,)...,.... terminator or UC terminator PAPEL §=6The instruction is treated as a NOP instruction on a plotter with an HP-IL interface (refer to Appendix C). 

The following paragraphs apply to plotters with either an HP-IB or RS-232-C interface. Each segment of the character is drawn on a character grid according to the three types of parameters in the command. 

A grid is established on each character-space field by dividing it into six horizontal units and 16 vertical units. The size of the characterspace field and, hence, the grid unit is set by the current size command. The size of the character-space field and thus the grid is always twice the current character height and 1% times the current character width. In order to draw a user defined character the same size as a character drawn with a label command, the user defined character must be designed in the lower-left corner of the grid with a width of four grid units and a height of eight grid units. 

The three types of parameters are described below. 

The X- and Y-increments should appear in pairs and must be greater than —99 and less than +99. They specify, in decimal format, the number of X- or Y-grid units that the pen will move horizontally or vertically from the current pen position. The parameters need not be integers; fractional portions are used. Positive X-increment parameters move the pen in the direction of labeling, i.e., to the right with default label direction, and positive Y-increment parameters move the pen up with default label direction. Negative parameters move the pen in the opposite direction. Unmatched X,Y increments are discarded, error 2 is set, and the rest of the character is drawn. 

Pen control parameters must be less than or equal to —99 or greater than or equal to +99. A positive pen control parameter lowers the pen; a 

LABELING 5-19 
