## **C O N F I D E N T I A L** 

## ■ The relationship between the defined data and a print result is as follows. 

Example: data of the definition of the user defined character (2 bytes in vertical × 16 dots in horizontal) is necessary. (k = 32) 

|d1|d3|d5|...|d27|d29|d31|
|---|---|---|---|---|---|---|
|d2|d4|d6|...|d28|d30|d32|



## [Model-dependent variations] 

TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60, TM-U230, TM-U220 

|**Program Example**<br>PRINT #1, CHR$(&H1C);"C"; CHR$(0):<br>←Select JIS code system<br>PRINT #1, CHR$(&H1C);"2";<br>PRINT #1, CHR$(&H77);CHR$(&H21);<br>FOR k = 1 To 32<br>READ d: PRINT #1, CHR$(d);<br>NEXT k<br>PRINT #1, CHR$(&H1C);"&";<br>←Specify Kanji mode<br>PRINT #1, CHR$(&H77);CHR$(&H21);<br>PRINT #1, CHR$(&H33);CHR$(&H30);<br>PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA);<br>PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA);<br>PRINT #1, CHR$(&H1C);".";<br>←Cancel Kanji mode<br>DATA &H00, &H00, &H00, &H00, &H01, &HE0, &H07, &HF0<br>DATA &H0F, &HF0, &H1F, &HF2, &H3F, &HE2, &H7F, &HFE<br>DATA &H7F, &HFE, &H3F, &HE2, &H1F, &HF2, &H0F, &HF0<br>DATA &H07, &HF0, &H01, &HE0, &H00, &H00, &H00, &H00|**Print Sample**|
|---|---|
