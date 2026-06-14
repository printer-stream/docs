Page 3-4 

## PA The Plot Absolute Instruction 

- PA Xj coordinate, Y; coordinate (X2 coordinate, Y2 coordinate, s+, Xn coordinate, Yn coordinate) (;) 

   - or 

- PA (3) Purpose: Plots to the X,Y coordinates in the order listed using the current pen up/down status. PA; sets absolute plotting. 

- Parameters: Pairs of integers representing plotter units if scaling not in effect, otherwise user units, integers or decimals. 

## PD The Pen Down Instruction 

   - Page 3-2 

- PD (;) or 

- PD Xj, coordinate, Y; coordinate (,...Xn, Yn coordinates) (;) Purpose: Programmatically lowers the pen. Parameters may be included as in PA or PR. 

## PR The Plot Relative Instruction 

Page 3-8 

- PR Xj increment, Y; increment (, X2 increment, Y2 increment, ...,.++ Xn increment, Yn increment) (;) 

- or 

| 

- PR (;) Purpose: Plots, in order, to the points indicated by the X,Y increments, relative to the previous pen position. PR; sets relative plotting for PU or PD with parameters. 

- Parameters: Pairs of integers representing plotter units if scaling is not in effect, otherwise user units, integers or decimals. 

## PU The Pen Up Instruction 

   - Page 3-2 

- PU (;) or 

- PU Xi coordinate, Yj coordinate (,... Xn, Yn coordinates) (; ) Purpose: Programmatically raises the pen. Parameters may be included as in PA or PR. 

B-8 INSTRUCTION SYNTAX 
