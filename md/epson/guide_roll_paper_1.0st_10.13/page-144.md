## **C O N F I D E N T I A L** 

## **ESC {** 

SETTING COMMAND 

[Name] Turn upside-down print mode on/off 

[Format] ASCII ESC { n Hex 1B 7B n Decimal 27 123 n [Range] 0 ≤ n ≤ 255 

[Default] n = 0 

- [Printers not featuring this command] None 

- [Description] In standard mode, turns upside-down print mode on or off. 

      - When the LSB of n is 0, upside-down print mode is turned off. 

      - When the LSB of n is 1, upside-down print mode is turned on. 

- [Notes] ■ When standard mode is selected, this command is enabled only when processed at the beginning of the line. 

   - The upside-down print mode is effective for all data in standard mode except the following: 

      - The graphics from GS ( L of <Function 112>. 

      - Raster bit image from GS v 0. 

      - Variable vertical size bit image from GS Q 0. 

   - The upside-down print mode has no effect in page mode. If this command is processed in page mode, an internal flag is activated, and this flag is enabled when the printer returns to standard mode. 

   - The settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off. 

   - When upside-down print mode is turned on, the printer prints 180°-rotated characters from right to left. The line printing order is not reversed; therefore, be careful of the order of the data transmitted. 
