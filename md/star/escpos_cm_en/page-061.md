Rev.2.52 

## **ESC L** 

Select page mode 

Name Select page mode Code ASCII ESC L Hex. 1B 4C Decimal 27 76 Function Switches from standard mode to page mode. 

Function Switches from standard mode to page mode. Details • Enabled only when input with the top of line. 

- Invalid when input by page mode. 

- Returns to standard mode after the following commands are issued. 

- a.  FF (Print and recover to page mode) 

- b. ESC S (Select standard mode) 

- Character expansion position has the starting point specified by ESC T (Character print direction selection in page mode) in the printing region designated by the ESC W (Set print region in the page mode) command. 

- This command switches the settings for the following commands the values of which can be set independently in standard mode and page mode to those for page mode 

- a. Set space amount: ESC SP, FS S 

- b. Set line feed amount: ESC 2, ESC 3 

- The following commands are enabled only when in page mode. 

- a. ESC V: Specify/cancel character 90 degree clockwise rotation 

- b. ESC a: Position alignment 

- c. ESC {: Specify/cancel upside-down printing 

- d. GS L: Set left margin e. GS W: Set print region width 

- The following command is ignored in page mode. 

- a. GS (A: Test print 

- The following commands are invalid in page mode. 

- a. FS p: Print NV bit image 

- b. FS q: Define NV bit image 

- c. FS g1: Write data to user NV memory 

- d. GS v0: Print raster bit images 

- e. GS ( L m fn (fn = 69): Print NV graphics f. GS ( 8 m fn (fn = 69): Print NV graphics 

• Recover to standard mode using ESC@ (initialize printer). 

Reference 

FF, CAN, ESC FF, ESC S, ESC T, ESC W, GS $, GS \ See section 2. Explanations of the Page Mode for details. 

ESC/POS Command Specifications 

61 
