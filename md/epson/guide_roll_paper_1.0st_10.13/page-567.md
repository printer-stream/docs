## **C O N F I D E N T I A L** 

■ When Kanji mode is selected, the printer processes a character code that corresponds to the first byte of Kanji code, and then processes a consecutive byte as the second byte of Kanji code. Therefore, when Kanji code is specified, an ASCII code character that corresponds to the first byte of Kanji code cannot be printed. 

## ■ Kanji mode is selected at default. 

|**Program Example**<br>PRINT #1, CHR$(&H1C);"C";CHR$(0);<br>←<br>Select JIS code system<br>PRINT #1, CHR$(&H1C);"&";<br>←<br>Specify Kanji mode<br>PRINT #1, CHR$(&H34);CHR$(&H41);<br>PRINT #1, CHR$(&H3B);CHR$(&H7A); CHR$(&HA);|**Print Sample**|
|---|---|
