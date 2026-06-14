## **C O N F I D E N T I A L** 

- If [horizontal logical origin + print area width] exceeds the printable area, the print area width is automatically set to [horizontal printable area – horizontal logical origin]. 

- If [vertical logical origin + print area height] exceeds the printable area, the print area height is automatically set to [vertical printable area – vertical logical origin]. 

- Keep the following conditions in mind for printers that support <Function 48> of GS ( P. 

   - The maximum area that can be specified by this command is the same as the printable area specified by <Function 48> of GS ( P. 

   - The origin of this command is the same as the upper left point of the printable area specified by <Function 48> of GS ( P. 

   - When adjusting the printable area of the page mode with <Function 48> of GS ( P, specify the printable area to be the same as the setting of the printable area by this command after executing ESC L. 

- The print area and the logical origin set by this command are effective only in page mode. 

- This command setting has no effect in standard mode. If this command is processed in standard mode, the logical origin and the print area are set, and they are enabled when the printer selects page mode. 

- Even if the horizontal or vertical motion unit is changed after changing the printable area, the setting of the printable area will not be changed. 

- The settings of this command are effective until FF is executed, ESC @ is executed, the printer is reset, or the power is turned off. 
