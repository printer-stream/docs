## **5-6-3. Print Data Expansion to the Print Region** 

Expanding print data to the print region is performed in the following way. 

- (1) The print region is set by ESC GS P 3, but when all printing and paper feeds are ended before the printer receives ESC GS P 3 the left edge when facing the printer becomes the origin of the print region (x0, y0). The print region is a square shape using dx pitch for the x direction (horizontal direction) and dy pitch for the y direction (perpendicular direction) as sides, including the origin point from the origin points (x0, y0). (When ESC GS P 3 is not set, the initial value is the print region.) 

- (2) When the print region is set by ESC GS P 3, and the printer receives print data after the print direction is set by ESC GS P 2, point A in Fig. 2.3.1 becomes the starting point initial value, and the print data is expanded in the print region. For characters, this starting point is the base line. Downloaded bit images and bar codes are expanded using the lower left-hand point of the image data as the baseline (Point B in Fig. 5.9.3.1). However, HRI characters with a bottom bar code are printed below the base line. When expanding characters (double-tall characters) higher than the standard character height and download bit images and the like at the starting point, the portion higher than the standard characters is not printed. 

- (3) If the print data is out of the print region (including character right spaces) before receiving commands that accompany line feeds (LF, ESC J and the like), the line feed is automatically performed in the print region, and the expansion position of the print data is moved one line so the next expansion position is at the top of the line. The line feed amount at that time uses the line feed amount set by ESC 0 and ESC 1. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-25 
