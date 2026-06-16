<!-- image -->

Negative SI parameters will produce mirror images of labels. A nega­ tive SI width parameter will mirror labels in the right-to-left direction.

RESULTING LABEL

<!-- formula-not-decoded -->

A negative height parameter will mirror labels in the top-to-bottom direction. .

<!-- formula-not-decoded -->

RESULTING LABEL

F+tj

Twonegative SI parameters will mirror the label in both directions and the label will appear to be rotated 180degrees.

<!-- formula-not-decoded -->

RESULTING LABEL

CJP4

For further information on the effects of negative parameters, refer to the section Parameter Interaction in Labeling Commands later in this chapter.

In order to produce legible characters, parameters should be greater than 0.1. Parameter values above 18 allow a maximum of one character to be drawn on the paper.

## The Relative Character Size Instruction, SR

DESCRIP-'UN The relative character size instruction, SR, specifies the size of characters and symbols as a percentage of the distance between scaling points P1 and P2.

USE3 The instruction can be used to define character size relative to the distance between P1 and P2 so that if the P1,P2 distance changes, character size will adjust to occupy the same 'relative' amount of space.

<!-- image -->

SYNTAX SR

width, height terminator

or

SR terminator
