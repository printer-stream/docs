<!-- image -->

## 6. APPENDIX

## 6-1 Appendix	1	Cautions

&lt;Precautions relating to printing and paper feeds&gt;

- (1)This is a line printer.  Printing is always accompanied by a paper feed.  Therefore, if a value that is smaller than the print data is set for one line of a line feed, paper will be fed more than the set amount to print that data.

For example, if one line feed is set to 10 dots (10/180 inches), a paper feed of only 10 dots will occur, but if printing a bit image, paper will be fed 24 dots.

## Paper Feed Amount

|                     |                         | Necessary Paper Feed Amount (Dots)    |
|---------------------|-------------------------|---------------------------------------|
| Standard Characters | Font A                  | 24 x Vertical Direction Magnification |
| Standard Characters | Font B                  | 24 x Vertical Direction Magnification |
| Standard Characters | Chinese Character Fonts | 24 x Vertical Direction Magnification |
| Rotated             | Font A                  | 12 x Vertical Direction Magnification |
| Rotated             | Font B                  | 9 x Vertical Direction Magnification  |
| Rotated             | Chinese Character Fonts | 24 x Vertical Direction Magnification |
| Bit Image (ESC *)   | Bit Image (ESC *)       | 24                                    |

- (2)When the printer enters a data wait state for data from the host, printing and a paper feed is temporarily stopped, but when starting printing with data input, the paper feed can occur between 1 to 3 dots when starting printing.  This particularly affects printing of bit images.
- (3)The auto-cutter is recommended to after printing more than ten lines or after a paper feed.  (If the cut paper is too small, it may not be easy to discharge, or can cause a paper jam.)
