## AdvancedProgramming Tips

When drawing labels, you often wish to position them precisely in rela­ tion to a specific point. Unless positioned differently by the programmer, labels are written beginning at the current pen position which marks the baseline of the label.

The following BASIC program illustrates various ways to center labels. The program uses the BASIC command LEN($) to find the length of the string. This length is used to determine horizontal adjustments, ie, how many character-spacewidths the pen must be moved in order to achieve the desired positioning. Vertical moves are in terms of character­ space heights. Since an uppercase letter is half the height of a character space, a vertical movement of one-quarter character space down will center uppercase letters on the point; notice the parameter is negative. A parameter of -0.5 will cause the top of uppercase letters to be level with the point.

Symbol mode plotting, with an * as the symbol, has been used here to show pen position at the start of the label command. The character plot instruction which positions the label is shown above each label.

```
10 DIMH$[40],B$[40],C$[40] 20 H$='THIS LHBEL IS RIGHT JUSTIFIED' 30 PRINT 'SP1;SM*;PHS00O,5500;PDPU;' 40 PRINT 'CF';-LEN(H$J;'O;LB';H$;'5' so B$='THIS LHBEL IS CENTERED DELDN THE POINT' 50 PRINT "PR45oo,5ooo;PDPu;" 70 PRINT'CF';-LEN(B$)/2;'-.S;LB';B$;'E' so C$='VERTICHLLY CENTERED LHBELU 90 PRINT 'PH2?50,4500;PDPU;' 100 PRINT 'CPO,-.25;LB';C$;'E' 110 END 'CF';-LEN(H$);'O;' THIS LABEL IS RIGHT JUSTIFIEDR 'CF';-LEN(B$J/2;'-.5;' THIS LABEL IS CENTERED BELOW THE POINT 'CPO,-.2S;' VERTICALLY CENTERED LABEL =
```
