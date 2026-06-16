<!-- image -->

## Hatching a Bar

The following program segment, together with lines 10 to 100 and 400 of this chapter's program, hatches a bar which represents February data for line 2, i.e., 2,50. The XTinstruction was deleted from line 70to omit drawing the X-ticks. Again the bar is centered over the X data point. In this segment, the increment variable P is the distance between hatching lines and determines whether a wide or narrow hatch pattern is drawn. Youmay want to make further refinements depending on pen width and bar width and height. The bars are shown here actual size with P set at 100and 300. The locations of the variables are shown on the first bar and should help you understand the program listing.

For plots on transparency film or to make hatch lines more uniform, you should slow the pen Velocityusing the VS instruction.

The routine performs the following tasks.

1. and 2. (Same as solid fill algorithm.)
3. Using the output obtained in step 1, sets the window to be the bar we wish to hatch.
4. Beginning the width of the bar below the Yminvalue, plots a line at a 45 degree angle to the opposite side of the bar, increments the Y-Valueand continues the process until the top of the bar is reached.
5. Resets the scaling and window to their previous values.
