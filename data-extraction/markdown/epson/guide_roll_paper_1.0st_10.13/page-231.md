## C O N F I D E N T I A L

## Program Sample 2 (Printing graphics data)

## * Description for image data has been omitted.

```
PRINT #1, CHR$(&H1D);"(L";CHR$(250);CHR$(0);CHR$(48);CHR$(112);CHR$(48); ← Function 112: sending data (raster) PRINT #1, CHR$(1);CHR$(1); ← Specifies size (horizontal (times 1) ✕ vertical (times 1)) PRINT #1, CHR$(49); ← Specifies color 1 PRINT #1, CHR$(80);CHR$(0); ← Horizontal size (80 dots) PRINT #1, CHR$(24);CHR$(0); ← Vertical size (24 dots) FOR i=1 to 240 ← Image data (240 bytes) READ a$: d=VAL("&H"+a$): PRINT #1, CHR$(d); NEXT i PRINT #1, CHR$(&H1D);"(L";CHR$(250);CHR$(0);CHR$(48);CHR$(112);CHR$(48); ← Function 112: sending data (raster) PRINT #1, CHR$(1);CHR$(1); ← Specifies size (horizontal (times 1) ✕ vertical (times 1)) PRINT #1, CHR$(50); ← Specifies color 2 PRINT #1, CHR$(80);CHR$(0); ← Horizontal size (80 dots) PRINT #1, CHR$(24);CHR$(0); ← Vertical size (24 dots) FOR i=1 to 240 ← Image data (240 bytes) READ a$: d=VAL("&H"+a$): PRINT #1, CHR$(d); NEXT i PRINT #1, CHR$(&H1D);"(L";CHR$(2);CHR$(0);CHR$(48);CHR$(50); ← Function 50: printing graphics data
```
