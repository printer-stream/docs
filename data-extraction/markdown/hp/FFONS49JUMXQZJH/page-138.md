## Result:

The PR# 3: IN# 3 statement must be included in each program before instructions can be sent to the plotter. These statements assume the IEEE-488 interface card (HP-IB) is in slot three of the computer. The string Z$ addresses the plotter at address 5 to listen. It must be included in every print statement which sends HP-GLcommands to the plotter. The PR# 0: IN# 0 statement directs keyboard output to the dis­ play and must be included before the end of the program or before any­ thing can be printed on the display.

## Plotter-to-Computer

Typically, the computer obtains output information from the plotter by using I/O statements such as READ, INPUT, or ENTER. Sometimes these statements are available only in I/O ROMS,such as in the HP Series 80 computers. Check your computer documentation or ask your HP salesperson to determine if your system requires a special I/O ROM.The following examples of obtaining output data from the plotter using various computers are only intended to illustrate the necessity for understanding the I/O statement protocol implemented on your com­ puter. Each of these examples commands the pen to move to plotter coordinates X= 1000,Y = 1000and then output the current pen position and the plotter identifier string to the computer.

## HP 9825and 9826HPL Example:

```
fxd 0;dim H$[5J wrt ?O5,'PR1000,1000;UC' red ?05,H,B,C wrt ?05,'UI' red ?05,H$ dsp H,B,C,H$ end U'J(J'l-bl'.aJl\J4C)
```

Displayed current pen position and identification.

1000 1000 0 7470A

## HP 9826 BASIC Example:

- 10 PRINTER IS 705
- 20 PRINT 'PH1000,1000;UC'
- 30 ENTER?O5;H,B,C
- 40 PRINT "01" so ENTER ?OS;H$ so DISP H,B,C,H$ ?O END

Displayed current pen position and identification.

```
1000 1000 0 7470A
```

## 9-10 HP-IB INTERFACING
