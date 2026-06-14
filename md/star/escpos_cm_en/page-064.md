Rev.2.52 

## **ESC S** 

Select standard mode 

Name Select standard mode Code ASCII ESC S Hex. 1B 53 Decimal 27 83 Function Switches from page mode to standard mode. Details • Valid only when input by page mode. 

- All buffer data in page mode is deleted. 

- Sets the print position to the beginning of the next line after execution. 

- The print area set by ESCW (Set print region in page mode) is reset to the default setting. 

- This command switches the settings for the following commands the values of which can be set independently in standard mode and page mode to those for standard mode 

- a. ESC SP: Set character right space amount 

- b. FS S: Set Chinese character space amount 

- c. ESC 2: Set default line spacing 

- d. ESC 3: Set line feed amount 

- The following commands are effective only when in standard mode. 

- a. ESC W :Set print region in page mode 

- b. ESC T: Select character print direction in page mode 

- The following commands are ignored in standard mode. 

- a. GS S: Specify absolute position for character vertical direction in page mode 

- b. GS \: Specify relative position for character vertical direction in page mode 

- Standard mode is selected when the power is turned on, the printer is reset or initialized (ESC @). 

Reference 

FF, ESC FF, ESC L 

ESC/POS Command Specifications 

64 
