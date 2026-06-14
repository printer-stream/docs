SP 

The Pen Select Instruction 

Page 3-2 

SP pen number (;) 

- Purpose: Selects or stores a pen. Parameter: integers. Omitting parameters or a parameter of 0 stores the pen. Odd-numbered parameter selects pen from left stall, even-numbered from right. 

## SR The Relative Character Size Instruction Page 5-16 . 

- SR. width, height ; Purpose: Sets the character width and height relative to Pl and P2 for labels. 

- Parameters: decimals representing a percentage of vertical or hoyrizontal distance between P1 and P2. Width — percentage of (P2x — P1x). Height — percentage of (P2y — Ply). Omitting parameters results in value 0.75 for width and 1.5 for height. 

## SS The Select Standard Character Set Page 5-4 Instruction 

- SS (5) Purpose: Selects the standard character set designated by the CS instruction as the character set used for subsequent labeling. 

## TL The Tick Length Instruction 

## Page 4-2 

- TL tp(,tn)() Purpose: Establishes the length of ticks drawn with the instructions XT and YT. 

- Parameters: decimals. tp — percentage of (P2y — Ply) for XT or (P2x — P1x) for YT. Denotes portion above the X-axis or to the right of the Y-axis when difference is positive. tn — same as tp except denotes portion below the X-axis and to the left of the Y-axis. Omitting parameters causes tick lengths tp and tn 0.5% of (P2y— Ply) or (P2x— Plx), the same as the default values. 

- B-10 INSTRUCTION SYNTAX 
