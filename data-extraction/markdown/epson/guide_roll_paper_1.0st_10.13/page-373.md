## C O N F I D E N T I A L

- ■ HRI character is Human Readable Interpretation character indicated with bar code.

## Program Example for all printers

```
PRINT #1, CHR$(&H1D);"h";CHR$(80); ← Set height PRINT #1, CHR$(&H1D);"f";CHR$(0); ← Select font FOR n=0 to 3 PRINT #1, CHR$(&H1D);"H";CHR$(n); ← Select print position PRINT #1, CHR$(&H1D);"k";CHR$(2); ← Print bar code PRINT #1, "496595707379";CHR$(0); PRINT #1, CHR$(&HA); NEXT n
```

<!-- image -->
