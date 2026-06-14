## **C O N F I D E N T I A L** 

## [Notes for CODE93 (m = 72) process] 

- Start code and stop code are added automatically. 

- Check digits (2 character) are calculated and added automatically. 

- When HRI characters are designated to be added, special character HRI characters are processed as follows. 

   - The printer prints an HRI character " " as start and stop character. 

   - The printer prints HRI characters "■ + an alphabetic character"as control characters (not printable characters). 

[Notes for CODE128 (m = 73) process] 

- The first two-byte (d1, d2) start character must be code set selection character (any of CODE A, CODE B, or CODE C) which selects the first code set. 

- Check digit (1 character) is calculated and added automatically. 

- Special character HRI is processed as follows: 

   - The printer does not print HRI characters that correspond to the shift character or code set selection character (CODE A, CODE B, or CODE C). 

   - HRI characters of the function characters (FNC1, FNC2, FNC3, or FNC4) and control characters (in Hexadecimal: 00H to 1FH, 7FH / in Decimal 0 to 31, 127) are printed as spaces. 
