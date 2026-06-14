Rev.2.52 

## **FS p n m** 

Name Print NV bit image Code ASCII FS p n m Hex. 1C 70 n m Decimal 28 112 n m 1 ≤ n ≤ 255 Defined Region 0 ≤ m ≤ 3, 48 ≤ m ≤ 51 

Function Prints NV bit image n using mode m. 

|m|Mode|Densityof Vertical Direction Dots|Densityof Horizontal Direction Dots|
|---|---|---|---|
|0,48|Normal Mode|180 DPI|180 DPI|
|1,49|Double-wide Mode|180 DPI|90 DPI|
|2,50|Double-tall Mode|90 DPI|180 DPI|
|3,51|Quadruple Mode|90 DPI|90 DPI|



   - n specifies the NV bit image number. 

   - m specifies the bit-image mode. 

- Details • NV bit image is a bit image defined in non-volatile memory by FS q and printed by this command. 

   - This command is ignored when the specified NV bit image n is undefined. 

   - This command is effective only when no data exists in the print buffer in standard mode. 

If data exists, 2 bytes are ignored. 

- When in page mode, this command is disabled. 

- Excluding upside-down printing, print modes (emphasized printing, double printing, underlines, character sizes, black/white inverted printing and 90 degree clockwise rotation) are unaffected. 

- If bit image specification is of a size that exceeds the print region, the data in the print region is targeted for printing, but the excessive data is not printed. 

- This command feeds dots (for the height _n_ of the NV bit image) in normal and double-width modes, and (for the height of the NV bit image n x 2) in double-height and quadruple modes, regardless of the line spacing specified by ESC 2 (Set default line spacing) or ESC 3 (Set line feed amount). 

- After printing the bit image, this command sets the print position to the top of the line and processes the subsequent data as normal data. 

## STAR 

- Dot density (when the STAR printer head = 203 DPI) on STAR printers. 

|m|Mode|Densityof Vertical Direction Dots|Densityof Horizontal Direction Dots|
|---|---|---|---|
|0,48|Normal Mode|203 DPI|203 DPI|
|1,49|Double-wide Mode|203 DPI|101 DPI|
|2,50|Double-tall Mode|101 DPI|203 DPI|
|3,51|Quadruple Mode|101 DPI|101 DPI|



- The NV bit image data defined by “GS ( L <fn=67>, GS ( 8 <fn=67>” is printable by this command. 

• See Appendix-11 for setting details. 

Related Commands ESC *, FS q, GS \, GS v 0 Reference Appendix -11 

ESC/POS Command Specifications 

82 
