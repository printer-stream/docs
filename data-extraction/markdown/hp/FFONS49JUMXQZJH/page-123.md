## L1st1ng

A complete listing of the program follows. This listing contains all the BASIC statements necessary to have this program run on an HP-85 computer with an HP-IB interface and the plotter set to address 5. When the plotter is used with an RS-232-C interface, line 10 should be replaced by other lines which send the escape code sequences necessary to turn on the plotter and establish handshaking. In some PRINT state­ ments, semicolons or commas are used to ensure that HP-GL com­ mands will have the necessary separators or no extra spaces. Youmay need to make changes for your computer's BASIC, or you can use some other programming language and send the strings of HP-GL com­ mands using your 1anguage'soutput statements and looping techniques.

NOTE: The end-of-text character 'xis equivalent to N on the HP-85's* display and internal printer. (N is obtained on the HP-85 by pressing CTRL and C simultaneously. On many computers, you can also use the CHR$(3)function to generate the end-of-text character.) This program listing was produced on an HP 7310printer. I

```
10 PRINTER I5 705,30 20 PRINT'IN;SP1;IP1250,75D,9250,E250;' 30 PRINT'5c1,12,o,15o;' 40 PRINT'PU1,0 PD 12,o,1E,15o,1,15o,1,0 PU' 50 PRINT'SI.Z,.3;TL1.5,0' 50 FOR x=1 TU 12 ?o PRINT 'PR';X,',O; XT;' so REHD Rs 90 PRINT'CF-.33,-1;LB';H$;'fi' 100 NEXT x 110 PRINT "PR5.5,o;cP-?,-:.5; LBCHLENDHR MDNTHE' 120 FOR Y=0 T0 150 5TEP 25 130 PRINT 'PH 1,',Y,'YT;' 140 IF Y<1OOTHENPRINT 'EP-3,-.25;LB';v;'a" 150 IF Y>9S THENPRINT 'CP-4,-.25; LB';Y;'§' 150 NEXT Y 170 PRINT 'PH1,15O CP-3.5,E LBSHLES$5CP-9,-1' 180 PRINT 'LB(THDUSRNUS] UNITED STHTES E' 130 PRINT 'LBEURUPE JHPHN SDUTH HMERICR§" 200 PRINT 'SPO;' 210 UISP 'CHRNGE TU WIDE PENS' 220 PHUSE Z30 DISP ' ' 240 PRINT'SP1 PHE,150 5I.4,.B CP-S.5,2.0' 250 PRINT 'LB1981 SRLES BY REGIUNR' 250 PRINT 'SP1;LT3,G;PR1 EEPDZ 25 3 13 4 22 5 23' 270 PRINT 'PBS 2? 7 2? 8 9 24 10 23 11 2? 12 27Pu~ 280 PRINT 'PH?.B,1B5 PD5.3,1a5 PU' 250 PRINT'5P2;LT5,a;PR1,45;PU;PR2,5o,3,52,4,53,5,52~ 300 PRINT"PD5,51,?,55,s,5E 9,5E,1o,5s,11,55,12,5oPu~ 310 PRINT 'PR10.1,185 PU11. ,1B5 PU'
```

(Program listing continued)
