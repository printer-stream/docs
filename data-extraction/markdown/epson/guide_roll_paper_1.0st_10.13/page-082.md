## C O N F I D E N T I A L

## [Model-dependent variations] None

## Program Example for all printers

PRINT #1, CHR$(&amp;H1B);"L"; ← Select page mode PRINT #1, CHR$(&amp;H1D);"P";CHR$(180);CHR$(180); PRINT #1, CHR$(&amp;H1B);"W";CHR$(0);CHR$(0);CHR$(0); CHR$(0);CHR$(60);CHR$(0);CHR$(90);CHR$(0); PRINT #1, CHR$(&amp;H1B);"T";CHR$(0); PRINT #1, "AAAAA"; CHR$(&amp;HA); ← Store characters for printing PRINT #1, "BBBBB"; CHR$(&amp;HA); ← Store characters for printing PRINT #1, "CCCCC"; CHR$(&amp;HC); ← Batch print

## Print Sample

AAAAA BBBBB CCCCC
