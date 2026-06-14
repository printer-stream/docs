## **C O N F I D E N T I A L** 

[Notes] 

- Settings of this command are effective until ESC @ is executed, the printer is reset, the power is turned off, or one of the following commands is executed: 

   - Bit 0 (character font): ESC M 

   - Bit 3 (Emphasized mode): ESC E 

   - Bit 4, 5 (character size): GS ! 

   - Bit 7 (underline mode): ESC – 

- Configurations of Font 1 and Font 2 are different, depending on the printer model. If the desired font type cannot be selected with this command, use ESC M. 

- The print modes set by this command (Bit 0, 4, 5 and 7) are effective for alphanumeric, Kana, and userdefined characters. 

- Bit 0 is effective for 1-byte code characters. 

- Bits 3, 4, 5, and 7 are effective for 1-byte code characters and Korean characters. 

- The emphasized print modes set by this command (Bit 3) are effective for alphanumeric, Kana, multilingual, and user-defined characters. 

- When some characters in a line are double-height, all characters on the line are aligned at the baseline. 

- When double-width mode is turned on, the characters are enlarged to the right, based on the left side of the character. 

- When both double-height and double-width modes are turned on, quadruple size characters are printed. 

- In standard mode, the character is enlarged in the paper feed direction when double-height mode is selected, and it is enlarged perpendicular to the paper feed direction when double-width mode is selected. However, when character orientation changes in 90° clockwise rotation mode, the relationship between double-height and double-width is reversed. 

- In page mode, double-height and double-width are on the character orientation. 

- The underline thickness is that specified by ESC –, regardless of the character size. The underline is the same color as the printed character. The printed character’s color is specified by GS ( N <Function 48>. 

- When underline mode is turned on, 90° clockwise-rotated characters and white/black reverse characters cannot be underlined. 
