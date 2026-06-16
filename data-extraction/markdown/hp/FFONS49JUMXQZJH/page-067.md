<!-- image -->

M Symbolmode plotting can be used to draw a specifiedchar­ acter at each data point and thus to create scattergrams, geometric drawings, or multiple-line graphs where lines are easy to differentiate.

## SYNTAX SM

c (terminator)

or

SM

(terminator)

EXPLANATIONAn SM command without parameters turns off symbol mode. When a parameter is present, it is limited to a single character, which must be one of the printing characters of the character set cur? rently selected.

After an SM command has been executed, subsequent PA and PR commands function as described in the previous chapter, except that the specified symbol mode character is drawn at the end of each vector and is centered on the plotted point. (A character drawn at a point using the label command, LB, would not be centered on the point.) Drawing ofthe character is independent of the current pen state (up or down);the character is always drawn at each point specified in the PA and PR command.

The character is drawn according to the character set selectedwhen the SMcommand is executed. The character does not change even if a new set is selected. An SM command remains in effect until another valid SM command is executed or an IN or DF command is executed. The size (SI and SR), slant (SL), and direction (DI and DR) commands affect the character drawn.

An SM command can specify any printing character (decimal values 33 through 127).The semicolon (decimal value 59)is used only to cancel symbol mode (SM;)and cannot be selected as the symbol to be drawn at the endpoint of each vector. Specifying a space (decimal value 32)or any control character also cancels symbol mode.

The following example shows symbol mode plotting with the pen up and the pen down as might be used in line graphs, geometric drawings, and scattergrams.

```
'IN;SP1;SM%;PH2UO,1000;' 'PU4DO,1230,BOO,1SBD,SO0,1E?U,15OD,1S0O,2000,2000;' 'PU;SM;PH100,300;SM3;' ' 'ESESE;Egg,2g8,:g0,fi0O$:§0613?Eé13PO,21O0,13SOPU;' '; ,.' ; ;S*Y; 33 O 'LqO;'
```

'SMZ;PH3500,350;SMH;PH1SO0,5éO;PU;SPO;'
