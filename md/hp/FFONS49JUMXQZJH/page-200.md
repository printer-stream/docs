Page 5-6 

## DT The Define Terminator Instruction 

## DT 

      - t(;) 

   - Purpose: Defines the label terminator used in LB command. Parameter: ASCII character 1 to 127 except 5 and 27. Only an IN or DF command or use of ETX (decimal 3) as parameter restores label terminator to ETX, its default value. 

- IM The Input Mask Instruction Page 1-12 IM E-mask value (, S-mask value(, P-mask value)) (;) Purpose: Set masks to specify which errors will cause the ERROR LED to come on and bit 5 of the status byte to be set, and to specify what conditions will cause a positive response to a serial or parallel poll in an HP-GL environment. 

         - Page 1-12 

   - Parameters: integers 0 through 255. If parameters omitted, masks are set to 223 ,0,0, the default values. 

## IN’ The Initialize Instruction 

## Page 1-11 

- IN ; Purpose: Sets the plotter to default conditions plus raises the pen, sets the scaling points to Pl = 250,279 and P2 = 10 250, 7479, clears all HP-GL errors, sets bit 3 of the output status byte to true (1), and reads setting of paper switch. 

## IP The Input P1 and P2 Instruction 

   - Page 2-4 

- IP Pix, Ply (, P2x, P2y) (;) Purpose: Sets scaling points. 

- Parameters: Integers in plotter units. Omitting parameters sets P1 and P2 to default values, P1 = 250, 279, P2 = 10 250, 7479. 

## IW The Input Window Instruction 

## Page 2-9 

- IW Xower left, Ylower left, Xupper right, Yupper right (5) Purpose: Sets window inside which plotting can occur. Parameters: Specify X- and Y-coordinates of lower-left and upper-right corners of the window. 

   - Omitting parameters sets window to maximum plotting area, determined by the setting of the paper switch. 

B-4 INSTRUCTION SYNTAX 
