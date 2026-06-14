plot command in the second line. Inserting carriage return and line feed characters directly into the label string in the third line causes the same effect as the CP; command in the last line. If the carriage return and line feed characters are available on your keyboard, you may prefer that method. 

"DF ;SP1;PA14 Ooo, 1 OOOPDUPRI On , OPU; PR-3000 205" "CPS,. 35;LBABOVE THE LINES FAZOOO, 1 OO0;" "ST; CPO,-,.95 ;LBBELOW THE LINES AND WITH A NEAT&"! "CP;LBMARGIN&" 

. ; 

**==> picture [250 x 83] intentionally omitted <==**

**----- Start of picture text -----**<br>
5 CHARACTER<br>SPACE<br>WIDTHS<br>——— ABOVE THE LINE<br>anDes<br>/ [BELOW THE LINE<br>1000 ie AND WITH A NEAT<br>,1000 2000, 10 MARGIN<br>**----- End of picture text -----**<br>


## The Absolute Character Size Instruction, SI 

DESCRIPTION Mitswees absolute character size instruction, SI, specifies the size of characters and symbols in centimetres. 

USES Hiiwars instruction can be used to change the character size from its default value or to another value and establish absolute character sizing in centimetres so character size is not dependent on the settings of P1 and P2. SYNTAX MRS width, height terminator or SI terminator 

EXPLANATION MiMi: parameters are included, two parameters are re quired, width and height. The defined width and height are interpreted as centimetres, must be in decimal format, and may have any value between —128 and 127.9999. An SI command with no parameters will default to the values 0.19 for width and 0.27 for height. 

An SI command remains in effect until another valid SI or SR command is executed or the plotter is initialized or set to default conditions. An SI command which sets an error condition is ignored and the character size does not change. The following example letters the plotter’s model number, 7470A, at the specified width of 1 cm and height of 1.5 cm. 
