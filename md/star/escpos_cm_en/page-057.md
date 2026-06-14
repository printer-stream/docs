Rev.2.52 

## **ESC D n1 … nk NUL** 

Name Set horizontal tab position Code ASCII ESC D n1...nk NUL Hex. 1B 44 n1...nk NUL Decimal 27 68 n1...nk NUL 1 ≤ n ≤ 255 Defined Region 0 ≤ k ≤ 32 Initial Value • Every 8 characters when using Font A (12 x 24) and the setting for the right spacing of characters is 0.   (9[th] column, 17[th] column, 25[th] column …) Function Sets horizontal tab position • n specifies the column number for setting a horizontal tab position from the left margin or the beginning of the line. • k indicates the number of horizontal tab positions to be set. Details • The horizontal tab position is a value of from the left margin or the beginning of the line [n x character width]. Character width is the horizontal width including ESC SP (character right space).  If the character horizontal direction magnification ratio is more than 2, the character width is also enlarged accordingly. 

- This command cancels the previous set horizontal tab settings. 

- When horizontal tab position setting n = 8, the next print position is moved to column 9 by executing HT (horizontal tab). 

- Up to 32 tab positions (k = 32) can be set. Subsequent data exceeding that is processed as normal data. 

- <n> for specifying horizontal position settings is input in ascending order.  It is quit using <00>H.  If <n> is less than or equal to the preceding value <n>, horizontal tab setting is completed and subsequent data is processed as normal data. 

- ESC D NULL cancels all horizontal tab positions. 

- Previously specified horizontal tab positions do not change, even if the character width changes after setting the horizontal tab position. 

The character width is stored for standard and page modes. 

- STAR • When using Chinese character mode, set for the pitch of the ANK fonts (Font-A and Font-B). 

   - If <n> exceeds the printable region, set the horizontal tab position to the position +1 of the maximum print column count. 

Reference 

HT 

ESC/POS Command Specifications 

57 
