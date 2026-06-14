## **C O N F I D E N T I A L** 

## ■ The data area includes the following codeword. 

   - Data specified by Function 080. 

   - The descriptor of symbol length (the first codeword in the data area). 

   - The error correction codeword calculated by modulus 929. 

   - Pad codeword 

- When auto processing (Function 065) is specified, the number of columns is calculated by the current print area, module width (Function 067), option setting (Function 070), and the codeword in the data area. Maximum number of the columns is 30. 

- When auto processing (Function 066) is specified in page mode, the number of rows is calculated by the current print area, module height (Function 068), and the codeword in the data area. The maximum number of rows is 90. 

- Printing of symbol is not affected by print mode (emphasized, double-strike, underline, white/ black reverse printing, or 90° clockwise-rotated), except for character size and upside-down print mode. 

- In standard mode, this command executes paper feeding for the amount needed for printing the symbol, regardless of the paper feed amount set by the paper feed setting command. The print position returns to the left side of the printable area after printing the symbol, and printer is in the status “beginning of the line,” or “there is no data in the print buffer.” 

- In page mode, the printer stores the symbol data in the print buffer without executing actual printing. The printer moves print position to the next dot of the last data of the symbol. 

- The quiet zone is not included in the printing data. Be sure to include the quiet zone when using this function. 

[Model-dependent variations] 

## TM-T90, TM-L90,TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-P60 

## TM-T90, TM-L90 

**In standard mode, the symbol which height exceeds 831 dots cannot be printed with this printer.** 

**When printing PDF417 symbols, the printer starts actual printing after it reaches control speed for printing symbol. The paper must be fed 10 dots or less in this operation. This area is not included in the vertical area transmitted by Function 082.** 
