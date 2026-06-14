## Result: APPLE II SENDING DATA 

The PR# 3: IN# 3 statement must be included in each program before instructions can be sent to the plotter. These statements assume the IEEE-488 interface card (HP-IB) is in slot three of the computer. The string Z$ addresses the plotter at address 5 to listen. It must be included in every print statement which sends HP-GL commands to the plotter. The PR# 0: IN# 0 statement directs keyboard output to the display and must be included before the end of the program or before anything can be printed on the display. 

## Plotter-to-Computer 

Typically, the computer obtains output information from the plotter by using I/O statements such as READ, INPUT, or ENTER. Sometimes these statements are available only in I/O ROMs, such as in the HP Series 80 computers. Check your computer documentation or ask your HP salesperson to determine if your system requires a special I/O ROM. The following examples of obtaining output data from the plotter using various computers are only intended to illustrate the necessity for understanding the I/O statement protocol implemented on your computer. Each of these examples commands the pen to move to plotter coordinates X = 1000, Y = 1000 and then output the current pen position and the plotter identifier string to the computer. 

## HAP 9825 and 9826 HPL Example: 

O: fxd Oj;dim A$ (5) 1: wrt 705," PA1000, 1000;0C" 2: red 705,A,B,C 3: wrt 705,"01" 4: red 705,A$ 3: dsp A,B,C,AS 6: end 

Displayed current pen position and identification. 1000 1000 0 7470A 

## HP 9826 BASIC Example: 

10 PRINTER IS 705 20 PRINT “FAIO0O0, 1000;0Cc" 30 ENTER 7053A,B,C 40 PRINT "QI" 50 ENTER 70O5;A$ 60 DISP A,B,C,A$ 70 END Displayed current pen position and identification. 

1000 1000 0 TA70A 

9-10 HP-IB INTERFACING 
