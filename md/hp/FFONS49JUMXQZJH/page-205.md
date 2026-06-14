Page 5-5 

## SA The Select Alternate Character Set Instruction 

- SA (;) Purpose: Selects the alternate character set designated by the CA instruction as the character set to be used for subsequent labeling. 

## SC. The Scale Instruction 

Page 2-6 

- SC Xmin, Xmax, Ymin, Ymax (;) Purpose: Scales the plotting area into user units. Parameters: Integers. 

## SI The Absolute Character Size Instruction 

Page 5-15 

- SI width, height ; 

- Purpose: Sets character width and height in centimetres for labels. Parameters: width, height — decimals representing centimetres, —128 to +127.9999. 

   - Omitting parameters establishes size of 0.19,0.27, the same as the default SR sizing with default P1,P2. 

## SL The Character Slant Instruction 

Page 5-18 

- SE tan@(;) 

- Purpose: Establishes the slant for labeled characters. 

- Parameters: decimal, —128 to +127.9999, interpreted as the tangent of the angle from vertical. 

Omitting parameters establishes no slant, the same as the default or SLO. 

## SM The Symbol Mode Instruction SM character (;) 

## Page 4-4 

Purpose: Causes specified symbol to be drawn at each plotted point. 

- Parameter: Any printing character ASCII 33 through 127 excluding semicolon (ASCII 59). SM space, SM control character, or SM; cancels symbol mode. 

INSTRUCTION SYNTAX B-9 
