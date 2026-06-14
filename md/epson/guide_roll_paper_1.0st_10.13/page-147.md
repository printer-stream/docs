## **C O N F I D E N T I A L** 

|**Program Example for all printers**<br>PRINT #1, CHR$(&H1D);"(N";CHR$(2);CHR$(0);<br>PRINT #1, CHR$(48); CHR$(49);←Set character color 1<br>PRINT #1, "Color 1";<br>PRINT #1, CHR$(&H1D);"(N";CHR$(2);CHR$(0);<br>PRINT #1, CHR$(48); CHR$(50);←Set character color 2<br>PRINT #1,"Color 2";||**Print Sample**<br>Color 1_Color 2_|
|---|---|---|



## TM-J2000/J2100 

**The printer supports all functions.** 

**When using ink cartridge SJIC5 only for** TM-J2000 **, only Color 1 is available.** 

**When using ink cartridges SJIC2 and SJIC4 only for** TM-J2100 **, the following character colors are available.** 

|**available.**||
|---|---|
|**Color selection **|**Character color**|
|**Color 1**|**Black (SJIC3 (K))**|
|**Color 2**|**Red (SJIC4 (R)), Blue (SJIC4 (B)), Green (SJIC4 (G))**|
|**Color 3**|**Color 1 + Color 2**|



## TM-T90, TM-T88IV, TM-L90 

**This printer supports only Function 48.** 

**This function applies to printing characters on the two-color thermal paper.** 

|**Color selection **|**Character color**|**Controls**|
|---|---|---|
|**Color 1**|**Black (KR, KB, KG) **|**Print by high energy**|
|**Color 2**|**Red (KR)**|**Print by low energy**|



**Characters printed  with Color 2 may fade, depending on the storage environment. Therefore, when the printing needs to last a long time, print with Color 1.** 
