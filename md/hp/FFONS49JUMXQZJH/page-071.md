## Chapter 5 Labelinge 

## What You’ll Learn in This Chapter 

In this chapter you will learn about character sets and labels used to create effective annotated graphics. You will learn how to designate and select character sets, how to use the label instruction with both constant and variable parameters, and how to set the size, slant, and direction of labels. Character spacing, moving the pen any number of character widths and/or lines, and designing your own characters will also be discussed. 

## HP-GL Instructions Covered 

- CS The Designate Standard Character Set Instruction CA The Designate Alternate Character Set Instruction SS. The Select Standard Character Set Instruction SA The Select Alternate Character Set Instruction DT The Define Terminator Instruction LB The Label Instruction DI The Absolute Direction Instruction DR The Relative Direction Instruction CP The Character Plot Instruction SI The Absolute Character Size Instruction SR The Relative Character Size Instruction SL The Character Slant Instruction 

- *UC The User Defined Character Instruction 

## Terms You Should Understand 

Label Terminator — the final character in every label string; it takes the plotter out of label mode so that characters are no longer drawn but are again interpreted as HP-GL instructions and parameters. Its default value is the ASCII character ETX (decimal equivalent 3), but it may be redefined using the DT instruction. 

Character Space Field — the space occupied by a single character, together with the space between it and the next character and the space above the character which separates it from the previous text line. 

*Not available with Option 003. 

LABELING 5-1 
