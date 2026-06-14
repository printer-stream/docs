Rev.2.52 

## **6. APPENDIX 6-1 Appendix 1 Cautions** 

<Precautions relating to printing and paper feeds> 

- (1)This is a line printer.  Printing is always accompanied by a paper feed.  Therefore, if a value that is smaller than the print data is set for one line of a line feed, paper will be fed more than the set amount to print that data. 

For example, if one line feed is set to 10 dots (10/180 inches), a paper feed of only 10 dots will occur, but if printing a bit image, paper will be fed 24 dots. 

Paper Feed Amount 

|Paper Feed Amount|||
|---|---|---|
|||NecessaryPaper Feed Amount(Dots)<br>|
|Standard Characters|Font A|24 x Vertical Direction Magnifcation<br>|
||Font B|<br>24 x Vertical Direction Magnifcation|
||Chinese Character Fonts|<br>24 x Vertical Direction Magnifcation<br>|
|Rotated Character|Font A|<br>12 x Vertical Direction Magnifcation<br>|
||Font B|<br>9 x Vertical Direction Magnifcation<br>|
||Chinese Character Fonts|<br>24 x Vertical Direction Magnifcation|
|Bit Image(ESC *)||<br>24|



- (2)When the printer enters a data wait state for data from the host, printing and a paper feed is temporarily stopped, but when starting printing with data input, the paper feed can occur between 1 to 3 dots when starting printing.  This particularly affects printing of bit images. 

- (3)The auto-cutter is recommended to after printing more than ten lines or after a paper feed.  (If the cut paper is too small, it may not be easy to discharge, or can cause a paper jam.) 

ESC/POS Command Specifications 

264 
