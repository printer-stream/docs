## **C O N F I D E N T I A L** 

## **ESC @** 

EXECUTING + SETTING 

[Name] Initialize printer [Format] ASCII ESC @ Hex 1B 40 Decimal 27 64 [Range] None [Default] None 

## [Printers not featuring this command] None 

- [Description] Clears the data in the print buffer and resets the printer modes to the modes that were in effect when the power was turned on. 

   - Any macro definitions are not cleared. 

   - Offline response selection is not cleared. 

   - Contents of user NV memory are not cleared. 

   - NV graphics (NV bit image) and NV user memory are not cleared. 

   - The maintenance counter value is not affected by this command. 

   - The specifying of offline response isn’t cleared. 

## [Notes] 

- The DIP switch settings are not checked again. 

- The data in the receive buffer is not cleared. 

- When this command is processed in page mode, the printer deletes the data in the print areas, initializes all settings, and selects standard mode. 

- This command can cancel all the settings, such as print mode and line feed, at the same time. 

- The print position moves to the beginning of the line when this command is executed. When a left margin is set in standard mode, the position of the left margin is the beginning of the line or there is no data in the print buffer. 
