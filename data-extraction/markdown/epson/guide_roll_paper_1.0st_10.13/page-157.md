## C O N F I D E N T I A L

[Model-dependent variations]

None

## Program Example for all printers

PRINT #1, CHR$(&amp;H1D);"B";CHR$(1); ← Select PRINT #1, "AAAAA"; CHR$(&amp;HA); PRINT #1, CHR$(&amp;H1D);"B";CHR$(0); ← Cancel PRINT #1, "BBBBB"; CHR$(&amp;HA);

## Print Sample

<!-- image -->

White/black reverse printing

BBBBB ← Normal printing AAAAA ←
