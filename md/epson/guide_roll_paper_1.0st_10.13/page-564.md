## **C O N F I D E N T I A L** 

## [Notes] 

- Settings of this command affect multilingual characters and user-defined characters. 

- Settings of this command are effective until any of the following commands are executed, ESC @ is executed, the printer is, or the power is turned off. 

   - Character size (bits 2 and 3): FS W, GS ! 

   - Underline (bit 7): FS – 

- When a double-height mode is specified, a character is enlarged based on a baseline of the character. 

- When a double-width mode is specified, a character is enlarged based on the left side of the character. 

- When both double-width and double-height modes are specified, quadruple-size characters are printed. 

- When double-height mode is selected in standard mode, a character is enlarged in the paper feed direction and when double-width mode is selected, a character is enlarged in the direction which is perpendicular to the paper feed direction. Therefore, when 90 ° clockwise-rotation is selected, the relationship between directions of enlargement of double-height and double-width is opposite from normal direction. 

- When double-height mode is selected in page mode, height size is enlarged and when double-width mode is selected in page mode, width size is enlarged. 

- When Kanji underline mode is specified, the width of the underline set by FS – is added. Even if the character size is changed, the width is not changed. The underline has the same color as the characters. The color can be selected by Function 48 of GS ( N. 

- Even if Kanji underline mode is specified, 90 ° clockwise-rotated characters, white/black reverse characters, and spaces skipped by HT, ESC $, or ESC \ are not underlined. 
