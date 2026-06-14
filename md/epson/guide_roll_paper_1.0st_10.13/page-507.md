## **C O N F I D E N T I A L** 

- x2L, x2H, y2L, y2H  set the line drawing end coordinate [X end position, Y end position] as the start position reference. 

   - X end position:  [(x2L + x2H × 256) × horizontal and vertical motion units] 

   - Y end position:  [(y2L + y2H × 256) × horizontal and vertical motion units] 

- m1 sets the type of line. The line width differs according to the model (refer to the model information). 

|■m1|sets the type of line. The line width differs|
|---|---|
|m1|**Line type**|
|1|Continuous line: Thin|
|2|Continuous line: Moderately thick|
|3|Continuous line: Thick|



## [Notes] 

- This function can be used when page mode is selected. Select page mode with ESC L. 

- You cannot specify a start coordinate [X start position, Y start position] and end coordinate [X end position, Y end position] that exceed the printing area set with ESC W. 

- You cannot specify a start coordinate [X start position, Y start position] and end coordinate [X end position, Y end position] that are the same coordinate. 

- Lines that can be drawn are lines horizontal in relation to characters (Y start position = Y end position) and lines vertical in relation to characters (X start position = X end position). Diagonal lines cannot be specified. 

- X and Y and the horizontal and vertical motion units used for the start position specified with ESC T are changed as shown in the table below. 
