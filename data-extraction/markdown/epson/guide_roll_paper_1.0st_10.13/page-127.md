## C O N F I D E N T I A L

- ■ Configurations of Font A and Font B depend on the printer model.
- ■ The settings of this command are effective until ESC ! is executed, ESC @ is executed, the printer is reset, or the power is turned off.

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 , TM-U220

## Program Example for all printers

PRINT #1, CHR$(&amp;H1B);"M";CHR$(0); Select font A

PRINT #1, CHR$(&amp;H1B);"M";CHR$(1); Select font B

```
← PRINT #1, "AAAAA";CHR$(&HA); ← PRINT #1,"BBBBB";CHR$(&HA);
```

## TM-J2000/J2100 , TM-T90 , TM-L90

## [Other than Japanese model]

## Character configurations

Font A: (12 × 24)

Font B: (9 17)

×

## Each character's baseline is as follows:

Font A (12 × 24): 21 dots from the top of a character. Font B (9 × 17): 16 dots from the top of a character.

## [Japanese model]

## Character configurations

Font A: (12 24)

×

Font B: (10 × 24)

Font C: (8 × 16)

## Each character's baseline is as follows:

Font A (12 × 24): 21 dots from the top of a character.

Font B (10 × 24): 21 dots from the top of a character.

Font C (8 × 16): 15 dots from the top of a character.

## Print Sample

AAAAA ← Font A

BBBBB ←

Font B
