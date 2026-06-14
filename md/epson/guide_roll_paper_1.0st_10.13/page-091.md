## **C O N F I D E N T I A L** 

## **ESC K** 

EXECUTING COMMAND 

[Name] Print and reverse feed [Format] ASCII ESC K n Hex 1B 4B n Decimal 27 75 n [Range] TM-U230, TM-U220 **: 0** ≤ n ≤ **48** [Default] None 

## [Printers not featuring this command] TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV ,TM-T88V, TM-T70, TM-L90, TM-P60 

- [Description] Prints the data in the print buffer and feeds the paper n × (vertical motion unit) in the reverse direction. 

- [Notes] 

- The maximum paper feed amount depends on the printer model. 

- After printing, the print position moves to the beginning of the line.  When a left margin is set, the position of the left margin is the beginning of the line. 

- When standard mode is selected, the vertical motion unit is used. 

- When page mode is selected, the vertical or horizontal motion unit is used for the print direction set by ESC T. 

   - When the starting position is set to the upper left or lower right of the print area using ESC T, the vertical motion unit is used. 

   - When the starting position is set to the upper right or lower left of the print area using ESC T, the horizontal motion unit is used. 

- When this command is processed in page mode, only the print position moves; the printer does not perform actual printing. 

- This command is used to temporarily feed a specific length without changing the line spacing set by other commands. 
