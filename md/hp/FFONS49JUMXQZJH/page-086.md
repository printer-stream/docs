## "S11,1.85;LB"470A%" ) A / [ A 

Negative SI parameters will produce mirror images of labels. A negative SI width parameter will mirror labels in the right-to-left direction. 

COMMAND RESULTING LABEL "SI-.35,.6;LBHP &" QH A negative height parameter will mirror labels in the top-to-bottom direction. 

COMMAND RESULTING LABEL "S1.35,-.6;LBHP®! Hb 

Two negative SI parameters will mirror the label in both directions and the label will appear to be rotated 180 degrees. COMMAND RESULTING LABEL "ST-.35,-.6;LBHPS" dH 

For further information on the effects of negative parameters, refer to the section Parameter Interaction in Labeling Commands later in this chapter. 

In order to produce legible characters, parameters should be greater than 0.1. Parameter values above 18 allow a maximum of one character to be drawn on the paper. 

## The Relative Character Size Instruction, SR 

SHEL =6The relative character size instruction, SR, specifies the size of characters and symbols as a percentage of the distance between scaling points Pl and P2. 

WISH The instruction can be used to define character size relative to the distance between P1 and P2 so that if the P1,P2 distance changes, character size will adjust to occupy the same “relative” amount of space. 

SAILS SR width, height terminator or SR terminator 

5-16 LABELING 
