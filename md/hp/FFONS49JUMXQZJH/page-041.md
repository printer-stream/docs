| 

## Chapter 3 Controllinge the Pen and Plottinge 

## What You’ll9 Learn ine Thise Chapter 

Now that you understand the unit systems in which data can be represented, you are ready to create plots. In this chapter, you will learn how to select either of the two pens or change pens, how to set and change pen velocity, how to raise and lower the pen, and how to plot. You will learn how to plot to absolute X,Y coordinates or to plot relative to the last pen position. Finally, you will learn how to send variables as parameters of plot commands; this will enable you to write general purpose graphics programs. 

## HP-GL Instructions Covered 

- SP The Select Pen Instruction CI* The Circle Instruction Vs The Velocity Select Instruction AA* The Arc Absolute PU/PD The Pen Up/Down Instructions Instruction PA The Plot Absolute Instruction AR* The Arc Relative PR The Plot Relative Instruction Instruction 

## Terms You Should Understand 

Absolute Plotting — plotting to a point whose location is specified relative to the origin (0,0). When the PA command is used to plot to a point, the pen always moves to the same point on the plotting surface, no matter where the pen was before the move. 

Relative Plotting — plotting to a point whose location is specified relative to the current pen position. The point moved to then becomes the effective origin for the next parameter of a plot relative command. When the PR command is used to plot to a point, the destination of the pen depends on where the pen was when the command was received. Plotter Unit Equivalent — the X,Y coordinates of a point, given in user units, if they were expressed in plotter units. 

*Available only with Option 001 plotters that have the serial prefix number 2308A or higher. 

CONTROLLING THE PEN AND PLOTTING 3-1 
