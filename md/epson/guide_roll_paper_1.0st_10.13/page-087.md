## **C O N F I D E N T I A L** 

## **ESC J** 

EXECUTING COMMAND 

[Name] Print and feed paper [Format] ASCII ESC J n Hex 1B 4A n Decimal 27 74 n [Range] 0 ≤ n ≤ 255 [Default] None 

## [Printers not featuring this command] None 

- [Description] Prints the data in the print buffer and feeds the paper n × (vertical or horizontal motion unit). 

- [Notes] 

- The maximum paper feed amount is 1016 mm {40 inches}. If the specified amount exceeds 1016 mm {40 inches}, the paper feed amount is automatically set to 1016 mm {40 inches}. 

- When standard mode is selected, the vertical motion unit is used. 

- When page mode is selected, the vertical or horizontal motion unit is used for the print direction set by ESC T. 

   - When the starting position is set to the upper left or lower right of the print area using ESC T, the vertical motion unit is used. 

   - When the starting position is set to the upper right or lower left of the print area using ESC T, the horizontal motion unit is used. 

- After printing, the print position moves to the beginning of the line. When a left margin is set in standard mode, the position of the left margin is the beginning of the line. 

- When this command is processed in page mode, only the print position moves; the printer does not perform actual printing. 

- This command is used to temporarily feed a specific length without changing the line spacing set by other commands. 
