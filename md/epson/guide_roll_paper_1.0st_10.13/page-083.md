## **C O N F I D E N T I A L** 

## **CR** 

EXECUTING COMMAND 

[Name] Print and carriage return [Format] ASCII CR Hex 0D Decimal 13 [Range] None [Default] None 

- [Printers not featuring this command] TM-P60 

- [Description] Executes one of the following operations. 

|**Print head**|**When auto line feed is enabled**|**When auto line feed is disabled**|
|---|---|---|
|Line thermal|Executes printing and one line feed asLF|This command is ignored|
|Serial dot head|Executes printing and one line feed asLF|In standard mode, prints the data in the<br>print buffer and moves the print position<br>to the beginning of the print line.<br>In page mode, moves the print position<br>to the beginning of the print line.|



## [Notes] 

- With a serial interface, the command performs as if auto line feed is disabled. 

- Enabling or disabling the auto line feed can be selected by the DIP switch or the memory switch. Memory switch can be changed with GS ( E <Function 3>. 

- After printing, the print position moves to the beginning of the line. When a left margin is set in standard mode, the position of the left margin is the beginning of the line. 

- When this command is processed in page mode, only the print position moves, and the printer does not perform actual printing. 
