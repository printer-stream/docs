## C O N F I D E N T I A L

[Notes]

- ■ This command is not effective when the NV bit image specified by n has not been defined.
- ■ In standard mode, this command is effective only when there is no data in the print buffer and the printer is at the beginning of the line.
- ■ In page mode, the NV bit image is only stored in the print buffer and is not printed.
- ■ If the NV bit image exceeds one line of print area, the printer does not print it.
- ■ The scales for width and height of NV bit images are specified by m . Therefore, in page mode with 90 ° or 270 ° clockwise-rotated NV bit image, the printer applies print area and dot density from [width: direction of paper feed, height: perpendicular to direction of paper feed].
- ■ This command is not affected by print modes (such as emphasized, underline, character size, or 90 ° rotated characters), except upside-down print mode.
- ■ This command executes paper feed for amount needed for printing the NV bit image regardless of paper feed amount set by a paper feed setting command.
- ■ After printing the bit image, this command sets the print position to the beginning of the line.
- ■ When printing the NV bit image, selecting unidirectional print mode with ESC U enables printing patterns in which the top and bottom parts are aligned vertically.
- ■ The NV bit image is defined by FS q .
- ■ NV bit image is printed in the default dot density (dot density of vertical and horizontal direction in normal mode) defined by GS L &lt;Function 49&gt;.

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-U220
