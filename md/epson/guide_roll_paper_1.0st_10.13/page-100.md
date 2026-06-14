## **C O N F I D E N T I A L** 

## **ESC 3** 

SETTING COMMAND 

[Name] Set line spacing [Format] ASCII ESC 3 n Hex 1B 33 n Decimal 27 51 n [Range] 0 ≤ n ≤ 255 

[Default] TM-P60: n = 30 

- Printers other than the above: Amount of line spacing which corresponds to “default line spacing.” (See ESC 2 for the default line spacing.) 

## [Printers not featuring this command] None 

- [Description] Sets the line spacing to n × (vertical or horizontal motion unit). 

- [Notes] ■ The maximum line spacing is 1016 mm {40 inches}. If the specified amount exceeds 1016 mm {40 inches}, the line spacing is automatically set to 1016 mm {40 inches}. 

   - When standard mode is selected, the vertical motion unit is used. 

   - When page mode is selected, the vertical or horizontal motion unit is used for the print direction set by ESC T. 

      - When the starting position is set to the upper left or lower right of the print area using ESC T, the vertical motion unit is used. 

      - When the starting position is set to the upper right or lower left of the print area using ESC T, the horizontal motion unit is used. 

   - The line spacing can be set independently in standard mode and in page mode. 

      - In standard mode this command sets the line spacing of standard mode. 

      - In page mode this command sets the line spacing of page mode. 

   - When the motion unit is changed after the line spacing is set, the line spacing setting does not change. 

   - Selected line spacing is effective until ESC 2 is executed, ESC @ is executed, the printer is reset, or the power is turned off. 
