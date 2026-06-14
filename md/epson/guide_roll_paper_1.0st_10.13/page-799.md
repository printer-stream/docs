## **C O N F I D E N T I A L** 

## **GS C 2** 

SETTING COMMAND 

[Name] Set counter [Format] ASCII GS C 2 nL nH Hex 1D 43 32 nL nH Decimal 29 67 50 nL nH [Range] 0 ≤ (nL + nH × 256) ≤ 65535 (0 ≤ nL ≤ 255, 0 ≤ nH ≤ 255) 

- [Default] (nL + nH × 256) = 1, nL = 1, nH = 0 

- [Printers not featuring this command] TM-J2000/J2100, TM-T90,TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-P60, TM-U230, TM-U220 

- [Description] Sets the serial number counter value. 

   - Specifies the counter value as (nL + nH × 256). 

## [Recommended Functions] 

This command is supported by some printer models but will not be supported by future models. Future models will not support counter value. 

- [Notes] 

- The serial counter values are stored by  GS c in the print buffer. 

- The setting of the counter value set by GS C ; is disabled by processing this command. 

- Settings of this command are effective until GS C ; is executed, ESC @ is executed, the printer is reset, or the power is turned off. 

**Program Example Print Sample** PRINT #1, CHR$(&H1D);"C1";CHR$(1);CHR$(0); PRINT #1, CHR$(44);CHR$(1);CHR$(1);CHR$(1); Line 010 PRINT #1, CHR$(&H1D);"C2";CHR$(10);CHR$(0); Line 011 PRINT #1, CHR$(&H1D);"C0";CHR$(3);CHR$(1); PRINT #1, "Line";CHR$(&H1D);"c";CHR$(&HA); PRINT #1, "Line";CHR$(&H1D);"c";CHR$(&HA); 
