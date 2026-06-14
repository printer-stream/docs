If parameters are included, two parameters are re quired, width and height. The defined width and height are interpreted as a percentage of the algebraic distance between the X- or Y-coordinates of PI and P2. The parameters are in decimal format and may have any value between —128 and 127.9999. An SR command with no parameters will default to the values 0.75 for width and 1.5 for height, which, when P1 and P2 are at default values, produces letters the same size as an SI command without parameters. 

An SR command remains in effect until another valid SI or SR command is executed or the plotter is initialized or set to default conditions. An SR command which sets an error condition is ignored and the character size does not change. 

The following example shows how changes.in P1 and P2 affect labels - drawn while an SR command is in effect. The upper label is written with default character size. Then P1 and P2 are changed to define a square area with 6000-plotter-unit sides. A new label is drawn. Next a new SR command is executed with both width and height parameters set to three percent. Because the area established by P1 and P2 is square, equal parameters create square letters. With default P1 and P2 settings, equal parameters do not create square letters. 

“IN; SP1;PA100, 7000;LBDEFRULT Si ZE&" "IP 1000, 1000, 7000, P7OO0O;FAION, B50c3" “LBNEW P1 AND PZ CHANGE LABEL SIZE% SR3,335" " PAI 00,6000;_BNEW SR COMMANDS '*CHANGES LABEL SIZE%! 

## DEFAULT SIZE 

## NEW P1 AND P2 CHANGE LABEL SIZE 

## NEW SR COMMAND CHANGES LABEL SIZE Hither negative SR parameters or switching the relative positions of P1 and P2 will produce mirror images of labels. Refer to The Absolute Size Instruction, SI, and Parameter Interaction in Labeling Commands for more information on mirroring. 

With default P1 and P2, the useful range of width and height parameters which produces legible characters and a label of suitable length is 0.6 to 5. 

LABELING 5-17 
