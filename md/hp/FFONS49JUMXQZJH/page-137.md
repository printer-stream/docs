TEK 4051 Example: 

100 DIM A$(13], 8801] 110 A$=" SENDING DATA 120 Y¥=2000 130 B=4051 135 BS=CHR(3) 140 PRINT @5:"SP1;PA1000,73 **"** 5"s 150 PRINT @5:"LBTEK" ;B;A$; BS 160 END 

No terminator is sent by the TEK 4051. It must, therefore, be included in each PRINT @ 5 statement if the last HP-GL command in the line requires one. In line 140, all characters after the Y may be omitted, since the terminator is optional with the PA command. 

- 

Result: TEK 4051 SENDING DATA 

Commodore PET* 2001 and 8032 Example: 

10 OPEN 5,5 20 DIM A$C(13) 30 A$=" SENDING DATA" 40 Be2001 50 Y=2000 BO PRINT#S,"SP1;PA1000," ;STR$CY) 70 PRINT#5,"LBPET ";B;A$;CHR$(3) 80 END 

A terminator is sent by PET at the end of the PRINT #5 statement. Result: PET 2001 SENDING DATA 

## Apple* IT Applesoft BASIC Example: 

10 PR 3: IN& 3 20 Z2¢= "WTK" + CHR$ (26) 30 DIM A$¢12) 40 AS= " SENDING DATA! 50 Y= 2000 60 PRINT Z$; "SP1;PR1000,",¥ 7O PRINT 2$; “LBAPPLE II ";A$;CHR$ (3) 80 PR O: IN# OG 30) 6END 

*Commodore PET is a trademark of Commodore Business Machines, Inc. Apple is a trademark of Apple Computer, Inc. 

HP-IBINTERFACING 9-9 
