## **C O N F I D E N T I A L** 

[Model-dependent variations] TM-J2000/J2100, TM-T90, TM-T20,  TM-T88IV, TM-T88V, TM-T70, TM-L90 

## **Program example for ESC $ and ESC \** 

**Program Example Print Sample** 90/180 inch PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); PRINT #1, "ABCD"; ABCD     EFGH PRINT #1, CHR$(&H1B);"$";CHR$(90);CHR$(0); ← Set absolute position ABCD         EFGH PRINT #1, "EFGH"; CHR$(&HA); PRINT #1, "ABCD"; 90/180 inch PRINT #1, CHR$(&H1B);"\";CHR$(90);CHR$(0); ← Set relative position PRINT #1, "EFGH"; CHR$(&HA); 

## TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90 

**The vertical or horizontal motion unit is specified by** GS P **.** 
