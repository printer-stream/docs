## **C O N F I D E N T I A L** 

## **HT** 

EXECUTING COMMAND 

[Name] Horizontal tab [Format] ASCII HT Hex 09 Decimal 9 [Range] None [Default] None 

- [Printers not featuring this command] None 

- [Description] Moves the print position to the next horizontal tab position. 

- [Notes] 

- This command is ignored unless the next horizontal tab position has been set. 

- Horizontal tab positions are set by ESC D. 

- If the next horizontal tab position exceeds the print area, the printer sets the print position to [Print area width + 1]. 

- If this command is processed when the print position is at [Print area width + 1], the printer executes print buffer-full printing of the current line and horizontal tab processing from the beginning of the next line. In this case, in page mode, the printer does not execute printing, but the print position is moved. 

- When underline mode is turned on, the underline will not be printed under the tab space skipped by this command. 

[Model-dependent variations] None 

**See program example and print sample for HT and ESC D** . 
