## HP 9835/9845 Example:

```
10 20 30 40 50 E0 ?0 80 PRINTER IS ?,5 H$=' SENDING DHTH' B=9835 C=S845 Y=2000 PRINT 'SP1;PH1000,';Y PRINT USING'K';'LBHP ',B,'f',C,H$,CHR$(3) END
```

Aterminator is sent by the computer at the end of a PRINT statement.

Rwflt

HP 9885/9845 SENDING DATA

## HP 2647 Example:

- 10 HSSIGN 'H35' TD #1

```
20 DIM H$[13] 30 H$='SENDING DHTH' 40 B=2B4? 50 Y=ZOOO 50 PRINT #1;"SP1,'PF%1000,",Y ?o PRINT #1;"l_EIHP",E,F1$,CHF2$(3Il 80 END
```

Aterminator is sent by the 2647at the end of PRINT #1 statements.

Result:

HP 2847 SENDING DATA

## HP-83/ 85 Example:

- 10 PRINTER IS T05

```
E0 30 40 '5 (:1 60 70 F1$=" SENUI NG DFITH" B=B5 Y=2000 PRINT 'SP1;RH1000,',Y PRINT " LBHP" ,' B; H$; " F-as " END
```

Aterminator is sent by the computer following PRINT statements.

Result:

HP 85 SENDING DATA

'
