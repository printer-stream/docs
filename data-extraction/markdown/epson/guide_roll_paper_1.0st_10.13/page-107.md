## C O N F I D E N T I A L

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 , TM-U230 , TM-U220

## Program Example for all printers

```
PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); PRINT #1, CHR$(&H1B);" ";CHR$(0); ← Character spacing set to 0 PRINT #1, "AAAAA"; CHR$(&HA); PRINT #1, CHR$(&H1B);" ";CHR$(6); ← Character spacing set to 6 PRINT #1, "BBBBB"; CHR$(&HA); PRINT #1, CHR$(&H1B);" ";CHR$(12); ← Character spacing set to 12 PRINT #1, "CCCCC"; CHR$(&HA);
```

## Print Sample

AAAAA ← 0-inch character spacing BBBBB ← 6/180-inch character spacing C C C C C ← 12/180-inch character spacing

## TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90

The vertical or horizontal motion unit is specified by GS P .

## TM-P60

The horizontal or vertical motion unit is approximately 0.125 mm {1/203 inches}. This value equals one dot pitch.

## TM-U230

The horizontal motion unit is 0.159 mm {1/160 inch}. This value equals a half dot pitch. This command does not use the vertical motion unit because the printer does not support page mode.

## TM-U220

The horizontal motion unit is 0.159 mm {1/160 inch}. This value equals a half dot pitch. This command does not use the vertical motion unit because the printer does not support page mode.
