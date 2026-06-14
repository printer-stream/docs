## **C O N F I D E N T I A L** 

## [Notes] 

- This command is ignored if a downloaded bit image has not been defined. 

- When standard mode is selected, this command is enabled only when there is no data in the print buffer and the printer is in the beginning of the line. If data exists in the print buffer, the printer processes m as normal data. 

- When page mode is selected, this command develops the downloaded bit image data in the print buffer but the printer does not print the downloaded bit image data. 

- If a downloaded bit image exceeds one line, the excess data is not printed. 

- The scales for width and height of downloaded bit images are specified by m. Therefore, in page mode with 90 ° or 270 ° clockwise rotated bit image, the printer applies print area and dot density from [width: direction of paper feed, height: perpendicular to direction of paper feed]. 

- The scales for width and height of downloaded bit images are specified by m. Therefore, in page mode with 90 ° or 270 ° clockwise-rotated bit image, the printer applies print area and dot density from [width: direction of paper feed, height: perpendicular to direction of paper feed]. 

- This command feeds as much paper as is required to print the downloaded bit image, regardless of the line spacing specified by ESC 2 or ESC 3. 

- The downloaded bit image is not affected by print mode (emphasized, double-strike, underline, character size, white/black reverse printing, or 90° clockwise-rotated), except for upside-down print mode. 

- When printing a downloaded bit image, selecting unidirectional print mode with ESC U enables printing patterns in which the top and bottom parts are aligned vertically. 

- The downloaded bit image is defined by GS ✻. 

- Downloaded bit image is printed in the default dot density (dot density of vertical and horizontal direction in normal mode) defined by GS L <Function 49>. 

- After printing the downloaded bit image, the print position is set to the left of the print area. The printer is in the beginning of a line and data is not in the print buffer. 

[Model-dependent variations] TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90 
