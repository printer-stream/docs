## HP 9835/9845 Example:

- 10 PRINTER 15 7,5
- 30 ENTER?05;H,B,C
- 20 PRINT 'PH1000,1000;DC'
- 40 PRINT 'DI'
- 50 ENTER ?O5;H$
- 50 DISP H,B,C,H$
- ?O END

Displayed current pen position and identification.

1000

1000

0

7470A

## HP 2647Example:

- '10 HSSIGN 'H35' TD :1
- 20 PRINT u1;~PR1ooo,1ooo;Dc"
- 40 PRINT a1;"DI"
- 30 REPDa1;P,B,c
- 50 REPD u1;Ps
- B0 PRINT H,B,C,H$
- 70 END

Displayed current pen position and identification.

1000

1000

0

7470A

## HP-85/ 86/ 87Example:*

- 10 PRINTER I 5 'P05
- 20 PRINT "PR1ooD,1ooo;Dc"
- 40 PRINT 'UI;'
- 30 ENTER ?O5 ; P,B,c
- SE': ENTER 705 ; Rs
- 50 DISP H,B,C,H$
- 'R0 END

Displayed current pen position and identification.

1000

0

1000

7470A

*Requires I/O ROM HP Part Number 00087-15003.
