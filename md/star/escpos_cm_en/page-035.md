Rev.2.52 

## **FF** 

Name Print and recover to page mode Code ASCII FF Hex. 0C Decimal 12 Function Prints all buffered data to the print region collectively, then recovers to the standard mode. Details • All buffer data is deleted after printing. • The print area set by ESC W (Set print region in page mode) is reset to the default setting. • No paper cut is executed. • Sets the print position to the beginning of the next line after execution. • This command is enabled only in page mode. Reference ESC FF, ESC L, ESC S 

ESC/POS Command Specifications 

35 
