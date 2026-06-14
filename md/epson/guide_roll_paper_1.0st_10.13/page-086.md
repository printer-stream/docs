## **C O N F I D E N T I A L** 

## **ESC FF** 

EXECUTING COMMAND 

[Name] Print data in page mode [Format] ASCII ESC FF Hex 1B 0C Decimal 27 12 [Range] None [Default] None 

- [Printers not featuring this command] TM-U230, TM-U220 

- [Description] In page mode, prints the data in the print buffer collectively. 

- [Notes] 

- This command is enabled only in page mode. Page mode can be selected by ESC L. 

- After printing, the printer does not clear the buffered data, the print position, or values set by other commands. 

- The printer returns to standard mode with FF, ESC S, and ESC @.  When it returns to standard mode by ESC @, all settings are canceled. 

- This command is used when the data in page mode is printed repeatedly. 

**Program Example for all printers Print Sample** AAAAA PRINT #1, CHR$(&H1B);"L"; ← Select page mode BBBBB PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); CCCCC PRINT #1, CHR$(&H1B);"W";CHR$(0);CHR$(0);CHR$(0); CHR$(0);CHR$(120);CHR$(0);CHR$(170);CHR$(0); PRINT #1, CHR$(&H1B);"T";CHR$(0); ← Select print direction AAAAA PRINT #1, "AAAAA"; CHR$(&HA); ← Store characters for printing BBBBB PRINT #1, "BBBBB"; CHR$(&HA); ← Store characters for printing CCCCC PRINT #1, "CCCCC"; CHR$(&H1B);CHR$(&HC); ← Batch print PRINT #1, CHR$(&HC); ← Batch print and return to standard mode 
