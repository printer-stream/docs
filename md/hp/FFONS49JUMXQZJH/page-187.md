## HP-75 BASIC Example: 

10 ASSIGN IO ":PL" 20 PRINTER IS ": PL" 30 AS="SENDING DATA" 40 Be?5 50 Y=2000 GO PRINT "SP1;PA1000,",¥ 70 PRINT "LBHP" ;B;A$;CHRE(3) BO PRINT "SPQ;" 90 END 

Result: HP 75 SENDING DATA 

HP Series 80 BASIC Example: 

16 PRINTER IS 901 20 A$="SENDING DATA" 30 B=80 40 Y=2000 SO PRINT "SP1;PA1000,",¥ 60 PRINT “LBHP"; B;A$; CHR (3) 70 PRINT "SPQ;" 80 END 

Result: HP 80 SENDING DATA 

## Plotter-to-Computer 

Transmitting data from the plotter to the computer is typically accomplished using I/O statements such as READ, INPUT, and ENTER. Sometimes these statements are only available in I/O ROMs; check your computer’s documentation or ask your HP dealer or HP Sales and Support Office. The following examples of obtaining output data from the plotter using various computers are only intended to illustrate the necessity for understanding the I/O statement protocol implemented on your computer. Each of these examples commands the pen to move to plotter coordinates 1000,1000 and then output the current pen position and the plotter identifier string to the computer. 

HP-ILINTERFACING 11-5 
