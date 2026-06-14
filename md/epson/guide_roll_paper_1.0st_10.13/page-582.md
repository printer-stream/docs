## **C O N F I D E N T I A L** 

   - When this command is set in page mode, character spacing for multilingual (except Thai) characters printed in page mode is set. 

- If the horizontal or vertical motion unit is changed after setting the character spacing, the spacing between the characters is not changed. 

- The character spacing is effective until ESC @ is executed, the printer is reset, or the power is turned off. 

- This command is used to change spacing between characters. 

[Model-dependent variations] TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60, TM-U230, TM-U220 

## **Program Example** 

## **Print Sample** 

PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); ← Left- and right-side character spacing: 0 PRINT #1, CHR$(&H1C);"C"; CHR$(0): ← Select JIS code system ye mm PRINT #1, CHR$(&H1C);"&"; ← Specify Kanji mode iz a= ← Left- and right-side character spacing: PRINT #1, CHR$(&H1C);"S";CHR$(0);CHR$(0); approx. 1.129 mm {8/180"} PRINT #1, CHR$(&H34);CHR$(&H41); PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA); PRINT #1, CHR$(&H1C);"S";CHR$(8);CHR$(8); PRINT #1, CHR$(&H34);CHR$(&H41); PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA); PRINT #1, CHR$(&H1C);"."; ← Cancel Kanji mode 

## TM-J2000/J2100, TM-T90, TM-T88IV, TM-T88V, TM-T70, TM-L90 

**The horizontal and vertical motion units are set by** GS P **.** 

## TM-T20 **,** TM-P60 

**The horizontal and vertical motion unit is about 0.125 mm {1/203 inch}. This corresponds to 1 dot pitch.** 

## TM-U230, TM-U220 

**The horizontal motion unit is approximately 0.159 mm {1/160 inch}. This is equivalent to a half dot pitch.** 
