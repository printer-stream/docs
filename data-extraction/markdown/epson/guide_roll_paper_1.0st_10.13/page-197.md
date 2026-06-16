## C O N F I D E N T I A L

## Program example for GS L and GS W

```
Program Example Set print area width
```

```
PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); PRINT #1, "01234567890123456789"; CHR$(&HA); PRINT #1, CHR$(&H1D);"L";CHR$(60);CHR$(0); ← Set left margin PRINT #1, CHR$(&H1D);"W";CHR$(120);CHR$(0); ← PRINT #1, "01234567890123456789"; CHR$(&HA);
```

## TM-J2000/J2100 , TM-T90

The horizontal motion unit is specified by GS P .

See GS ( E Functions 5 for specifying the paper width.

## TM-T20 , TM-T88IV , TM-T88V , TM-T70

The horizontal motion unit is specified by GS P .

## TM-L90

The horizontal motion unit is specified by GS P .

When a set value of the paper layout (horizontal size of the print area) is smaller than the print area (initial value of this command), it is not possible to print in the area where the paper layout (horizontal size of the print area) is exceeded.

See GS ( E Functions 5 for specifying the paper width.

See GS ( E Functions 49 and 50 for the paper layout (origin of layout, horizontal size of print area).

## Print Sample

<!-- image -->
