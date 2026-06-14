## **5.6. Appendix 6 Explanation of Page Mode** 

## **5-6-1. O verview** 

This printer is equipped with two print modes. They are standard and page mode. 

In standard mode, the printer prints and feeds paper each time it receives the print and paper feed instructions, but the print and paper feed instructions received in page mode are executed on the print region on the specified memory and the printer does not operate. Then, when the ESC GS P6 or ESC GS P7 commands are executed, the printer batch expands data to the printing region and prints. In other words, when printing and performing a line feed for data of “ABCDEF” <LF>, in standard mode, “ABCDEF” is printed and paper is fed one line. In page mode, however, “ABCDEF” is written to the print region specified on the memory, and one line is moved on the memory to write the next print data. This printer will enter page mode using ESC GS P 0. Commands received thereafter are all processed as page mode. By running ESC GS P 6, you can lump-print received data. Also, by running ESC GS P 7, you can return to standard mode after lump printing received data. You can return to standard mode without printing page mode print data using ESC GS P 1. However, print data will be cleared. 

<Transitioning to Standard Mode and Page Mode> 

## **5-6-2. Setting Values Using Each Command in Standard Mode and Page Mode** 

- The values set by each command are shared by both standard and page modes. However, only the settings of the following commands are independently set. 

- → ESC 0, ESC M, ESC P, ESC :, ESC g, ESC SP, ESC 0, ESC z, ESC 1, ESC D, ESC P, ESC s, ESC t,  ESC p 

## • The following commands are invalid in page mode. 

→ ESC GS c, ESC GS ) B, ESC RS m, ESC RS A, ESC GS M, ESC GS r, ESC GS %, ESC GS * 0, ESC RS C, ESC *, ESC RS r 

ESC RS L, ESC FS p, VT, FF, 

- The maximum number of dots is prescribed in standard mode, but the y directions (the x direction when there is no rotation) when printing is rotated 90 or 270º are larger than that. For details, see the setting (ESC GS P 3) command of the print region in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-24 
