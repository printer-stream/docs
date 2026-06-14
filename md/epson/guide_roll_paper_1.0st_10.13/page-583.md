## **C O N F I D E N T I A L** 

## **FS W** 

SETTING COMMAND 

[Name] Turn quadruple-size mode on/off for Kanji characters [Format] ASCII FS W n Hex 1C 57 n Decimal 28 87 n 

- [Printers not featuring this command] None 

- [Range] 0 ≤ n ≤ 255 

- [Default] n = 0 

- [Description] Turns quadruple-size mode on or off for multi-byte code character. 

   - When the LSB of n is 0, quadruple-size mode is turned off and normal size is specified. 

   - When the LSB of n is 1, quadruple-size mode is turned on. 

- [Notes] 

- Settings of this command affect multilingual characters and user-defined characters. 

- When a double-height mode is specified, a character is enlarged based on a baseline of the character and when a double-width mode is specified, a character is enlarged based on the left side of the character. 

- Settings of this command are effective until FS ! is executed, GS ! is executed, ESC @ is executed, the printer is reset, or the power is turned off. 

|**Program Example**<br>PRINT #1, CHR$(&H1C);"C";CHR$(0);<br>←Select JIS code system<br>PRINT #1, CHR$(&H1C);"&";<br>PRINT #1, CHR$(&H1C);"W";CHR$(0);<br>←Cancel quadruple-size mode<br>PRINT #1, CHR$(&H34);CHR$(&H41);<br>PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA);<br>PRINT #1, CHR$(&H1C);"W";CHR$(1);<br>←Specify quadruple-size mode<br>PRINT #1, CHR$(&H34);CHR$(&H41);<br>PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA);<br>PRINT #1, CHR$(&H1C);".";|**Print Sample**<br>←Normal size<br>←Quadruple size<br>ae<br>ik|
|---|---|
