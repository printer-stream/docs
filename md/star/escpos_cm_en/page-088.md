Rev.2.52 

## **GS $ nL nH** 

Name Specify absolute position for character vertical direction in page mode Code ASCII GS $ nL nH Hex. 1D 24 nL nH Decimal 29 36 nL nH Defined Region 0 ≤ nL ≤ 255, 0 ≤ nH ≤ 255 Function Specifies the character vertical direction position for the data expansion starting position using the absolute position based on the starting point in page mode.  The position of the character vertical direction for the next data expansion starting position is the position specified by [(nL + nH x 256) x basic calculated pitch] from the starting point. Details • When not in page mode, this command is ignored. • Specifications for absolute positions that exceed the specified print range are ignored. 

- The position of the character horizontal direction of the data expansion starting position does not move. 

- The starting point that is used as a reference is specified by ESC T. 

- The following operations occur depending on the starting point of (Selecting the character printing direction in page mode) ESC T. 

- a. If the starting point is upper left or lower right, specify the absolution position for the paper feed direction (character vertical direction).  Use the basic calculated pitch (y) for the horizontal direction at this time. 

- b. If the starting point is upper right or lower left, specify the absolution position for the paper feed in the vertical direction (character vertical direction).  Use the basic calculated pitch (x) for the horizontal direction at this time. 

- The basic calculated pitch is set by GSP (Set basic calculated pitch). 

- If the calculation results in fractions, the pitch is corrected to a minimal mechanical pitch and the rest is discarded. 

Reference ESC $, ESC T, ESC W, ESC \, GS P, GS \ 

See section 2. Explanations of the Page Mode. 

ESC/POS Command Specifications 

88 
