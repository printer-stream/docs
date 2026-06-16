## C O N F I D E N T I A L

## TM-P60

## [Peeler model]

If the current label feed to the print starting position operation fulfills any of the following conditions, Bit 0 of [Position information B] becomes "Feed current label to the print starting position is possible."

1. When Position information A is "standby in peeling position" (immediately after executing &lt;Function 65&gt; of this command)
2. When Position information A is "standby in cutting position" (immediately after executing &lt;Function 66&gt; of this command)

At the next operation to feed labels to the print starting position, Bit 1 of [Position information B] becomes "Feed next label to the print starting position is possible" irrespective of the current position.
