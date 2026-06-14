## Sending and Receiving Data 

## Computer-to-Plotter 

Transmitting data from a computer to the plotter is typically accomplished using I/O statements such as PRINT, PRINT#, or OUTPUT. The following examples of sending program data to the plotter from various computers are only intended to illustrate the necessity for understanding the I/O statement protocol implemented by your computer. Each of these examples will cause the plotter to label the identity of the computer sending data, beginning at the X,Y coordinates 1000,2000. The examples involve sending both character string and numeric data as variables, and constants or literals. 

## HP-41 RPN Example: 

NOTE: The characters that are enclosed in quotation marks must be entered in the alpha mode (the quotation marks do not need to be entered). The “} ” symbol is the “alpha append” symbol; it is produced by pressing the shift and K keys while in the alpha mode. @ 

O1@LBL "CTP" O02 AUTOIO O03 FIX 6 o4 CF 29 0S 2000 o6 "SP1 PA1O0OO," oO? ARCL xX 0g OUTA og 41 10 "LBHP " 11 ARCL xX 12 "hb SENDING DATA" 13 0 14 ENTERT 15 3 16 BLOSPEC 17 ARCL x 18 QUTA 19 "SPO" 20 QUTA 21 END Result: HP 41 SENDING DATA 

11-4 HP-IL INTERFACING 
