## C O N F I D E N T I A L

## Program Example

```
PRINT #1, CHR$(&H1C);"C";CHR$(0); ← Select JIS code system PRINT #1, CHR$(&H1C);"&"; ← Specify Kanji mode PRINT #1, CHR$(&H34);CHR$(&H41); PRINT #1, CHR$(&H3B);CHR$(&H7A); CHR$(&HA); PRINT #1, CHR$(&H1C);"."; ← Cancel Kanji mode PRINT #1, "kanji"; CHR$(&HA);
```

## Print Sample
