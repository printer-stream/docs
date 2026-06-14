## Sending and Receiving Data 

## Computer-to-Plotter 

Transmitting data from a computer to the plotter is typically accomplished using 1/O statements such as WRITE, PRINT, PRINT#, or OUTPUT. The following examples of sending program data to the plotter from various computers are only intended to illustrate the necessity for understanding the I/O statement protocol implemented by your computer. Each of these examples will cause the plotter to label the identity of the computer sending data, beginning at the X,Y coordinates 1000, 2000. The examples involve sending both character string and numeric data as variables, and constants or literals. 

## AP 9825 and 9826 HPL Example: 

QO: fxd O;dim A¢(13] 1: " SENDING DATA" -RA$ 2: Z0003¥ 3: 9826-8 4: wet 705,"5F1;PA1000,",7 S: wtb 705,"LBHP",str(B),AS, 3 6: end 

A terminator is sent by the 9825/9826 at the end of a wrt statement. 

## Result: HP 9826 SENDING DATA 

## 9826 BASIC Example: 

10 PRINTER IS 70S 20 A$="" SENDING DATR" 30 B=9826 40 Y=Z000 50 PRINT "SP1;PA1000,",% 60 PRINT USING "K";"LBHP ",B,AS,"& rae) END «! 

A terminator is sent by the 9826 at the end of a PRINT statement. 

Result: HP 9826 SENDING DATA 

HP-IB INTERFACING 9-7 
