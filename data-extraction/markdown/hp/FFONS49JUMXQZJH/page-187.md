## HP-75 BASIC Example:

```
10 20 30 40 50 80 70 BO 30 RssIcN ID ':PL' PRINTER IS ':PL' H$='SENDING URTR" B=?5 Y=2000 PRINT 'SP1;PH1000,',Y PRINT 'LBHP';B;H$;CHR$(3) PRINT 'SPO;' END
```

Result:

HP 75 SENDING DATA

## HP Series 80 BASIC Example:

```
10 20 30 40 50 E0 ?0 80 PRINTER IS 901 H$='SENDING DHTH' B=B0 Y=2000 PRINT '5P1;PH1000,',Y PRINT 'LBHP';B;H$;CHR$(3) PRINT 'SPO;' END
```

## Result:

HP 80 SENDING DATA

## Plotter-to-Computer

Transmitting data from the plotter to the computer is typically accom­ plished using I/O statements such as READ, INPUT, and ENTER. Sometimes these statements are only available in I/O ROMS;check your computer's documentation or ask your HP dealer or HP Sales and Support Office.The following examples of obtaining output data from the plotter using various computers are only intended to illustrate the necessity for understanding the I/O statement protocol implemented on your computer. Each of these examples commands the pen to move to plotter coordinates 1000,1000and then output the current pen position and the plotter identifier string to the computer.
