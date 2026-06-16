## C O N F I D E N T I A L

[Model-dependent variations]

TM-J2000/J2100 , TM-U230 , TM-U220

## Program Example for all printers

PRINT #1, CHR$(&amp;H1B);"r";CHR$(1); ← Select red

PRINT #1, "AAAAA";CHR$(&amp;HA);

PRINT #1, CHR$(&amp;H1B);"r";CHR$(0); ← Select black

PRINT #1,"BBBBB";CHR$(&amp;HA);

## TM-J2000/J2100

GS ( N or GS ( L are recommended when defining two-color printing with this printer.

When standard mode is selected, setting of this command affects the printing characters, ESC * , NV bit images, and downloaded bit images.

This command cannot be used with the TM-J2000 (single-color model).

## TM-U230

This command is enabled with the two-color model.

## TM-U220

This command is enabled with the two-color model.

AAAAA ← Red BBBBB ← Black

Print Sample
