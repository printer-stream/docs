Rev.2.52 

## **FF** 

Name Print and recover to page mode Code ASCII FF Hex. 0C Decimal 12 Function • When in page mode, this prints all buffered data to the print region collectively, then recovers to the standard mode. • In standard mode, this prints the data in the print buffer and feeds paper to the TOF position (the black mark). Details • In page mode, all buffer data is deleted after printing. • In page mode, the print area set by ESCW (Set print region in page mode) is reset to the default setting. • In page mode, no paper cut is executed. • In page mode, this sets the print position to the beginning of the next line after execution. STAR • The TOF position (black mark) varies according to the paper used and to customer specifications. Reference ESC FF, ESC L, ESC S 

ESC/POS Command Specifications 

172 
