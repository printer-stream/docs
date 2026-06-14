## **C O N F I D E N T I A L** 

TM-L90 **: [when receipt is selected]** 

nL **= 64,** nH **= 2 (when paper width is set to 80 mm to 78 mm)** 

- **256 +** ( **paper width - 38)** × **8 (when paper width is set to 77 mm to 38 mm)** 

**[when label paper is selected]** 

- nL **= 48,** nH **= 2 (when paper width is set to 80 mm)** 

**224 +** ( **paper width - 38)** × **8 (when paper width is set to 79 mm to 38 mm)** 

- TM-P60 **: [Peeler model]** 

nL **+** nH **x 256 = 388 (** nL **= 132,** nH **= 1)** 

**[Other than Peeler model]** 

- nL **= 164,** nH **= 1 (when paper width is set to 58 mm)** 

nL **= 176,** nH **= 1 (when paper width is set to 60 mm)** 

[Printers not featuring this command] TM-U230, TM-U220 

[Description] 

- [Notes] 

- In standard mode, sets the print area width to (nL + nH × 256) × (horizontal motion unit). 

- When standard mode is selected, this command is enabled only when processed at the beginning of the line. 

- The print area width has no effect in page mode. If this command is processed in page mode, the print area width is set and it is enabled when the printer returns to standard mode. 

- If the [left margin + print area width] exceeds the printable area, the print area width is automatically set to [printable area – left margin]. 

- If this command and GS L set the print area width to less than the width of one character, the print area width is extended to accommodate one character for the line. 

- Horizontal motion unit is used. 

- If horizontal motion unit is changed after setting the printable area width, the printable area width setting will not be changed. 

- Printable area width setting is effective until ESC @ is executed, the printer is reset, or the power is turned off. 

[Model-dependent variations] 

TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60 
