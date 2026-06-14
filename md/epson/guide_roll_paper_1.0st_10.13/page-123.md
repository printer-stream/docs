## **C O N F I D E N T I A L** 

## **Program example for ESC %, ESC &, and ESC ?** 

## **Program Example** 

## **Program Example (continued)** 

PRINT #1, CHR$(&H1B);"&";CHR$(2);"AC"; PRINT #1, CHR$(9); FOR i=1 TO 2*9 READ d: PRINT #1, CHR$(d); NEXT i PRINT #1, CHR$(9); FOR i=1 TO 2*9 READ d: PRINT #1, CHR$(d); NEXT i PRINT #1, CHR$(10); FOR i=1 TO 2*10 READ d: PRINT #1, CHR$(d); NEXT i 

PRINT #1, CHR$(&H1B);"%";CHR$(0); ← Select resident character PRINT #1, "A B C D E"; CHR$(&HA); 

PRINT #1, CHR$(&H1B);"%";CHR$(1); ← Select user-defined character PRINT #1, "A B C D E"; CHR$(&HA): 

PRINT #1, CHR$(&H1B);"?";"A"; ← Cancel the user-defined character PRINT #1, "A B C D E"; CHR$(&HA); 

DATA &H18,&H00,&H00,&H00,&H3C,&H00,&H00,&H00 DATA &H7E,&H00,&H00,&H00,&H3C,&H00,&H00,&H00 DATA &H18,&H00 

DATA &H18,&H00,&H00,&H00,&H24,&H00,&H00,&H00 DATA &H42,&H00,&H00,&H00,&H24,&H00,&H00,&H00 DATA &H18,&H00 

DATA &H00,&H00,&H10,&H00,&H20,&H00,&H5F,&H00 DATA &H00,&H00,&H81,&H00,&H00,&H00,&H5F,&H00 DATA &H20,&H00,&H10,&H00 

## **Print Sample** 

A B C D E ← Characters from resident character set 

♦ ◊ � D E ← Characters from user-defined character set A ◊ � D E ← Characters from user-defined character set (cancel one character) 
