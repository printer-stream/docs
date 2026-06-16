## C O N F I D E N T I A L

[Model-dependent variations]

## TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90

```
Program Example for all printers
```

```
PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); PRINT #1, CHR$(&H1B);" ";CHR$(20); ← Set character spacing PRINT #1, CHR$(&H1B);"3";CHR$(15); ← Set line spacing PRINT #1, CHR$(&H1B);"V";CHR$(1); ← Select PRINT #1, "AAAAA"; CHR$(&HA); PRINT #1, "BBBBB"; CHR$(&HA); PRINT #1, "CCCCC"; CHR$(&HA); PRINT #1, CHR$(&H1B);"2"; ← Set line spacing PRINT #1, CHR$(&H1B);"V";CHR$(0); ← Cancel PRINT #1, "AAAAA"; CHR$(&HA); PRINT #1, "BBBBB"; CHR$(&HA); PRINT #1, "CCCCC"; CHR$(&HA);
```

<!-- image -->

## TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90

These printers don't support the 90 ° clockwise rotation mode (1.5-dot character spacing). The printer models use n as follows.

| n           | Function                                                         |
|-------------|------------------------------------------------------------------|
| 0, 48       | Turns off 90 ° clockwise rotation mode.                          |
| 1, 49 2, 50 | Turns on 90 ° clockwise rotation mode (1-dot character spacing). |
