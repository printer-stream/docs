Rev.2.52 

## **GS W nL nH** 

Name Set print region width Code ASCII GS W nL nH Hex. 1D 57 nL nH Decimal 29 87 nL nH 0 ≤ nL ≤ 255 Defined Region 0 ≤ nH ≤ 255 Initial Value See the  Appendix -4 Function • Sets the print region width specified by nL and nH. 

- Print region width is [(nL + nH x 256) x basic calculated pitch]. 

Printable Region Left Margin Print Region Width 

- Details • This command is effective only when processed at the top of the line when standard mode is being used. 

   - This command has no affect on page mode when in page mode.  Only the setting is effective for this command. 

   - When a value that exceeds the printable region of one line, the entire region, excluding the left margin, is set as the print region width. 

   - The basic calculated pitch is set by GSP (Set basic calculated pitch).  Also, the set printing region width is not changed even if the basic calculated pitch is changed after setting the print region width. 

   - Use the basic calculated pitch (x) for the horizontal direction of GS P (Set basic calculated pitch) to calculate the print region width. 

If the calculation results in fractions, the pitch is corrected to a minimal mechanical pitch and the rest is discarded. 

- If the print region width is smaller than the width of the first character expanded at the top of the line (including the right space), the following are processed only on that line. 

1. The print region is expanded to the right for the size of that character within the range that does not exceed the printable region. 

2.  If there is not enough space even if 1. is executed, the print region is expanded to the left side. 

3.  If there is not enough space even if 2. is executed, the right space deleted. 

- See Appendix-4 for setting details. 

Reference GS L, GS P, Appendix -4 

ESC/POS Command Specifications 

143 
