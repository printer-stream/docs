Page 5-7 

## LB The Label Instruction 

TB c...c +t 

- Purpose: Draws the character string using the currently selected character set. 

- Parameters: c...c — ASCII characters which may include control characters. 

- Terminator: t — label terminator defined by DT. Default is ETX, decimal 3. 

## LT The Line Type Instruction 

## Page 4-6 

- LT pattern number (, pattern length) (;) Purpose: Sets the line type used in drawing lines. Parameters: pattern number — integer between 0 and +6. Omitting parameter causes solid line. 

**==> picture [177 x 99] intentionally omitted <==**

**----- Start of picture text -----**<br>
O- specifies dots only at the points that are plotted.<br>1- See . ‘<br>No parameter (Default Value) ———————_—___-<br>**----- End of picture text -----**<br>


pattern length — decimal, 0 to 127.9999, a percentage of diagonal distance between P1 and P2. Default 4%. 

## OA The Output Actual Position and Pen Status Instruction 

## Page 7-3 

OA (;) 

Purpose: Used to output the pen’s physical position at time of command. 

Response: X,Y,P [TERM] — integers, in ASCII. 

X,Y — in plotter units within current window. 

P — 0, pen up or 1, pen down. 

INSTRUCTION SYNTAX B-5 
