## **C O N F I D E N T I A L** 

|**Program Example**<br>PRINT #1, CHR$(&H1C);"C";CHR$(0);<br>←Select JIS code system<br>PRINT #1, CHR$(&H1C);"&";<br>PRINT #1, CHR$(&H1C);"-";CHR$(1);<br>←Select underline mode<br>PRINT #1, CHR$(&H34);CHR$(&H41);<br>PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA);<br>PRINT #1, CHR$(&H1C);"-";CHR$(0);<br>←Cancel underline mode<br>PRINT #1, CHR$(&H34);CHR$(&H41);<br>PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA);<br>PRINT #1, CHR$(&H1C);".";<br>←Cancel Kanji mode|**Print Sample**<br>←1-dot width underline added<br>←No underline|
|---|---|
