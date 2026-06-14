## Appendix B Instructione Syntax 

## HP-GL Syntax 

This section lists the formal syntax for each plotter instruction in alphabetical order of the instruction’s two-letter mnemonic. 

Each instruction is listed with its purpose, syntax, parameter or response type, and range. If no parameter range is given, the range is —2)5 to 215 -1. Refer to the indicated pages for details. The semicolon is included as the terminator for all instructions except the label instructions. A nonalphabetic or nonnumeric character such as # or $, or the next mnemonic can also be used as the instruction terminator. In addition, if you have an HP-IB or HP-IL plotter, the line feed character can be used as a terminator. The semicolon appears in parentheses (;) if the instruction executes without the plotter receiving the terminator. [TERM] means the terminator sent by the plotter at the end of output. It is CRLF in an HP-IB or HP-IL configuration and CR or as set by an ESC .M command in an RS-232-C configuration. 

## AA* The Are Absolute Instruction 

## Page 3-17 

- AA X-coordinate, Y-coordinate,arc angle(,chord angle); Purpose: Draws arc of specified number of degrees with specified smoothness; centered at X,Y coordinate, using current pen status (up or down). 

- Parameters: X- and Y-coordinates — integer, in plotter units unless scaling in effect; then in user units. 

   - arc angle — integer, negative value specifies clockwise arc, positive value specifies counterclockwise arc. 

chord angle — integer, defines arc smoothness in degrees. Default is 5 degrees. 

- *Available only with RS-232-C plotters that have the serial prefix number 2308A or higher. 

INSTRUCTION SYNTAX B-1 
