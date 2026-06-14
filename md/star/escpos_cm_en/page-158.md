Rev.2.52 

## **GS v 0 m xL xH yL yH d1 … dk** 

Name Print raster bit images 

Code ASCII GS v 0 m xL xH yL yH d1...dk Hex. 1D 76 30 m xL xH yL yH d1...dk Decimal 29 118 48 m xL xH yL yH d1...dk 

Defined Region 0 ≤ m ≤ 3, 48 ≤ m ≤ 51 0 ≤ xL ≤ 128, xH=0  (0 ≤ xL +xH×256)  ≤ 128) 0 ≤ yL ≤ 255, 0 ≤ yH ≤ 15  (0 ≤ yL +yH×256  ≤ 4095) 0 ≤ d ≤ 255 k =  (xL+xH×256) × (yL+yH×256)   However, k ≠ 0 

Function Prints raster method bit images using mode m. 

|m|Mode|Densityof Vert. Dir. Dots|Densityof Hor. Dir. Dots|
|---|---|---|---|
|0,48|Normal Mode|180 DPI|180 DPI|
|1,49|Double-wide Mode|180 DPI|90 DPI|
|2,50|Double-tall Mode|90 DPI|180 DPI|
|3,51|Quadruple Mode|90 DPI|90 DPI|



   - xL and xH specify the horizontal direction data count for one bit image (xL + xH x 256) in bytes. 

   - yL and yH specify the vertical direction data count for one bit image (yL + yH x 256) in dots. 

- Details • This command is effective only when there is no print data in the print buffer when standard mode is selected. 

   - Print modes (character size, enhanced characters, duplicated characters, upside down, unline, black/white inverted, etc.) do not affect raster bit images. 

   - Data not in the print region is discarded in dot increments. 

   - It is possible to specify any position to start printing raster bit images according to HT (Horizontal tab), ESC $ (Specify absolute position), ESC \ (Specify relative position) and GS L (Specify let margin).  However, if the print starting position is no a multiple of 8, printing speed will decrease. 

   - ESC a (Position alignment) settings are effective also for raster bit images. 

   - When executing this command while defining a macro, the macro definition is terminated and the command commences with processing. 

The macro during this time is undefined. 

   - d specifies defined data. 

   - Bits that correspond to the dots to print are 1, and the bits that correspond to the dots that are not printed are 0. 

- STAR • On STAR printers, the ACK pulse width when using a parallel interface is fixed at 1 μsec. 

   - When in page mode, transmission of this command is prohibited. If sent, the results of the print are not guaranteed. 

   - Dot density (when the STAR printer head = 203 DPI) on STAR printers. 

ESC/POS Command Specifications 

158 
