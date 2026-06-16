SP pen number (;)

Purpose:

Selects or stores a pen.

integers. Omitting parameters or a parameter of 0 stores the pen. Odd-numbered parameter selects pen from left stall, even-numbered from right.

Parameter:

## SR The Relative Character SizeInstruction

SR width, height; ;

'

Purpose:

Sets the character width and height relative to P1 and P2 for labels.

Parameters:

decimals representing a percentage of vertical or hori­ zontal distance between Pl and P2.

Width -percentage of (P2X- Plx).

Height -percentage of (P2y -Ply).

Omitting parameters results in value 0.75for width and 1.5for height.

## The Select Standard Character Set Page 5-4

## SS Instruction

SS (;)

Purpose:

Selects the standard character set designated by the CS instruction as the character set used for subsequent labeling.

## TL The Tick Length Instruction Page4-2

TL tp(,tn)(;)

Purpose:

Establishes the length of ticks drawn with the instruc­ tions XT and YT.

Parameters:

decimals.

tp -percentage of (P2y - Ply) for XT or (P2X- Plx) for YT. Denotes portion above the X-axis or to the right of the Y-axis when difference is positive.

tn -same as tp except denotes portion below the X-axis and to the left of the Y-axis.

Omitting parameters causes tick lengths tp and tn 0.5% of (P2y-Ply) or (P2x-Plx), the same as the default values.

Page

## 5-16
