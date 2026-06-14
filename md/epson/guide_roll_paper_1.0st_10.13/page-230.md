## **C O N F I D E N T I A L** 

[Model-dependent variations] TM-J2000/J2100, TM-T90, TM-L90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-P60 

## **Program Sample 1 (Defining and printing NV graphics data)** 

## * Description for image data has been omitted. 

PRINT #1, CHR$(&H1D);"(L";CHR$(76);CHR$(6);CHR$(48);CHR$(67);CHR$(48); ← Function 67: defining data (raster) 

PRINT #1, "G1"; ← Key code PRINT #1, CHR$(2); ← Color no. PRINT #1, CHR$(80);CHR$(0); ← Horizontal size (80 dots) PRINT #1, CHR$(80);CHR$(0); ← Vertical size (80 dots) PRINT #1, CHR$(49); ← Specifies Color 1 FOR i=1 to 800 ← Image data (800 bytes) for Color 1 READ a$: d=VAL("&H"+a$): PRINT #1, CHR$(d); NEXT i PRINT #1, CHR$(50); ← Specifies color 2 FOR i=1 to 800 ← Image data (800 bytes) for Color 2 READ a$: d=VAL("&H"+a$): PRINT #1, CHR$(d); NEXT i 

PRINT #1, CHR$(&H1D);"(L";CHR$(6);CHR$(0);CHR$(48);CHR$(69); ← Function 69: Printing NV graphics Data PRINT #1, "G1"; ← Key code PRINT #1, CHR$(2);CHR$(1); ← Specifies size (horizontal (times 2) ✕ vertical (times 1)) 
