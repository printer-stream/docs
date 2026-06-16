## C O N F I D E N T I A L

## Program Example for ESC L and ESC S

## Program Example for all printers

```
PRINT #1, CHR$(&H1B);"L"; ← Select page mode PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); PRINT #1, CHR$(&H1B);"W";CHR$(0);CHR$(0);CHR$(0); CHR$(0);CHR$(240);CHR$(0);CHR$(200);CHR$(0); PRINT #1, CHR$(&H1B);"T";CHR$(0); ← Select print direction PRINT #1, "AAAAA"; CHR$(&HA); PRINT #1, "BBBBB"; CHR$(&HA); PRINT #1, "CCCCC"; PRINT #1, CHR$(&H1B);CHR$(&HC); ← Batch print PRINT #1, CHR$(&H1B);"S"; ← Select standard mode
```

AAAAA

BBBBB

CCCCC

## Print Sample
