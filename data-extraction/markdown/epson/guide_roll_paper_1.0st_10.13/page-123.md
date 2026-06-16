## C O N F I D E N T I A L

## Program example for ESC % , ESC &amp; , and ESC ?

```
Program Example PRINT #1, CHR$(&H1B);"&";CHR$(2);"AC"; PRINT #1, CHR$(9); FOR i=1 TO 2*9 READ d: PRINT #1, CHR$(d); NEXT i PRINT #1, CHR$(9); FOR i=1 TO 2*9 READ d: PRINT #1, CHR$(d); NEXT i PRINT #1, CHR$(10); FOR i=1 TO 2*10 READ d: PRINT #1, CHR$(d); NEXT i PRINT #1, CHR$(&H1B);"%";CHR$(0); ← Select resident character PRINT #1, "A B C D E"; CHR$(&HA); PRINT #1, CHR$(&H1B);"%";CHR$(1); ← Select user-defined character PRINT #1, "A B C D E"; CHR$(&HA): PRINT #1, CHR$(&H1B);"?";"A"; ← Cancel the user-defined character PRINT #1, "A B C D E"; CHR$(&HA);
```

## Program Example (continued)

DATA &amp;H18,&amp;H00,&amp;H00,&amp;H00,&amp;H3C,&amp;H00,&amp;H00,&amp;H00 DATA &amp;H7E,&amp;H00,&amp;H00,&amp;H00,&amp;H3C,&amp;H00,&amp;H00,&amp;H00 DATA &amp;H18,&amp;H00 DATA &amp;H18,&amp;H00,&amp;H00,&amp;H00,&amp;H24,&amp;H00,&amp;H00,&amp;H00 DATA &amp;H42,&amp;H00,&amp;H00,&amp;H00,&amp;H24,&amp;H00,&amp;H00,&amp;H00 DATA &amp;H18,&amp;H00 DATA &amp;H00,&amp;H00,&amp;H10,&amp;H00,&amp;H20,&amp;H00,&amp;H5F,&amp;H00 DATA &amp;H00,&amp;H00,&amp;H81,&amp;H00,&amp;H00,&amp;H00,&amp;H5F,&amp;H00 DATA &amp;H20,&amp;H00,&amp;H10,&amp;H00

## Print Sample

A B C D E ← Characters from resident character set

♦ ◊ × D E ← Characters from user-defined character set

A ◊ × D E ← Characters from user-defined character set (cancel one character)
