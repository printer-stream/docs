Rev.2.52 

## **GS \ nL nH** 

Specify relative position for character vertical direction in page mode 

Name Specify relative position for character vertical direction in page mode Code ASCII GS \ nL nH Hex. 1D 5C nL nH Decimal 29 92 nL nH 0 ≤ nL ≤ 255 Defined Region 0 ≤ nH ≤ 255 Function • Specifies the character vertical direction position for the data expansion starting position using the relative position based on the current point in page mode.  This sets the position moved from the current position to [(nL + nH x 256) x basic calculated pitch] for the next data expanding starting position. Details • When not in page mode, this command is ignored. • If the direction below the current position is specified for the characters, specify a positive number; if the direction above is specified, a negative number is used. • Negative numbers are represented by the complement of 65536.  For example, when moving in the upward direction N pitches, use: nL + nH × 256 = 65536-N • Specifications for relative positions that exceed the specified print region are ignored. 

- The following operations occur depending on ESC T (Selecting the character printing direction in page mode). 

- a. If the starting point is upper left or lower right, specify the relative position for the paper feed direction. 

Use the basic calculated pitch (y) for the horizontal direction at this time. 

   - b. If the starting point is upper right or lower left, specify the relative position for the paper feed in the vertical direction.  Use the basic calculated pitch (x) for the horizontal direction at this time. 

   - The basic calculated pitch is set by GSP (Set basic calculated pitch). 

- If the calculation results in fractions, the pitch is corrected to a minimal mechanical pitch and the rest is discarded. 

- Reference ESC $, ESC T, ESC W, ESC \, GS $, GS P 

ESC/POS Command Specifications 

144 
