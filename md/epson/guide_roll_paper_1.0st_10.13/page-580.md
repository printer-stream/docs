## **C O N F I D E N T I A L** 

**Program Example Print Sample** PRINT #1, CHR$(&H1C);"C";CHR$(0); ← Select JIS code system ← Print using JIS code PRINT #1, CHR$(&H1C);"&"; ← Specify Kanji mode ie ← Print using SHIFT JIS code PRINT #1, CHR$(&H34);CHR$(&H41); PRINT #1, CHR$(&H3B);CHR$(&H7A); CHR$(&HA); PRINT #1, CHR$(&H1C);"."; ← Cancel Kanji mode PRINT #1, CHR$(&H1C);"C";CHR$(1); ← Select SHIFT JIS code system PRINT #1, CHR$(&H8A);CHR$(&HBF); PRINT #1, CHR$(&H8E);CHR$(&H9A); CHR$(&HA); 
