## Advanced Programming Tips ——— 

When drawing labels, you often wish to position them precisely in relation to a specific point. Unless positioned differently by the programmer, labels are written beginning at the current pen position which marks the baseline of the label. 

The following BASIC program illustrates various ways to center labels. The program uses the BASIC command LEN($) to find the length of the string. This length is used to determine horizontal adjustments, ie., how many character-space widths the pen must be moved in order to achieve the desired positioning. Vertical moves are in terms of characterspace heights. Since an uppercase letter is half the height of a character space, a vertical movement of one-quarter character space down will center uppercase letters on the point; notice the parameter is negative. A parameter of —0.5 will cause the top of uppercase letters to be level with the point. 

Symbol mode plotting, with an * as the symbol, has been used here to show pen position at the start of the label command. The character plot instruction which positions the label is shown above each label. 

10 DIM A$(401,B$l401,C$40] 20 Ag="THIS LABEL IS RIGHT JUSTIFIED" 30 PRINT "SP1;SM*;PA6000,5500; POPU; " 40 PRINT "CP"; -LENCA$);"O;LB"; A$; "4%" a) B$="THIS LABEL IS CENTERED BELOW THE POINT" 60 PRINT "PA4500, 5000; PDPU;" 70 PRINT "CP"; -LEN(B$)/2;"-.5;LB"; 80 C$="VERTICALLY CENTERED LABEL" BS; "&" 30 PRINT "PA2Z?750,4500; PDPU;" 100 PRINT "CPO,-.25;LB";C#5 "5" 110 END 

## "CP"; -LENCAS$) ;"G;" THIS LABEL IS RIGHT JUSTIFIED, 

"CP" 5 -LEN(B$)/2;"-.55" THIS LABEL IS CENTERED BELOW THE POINT "CPO,-.25;" WERTICALLY CENTERED LABEL 

5-26 LABELING 
