of CP instructions is the pen position at the completion of the user defined character, one character-space field to the right of the origin of the user defined character. 

## "SP1:PA1000,9000;S1.25,.4" 

"C0,4,99,1.75,0,1.5,4,3,-8,3,8,3,-8,3,8,3,-8,1.5,4,1.75,0;" "CP3.25,0;LB1000 ahms&" 

## MW 1000 ohms 

User defined characters are drawn using the current character size, slant, and direction. It is also possible to change the size of a user defined character by changing each X- or Y-increment parameter by a constant multiple. Send the following commands to the plotter. The resistor drawn will be twice the size of the resistor drawn in the last example. 

“SP1;PA1000,4500;51.25,.4" "UCO,8,99,2.5,0,3,8,6,-16,6,16,6,-16,6,16,6,-16,3,8,3.5,0;" 

## Parameter Interaction in Labeling Commands 

There are three factors which interact and affect the direction and mirroring of labels; the label direction as specified by DI or DR commands or default direction, the sign of the parameters for the size commands SI or SR, and the relative positions of Pl and P2. These interactions are complex. This section considers the four possible combinations of DI, DR, SI, and SR and illustrates the effects of various parameters and settings of P1 and P2 on labels. 

The labels used in the illustrations are the commands which cause the direction, size, and mirroring of the label. AlJl descriptions are in terms of the standard X,Y coordinate system. An arrow is shown for each label; this arrow is the baseline along which labeling occurs and shows the left-to-right direction that is the standard direction of a label without mirroring. The same P1,P2 area, that area set by default Pl and P2, is always used. During the course of the illustrations, Pl and P2 are assigned to opposite corners of this rectangle in all possible ways. The values used for X-coordinates of Pl and P2 are 250 and 10 250; the values used for the Y-coordinates of P1 and P2 are 279 and 7479. 

LABELING 5-21 
