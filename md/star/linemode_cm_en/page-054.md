**ESC k n1 n2 d1...dk** 

[Name] Fine density bit image [Code] ASCII ESC k n1 n2 d1 ... dk Hex. 1B 6B n1 n2 d1 ... dk Decimal 27 107 n1 n2 d1 ... dk 

[Defined Area] n2 = 0 1 ≤ {(n1 + n2 x 256) x 8} ≤ printable region k = {(n1 + n2 x 256) x 24} 0≤d≤255 

[Initial Value] - - - [Function] Prints bit images using 1 dot wide and 1 dots high per 1 dot of input data. The following shows the data processing in this command. 

• When {(n1 + n2 x 256) x 8} exceeds the printable region, data after d1 is handled as normal data. • When {(n1 + n2 x 256) x 8} exceeds the printable region that is currently set, only the data in the printing region is printed. 

At this time, all data for the print region is discarded. 

- If the current position already exceeds the print region, this command discards all data. 

|**24 Dots**|**X Bytes =(n1 + n2 x 256)**|**X Bytes =(n1 + n2 x 256)**|**X Bytes =(n1 + n2 x 256)**|**X Bytes =(n1 + n2 x 256)**|
|---|---|---|---|---|
||||||
||d1|d2|• • • • • • •|dX|
||dX x 1+1|dX x 1+2|• • • • • • •|dX x 2|
||dX x 2+1|dX x 2+2|• • • • • • •|dX x 3|
||•<br>•<br>•<br>•<br>•<br>•<br>•<br>•||•<br>•<br>•<br>•||
||dX x 23+ 1|dX x 23+ 2|• • • • • • •|dX x 24|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-36 
