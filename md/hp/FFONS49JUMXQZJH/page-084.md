| 

- label can be moved slightly above or belowa line, spaces or lines can be inserted in text, or labels can be centered. SMES CP #of character-space-field widths, # of character-space field heights terminator 

- CP terminatoror 

EXPLANATION Mii forms Gamets parameters are specified, a CP command pera carriage return and line feed, moving one character-space-field height down and returning to the margin defined by the carriagereturn point. The carriage-return point is the last point moved to using either a PA, PR, PU, or PD command or front panel controls, or the pen position at the last DI or DR command. Refer to The Label Instruction in this chapter. 

When parameters are specified, the CP command moves the pen the specified number of character-space-field widths to the right (a positive value) or the left (a negative value). Note that right, left, up, and down are relative to the label direction, where a positive value means from P1 toward P2. This is shown below. 

**==> picture [290 x 57] intentionally omitted <==**

**----- Start of picture text -----**<br>
ws<br>LEFT (--—«~ LABEL, DIRECTION, ODI1, O-> RIGHT (+)<br>DOWN (-}<br>**----- End of picture text -----**<br>


mo (-) RIGHT (=O ‘I-10 ‘NOILOSYIO Wav teet 1 UP (+) 

The pen’s position (raised or lowered) does not change when a CP command is executed. The parameters must be > —128 and < +128. However, since there are approximately 90 character-space-field widths and 40 character-space-field heights on the plotting surface, assuming default sizing, the effective parameter range that will keep the labels on the medium is considerably less, depending on the pen position at the given time. 

The use of the CP command to produce lettering along a line, but not on top of it and alignment with a left-hand margin is illustrated in the following program. The CP command in the second line moves the label slightly above the line. The CP command in the third line moves the label slightly below the line and the CP command in the last line performs a carriage return, line feed to the margin established by the 5-14. LABELING 
