## **C O N F I D E N T I A L** 

■ Horizontal tab position settings are effective until ESC @ is executed, the printer is reset, or the power is turned off. 

## ■ Print position can be changed by HT. 

■ When the left margin setting is changed, the horizontal tab position is also changed. 

[Model-dependent variations] None 

## **Program example for HT and ESC D** 

## **Program Example** 

## **Print Sample** 

PRINT #1, "0123456789012345678901234567890123456"; PRINT #1, CHR$(&HA); 

FOR i=1 TO 4 

PRINT #1, CHR$(&H9); "H"; ← Execute HT NEXT i : PRINT #1, CHR$(&HA); PRINT #1, CHR$(&H1B);"D";CHR$(10);CHR$(20); PRINT #1, CHR$(30);CHR$(0); ← Set HT positions FOR i=1 TO 4 PRINT #1, CHR$(&H9); "H"; ← Execute HT NEXT i : PRINT #1, CHR$(&HA); 

**==> picture [188 x 81] intentionally omitted <==**

**----- Start of picture text -----**<br>
0123456789012345678901234567890123456<br>H H H H<br>H H HH<br>↑ ↑ ↑<br>Tab Tab Tab<br>position positionposition<br>10 20 30<br>Default  → 8 16 24 32<br>**----- End of picture text -----**<br>
