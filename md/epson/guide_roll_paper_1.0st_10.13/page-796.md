## **C O N F I D E N T I A L** 

## [Notes] 

■ The serial number counter is stored in the print buffer by GS c. 

■ Settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off. 

## **Program Example** 

PRINT #1, CHR$(&H1D);"C0";CHR$(3);CHR$(0); PRINT #1, "AAAAA";CHR$(&H1D);"c";CHR$(&HA); PRINT #1, CHR$(&H1D);"C0";CHR$(4);CHR$(1); PRINT #1, "BBBBB";CHR$(&H1D);"c";CHR$(&HA); 

## **Print Sample** 

AAAAA 1  ← 3 digits + right alignment + adding spaces to the left BBBBB0002 ← 4 digits + right alignment + adding "0"  to the left 
