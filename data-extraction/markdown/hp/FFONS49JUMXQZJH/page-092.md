## Use of DI and SI

When DI and SI commands are used together,'the DI command estab­ lishes the label's direction and the SI command establishes its size. The direction serves as the axis along and about which labels (written with negative SI parameters) are mirrored. Positions of P1 and P2 do not affect the labels. Refer to The Absolute Direction Instruction, DI, and The Absolute Size Instruction, SI.

Two examples of mirrored labels are shown below.In the first example, the DI parameters 3,2 place the directional line in the first quadrant. The negative width parameter of the SI command mirrors the label in the right-to-left direction. In the second example, the DI parameters 3,-2 place the directional line in the fourth quadrant. The negative height parameter of the SI instruction mirrors the label top-to-bottom.

<!-- image -->

## Use of DR and SI

When DR and SI commands are used together, the label size is deter­ mined by the SI command and does not change with changes in the settings of P1 and P2. However, changes in the settings of P1 and P2 will affect the label direction. The algebraic differences (P2x' Plx) and (P2y-Ply) are multiplied by the run and rise parameters of the DR command. The resulting parameters, when applied to the standard coordinate system, determine the label baseline. Mirroring about this baseline is determined by the signs of the SI parameters.

In illustration 3, P1 and P2 are at their default settings so the algebraic differences (P2,; -Plx) and (P2y -Ply) are both positive. The DR parameters 3,-2 are used as is and establish the directional line in the fourth quadrant. The negative SI height parameter mirrors the label from top to bottom.
