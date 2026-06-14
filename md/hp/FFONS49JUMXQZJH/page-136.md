## HP 9835/9845 Example: 

10 PRINTER IS ?,5 20 Ag=" SENDING DATA" 30 B=9835 40 C=9845 30 Y=Z000 50 PRINT "SP1,;PRi000,";7 70 PRINT USING "K";"LBHP ',B,"/“",C,A%, CHRS$(3) 10) END 

A terminator is sent by the computer at the end of a PRINT statement. Result: HP 9835/9845 SENDING DATA 

## HP 2647 Example: 

~ 

10 ASSIGN "H#5" TO #1 20 DIM AS$(13] 30 R$="SENDING DRTA" 40 B=264?7 50 Y=Z000 60 PRINT #1;"SP1;PA1000,",¥ 70 PRINT #1;"LBHP",B,A$, CHRS$C3) 80 END 

A terminator is sent by the 2647 at the end of PRINT #1 statements. Result: HP 2647 SENDING DATA 

## HP-83/85 Example: 

10 PRINTER IS 705 20 A¢="SENDING DATA" 30 Bs85 40 Y=Z2000 50 PRINT "SP1;PA1000,",Y 6 PRINT “LBHP";B;A$;" ri" 70 END 

A terminator is sent by the computer following PRINT statements. Result: HP 85 SENDING DATA 

9-8 HP-IB INTERFACING 
