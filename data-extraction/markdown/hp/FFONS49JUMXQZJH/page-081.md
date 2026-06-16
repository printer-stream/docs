The following example labels the years 1978through 1985,in a circular pattern starting with vertical labeling. The direction in which each year is labeled is changed by 45 degrees. Then the labels in the center are drawn to illustrate the use of cosine and sine values as parameters. The label \_*\_2000 contains both a carriage return and a line feed character before the label terminator, ETX, so the pen position at the end ofthat label is one line belowthe beginning of that label. The fact that DI commands update the carriage return point can be clearly seen by observing the pen's position at the end of the program. The final character in the last label is a carriage return and the pen returns to . the carriage return point, the position of the pen at the last 'DI command.

<!-- image -->

NOTE: Check the format of the COS and SIN functions on your computer, and change these accordingly. Also, check your computer documentation to see how your computer interprets angles. If angles are interpreted as radians, you need to change to degrees before using the COS and SIN functions. On the HP Series 80 computers, execute the BASICstatement DEG. I

## The Relative Direction Instruction, DR

DESCRIPTHJNThe relative direction instruction, DR, specifies the direc­ tion in which characters are lettered.
