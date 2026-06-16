## C O N F I D E N T I A L

## [Model-dependent variations] None

## Program Example for all printers

```
PRINT #1, CHR$(&H1B);"{";CHR$(0); ← Cancel PRINT #1, "ABCDE"; CHR$(&HA); PRINT #1, "BCDEF"; CHR$(&HA); PRINT #1, CHR$(&H1B);"{";CHR$(1); ← Select PRINT #1, "ABCDE"; CHR$(&HA); PRINT #1, "BCDEF"; CHR$(&HA);
```

## Print Sample

Normal printing

ABCDE

BCDEF

BCDEF

ABCDE

Upside-down printing
