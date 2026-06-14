| 

| USES | Symbol mode plotting can be used to draw a specified character at each data point and thus to create scattergrams, geometric drawings, or multiple-line graphs where lines are easy to differentiate. 

## SM c (terminator) or SM_ (terminator) 

An SM command without parameters turns off symbol mode. When a parameter is present, it is limited to a single character, which must be one of the printing characters of the character set currently selected. 

After an SM command has been executed, subsequent PA and PR commands function as described in the previous chapter, except that the specified symbol mode character is drawn at the end of each vector and is centered on the plotted point. (A character drawn at a point using the label command, LB, would not be centered on the point.) Drawing of the character is independent of the current pen state (up or down); the character is always drawn at each point specified in the PA and PR command. 

The character is drawn according to the character set selected when the SM command is executed. The character does not change even if a new set is selected. An SM command remains in effect until another valid SM command is executed or an IN or DF command is executed. The size (SI and SR), slant (SL), and direction (DI and DR) commands affect the character drawn. 

An SM command can specify any printing character (decimal values 33 through 127). The semicolon (decimal value 59) is used only to cancel symbol mode (SM;) and cannot be selected as the symbol to be drawn at the endpoint of each vector. Specifying a space (decimal value 32) or any control character also cancels symbol mode. 

The following example shows symbol mode plotting with the pen up and the pen down as might be used in line graphs, geometric drawings, and scattergrams. 

"IM; SP1;S5M¥;PRZ00,1000;" "PD400,12390,600, "PU; SM; PA1O0, 300;1560,5M3;" 900, 1670, 1500, 1600, 2000, 20003" "PAZ00,500,500, "SM; PA1900,560;PD;450,900,850,SMY; PAS300, 1350,1250;"1300, 2100, 1350PU;" "SMZ;PAS5950; SM; PA1900, 56 **0** ; PU;0,SPO;" 

ENHANCING THE PLOT 4-5 
