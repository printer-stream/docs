label can be moved slightly above or below a line, spaces or lines can be inserted in text, or labels can be centered.

CP

- # of character-space-fieldwidths, # of character-space field heights terminator or
- CP terminator

EXPI-ANA-'UNIf no parameters are specified, a CP command per­ forms a carriage return and line feed, moving one character-space-field height down and returning to the margin defined by the carriage­ return point. The carriage-return point is the last point moved to using either a PA, PR, PU, or PD command or front panel controls, or the pen position at the last D1or DR command. Refer to The Label Instruction in this chapter.

When parameters are specified, the CP command moves the pen the specified number of character-space-field widths to the right (a positive value) or the left (a negative value). Note that right, left, up, and down are relative to the label direction, where a positive value means from P1 toward P2. This is shown below.

<!-- image -->

<!-- image -->

The pen's position (raised or lowered) does not change when a CP com­ mand is executed. The parameters must be 2 -128 and &lt; +128. However,since there are approximately 90 character-space-field widths and 40 character-space-field heights on the plotting surface, assuming default sizing, the effectiveparameter range that will keep the labels on the medium is considerably less, depending on the pen position at the given time.

The use of the CP command to produce lettering along a line, but not on top of it and alignment with a left-hand margin is illustrated in the following program. The CP command in the second line moves the label slightly above the line. The CP command in the third line moves the label slightly below the line and the CP command in the last line performs a carriage return, line feed to the margin established by the
