## SYNTAX

TL

tp

(,tn)

(terminator)

or

TL (terminator)

EXPLANATIONBoth parameters must be between -128 and +127.9999. Use of positive parameters is recommended. For most applications, parameters will be between 0 and 100.

The up and right tick length, tp, determines the length of the upward portion of the tick marks drawn along the X-axis and the right-side portion of the tick marks drawn along the Y-axis, taking P1 as the. lower-leftcorner.

The down and left tick length, tn, determines the length of the down­ ward portion of the tick marks drawn along the X-axis and the left-side portion of the tick marks drawn along the Y-axis, taking P1 as the lower-left corner.

The values specified by parameters tp and tn are a percentage of the vertical scale length (P2y-Ply) when used with the XT instruction, and a percentage of the horizontal scale length (P2,;- Plx) when used with the YT instruction. Note the actual tick length is a function of the scaling established by P1 and P2, and the length of ticks on the X-and Y-axes will be different even if the same tick length percentage value is specified for both XT and YT, unless the area defined by P1 and P2 is square.

The plotter, when initialized, automatically sets the tick length values to 0.5% of the scaling lengths (P2y\_ Ply) and (P2x-Plx). A TL command with no parameters will default to the same values. A TL command with only one parameter specifies the length of tp, and tn will be zero. A negative tp parameter will draw a negative tick just as would be drawn by a tn with a positive parameter. Likewise, a negative tn parameter will draw a positive tick. Use of negative parameters is not recommended both because the results are more difficult to visualize and programs with negative parameters will not be compatible with other HP plotters. A TL command remains in effect until another TL command with valid parameters is executed or an IN or DF instruction is executed.

The following example draws both tick marks and grid lines. The grid lines are a result of specifying 100%tick length. The horizontal tick marks on the left-most grid line are drawn using the default tp,tn. The tick marks on the second grid line have a positive tick length of 1%and no negative tick. The tick marks on the third grid line have no positive tick and a negative tick length of 5%.Note that these last tick marks are drawn by the YT instruction even though the PU instruction is in effect. However, the moves to the next tick location are made with the pen up, and hence, the grid line is not retraced. A reduced version of the plot follows.
