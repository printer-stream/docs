Rev.2.52 

## **ESC GS * 2 m c w** 

Specify mark color and mark horizontal width for each mark number 

|||
|---|---|
|Name<br>Specify mark color and mark horizontal width for each mark number<br>Code<br>ASCII<br>ESC<br>GS<br>*<br>2<br>m<br>c<br>w<br>Hex.<br>1B<br>1D<br>2A<br>32<br>m<br>c<br>w<br>Decimal<br>27<br>29<br>42<br>50<br>m<br>c<br>w<br>Defned Region<br>“0”≤m≤”9”<br>“0”≤c≤”1”<br>“001”≤w≤”999”<br>Initial Value<br>Non-volatile memory<br>Function<br>Specifes mark color and mark horizontal width for each mark number.<br>m specifes the mark number.<br>c specifes the mark color.<br>w specifes the mark horizontal width (number of dots).<br>If w exceeds the print region, this command is ignored.<br>m, c and w are ASCII character strings that are represented by decimals; They are<br>composed of character codes “0” to “9.”||
|c|Mark Color|
|n = “0”(48)|White|
|n = “1”(49)|Black|



Reference ESC GS * 0, ESC GS * 1, ESC GS * W, ESC GS * C 

ESC/POS Command Specifications 

203 
