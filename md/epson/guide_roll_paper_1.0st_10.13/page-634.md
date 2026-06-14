## **C O N F I D E N T I A L** 

- Printing of symbol is not affected by print mode (emphasized, double-strike, underline, white/ black reverse printing, or 90° clockwise-rotated), except for character size and upside-down print mode. 

- In standard mode, this command executes paper feeding for the amount needed for printing the symbol, regardless of the paper feed amount set by the paper feed setting command. The print position returns to the left side of the printable area after printing the symbol, and printer is in the status “beginning of the line,” or “there is no data in the print buffer.” 

- In page mode, the printer stores the symbol data in the print buffer without executing actual printing. The printer moves print position to the next dot of the last data of the symbol. 

- The quiet zone is not included in the printing data. Be sure to secure the quiet zone when using this function. 

[Model-dependent variations] 

## TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60 

## TM-T90, TM-T88IV, TM-T70 

**This model does not support this function.** 

## TM-T20, TM-T88V, TM-L90 

**When printing MaxiCode symbols, the printer starts actual printing after it reaches the control speed for printing symbols. It is needed to feed paper amount of 10 dots or less in this operation. This area is not included in the vertical area transmitted by Function 282.** 

## TM-P60 

TM-P60 **with peeler supports this function.** 

**MaxiCode symbols are printed with the “printing control mode = fine” regardless of the setting of Function 48 of** GS ( K **.** 
