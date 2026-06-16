## C O N F I D E N T I A L

- X end position: [( x2L + x2H × 256) × horizontal and vertical motion units]
- Y end position:  [( y2L + y2H × 256) × horizontal and vertical motion units]
- ■ m1 sets the type of line. The line width differs according to the model (refer to the model information).
- ■ This function can be used when page mode is selected. Select page mode with ESC L .
- ■ You cannot specify a start coordinate [X start position, Y start position] and end coordinate [X end position, Y end position] that exceed the printing area set with ESC W .
- ■ You cannot specify [X start position ≥ X end position] or [Y start position ≥ Y end position].
- ■ X and Y and the horizontal and vertical motion units used for the start position specified with ESC T are changed as shown in the table below.

|   m1 | Line type                         |
|------|-----------------------------------|
|    1 | Continuous line: Thin             |
|    2 | Continuous line: Moderately thick |
|    3 | Continuous line: Thick            |

## [Notes]
