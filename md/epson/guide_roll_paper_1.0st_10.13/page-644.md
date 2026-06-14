## **C O N F I D E N T I A L GS ( k** <Function 381> 

- [Name] 2-dimensional GS1 DataBar: Print the symbol data in the symbol storage area 

- [Format] ASCII GS ( k pL pH cn fn m Hex 1D 28 6B 03 00 33 51 30 Decimal 29 40 107 3 0 51 81 48 

- [Range] (pL + pH × 256) = 3 (pL = 3, pH = 0 ) cn = 51 fn = 81 

   - m = 48 

- [Description] Encodes and prints the GS1 DataBar symbol data in the symbol storage area using the process of <Function 380>. 

- [Notes] ■ In standard mode, use this function when printer is “at the beginning of a line,” or “there is no data in the print buffer.” 

   - The symbol size that exceeds the print area cannot be printed. 

   - If there is any error described below in the data of the symbol storage area, it cannot be printed. 

      - There is no data (Function 380 is not processed). 

      - When there is a problem with the amount of data saved in the symbol storage area. 

      - When the data saved in the symbol storage area includes data outside the domain. 

   - Printing of symbol is not affected by print mode (emphasized, double-strike, underline, white/ black reverse printing, or 90° clockwise-rotated), except for character size and upside-down print mode. 

   - In standard mode, this command executes paper feeding for the amount needed for printing the symbol, regardless of the paper feed amount set by the paper feed setting command. The print position returns to the left side of the printable area after printing the symbol, and printer is in the status “beginning of the line,” or “there is no data in the print buffer.” 

   - In page mode, the printer stores the symbol data in the print buffer without executing actual printing. The printer moves print position to the next dot of the last data of the symbol. 
