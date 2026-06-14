The Tick Instructions, XT and YT SSH §=The tick instruction, XT, draws a vertical X-tick at the current location. The tick instruction, YT, draws a horizontal Y-tick at the current pen location. | USES | These instructions can be used to draw tick marks on axes, draw grid lines by making the tick length 100%, or draw horizontal or vertical lines either centered on or ending at the current pen position. SYNTAX Beg (terminator) or YT (terminator) 

PAPEL §=Neither instruction requires parameters; numeric parameters are ignored. The terminator should be included to complete the command. 

The tick mark will be drawn at the current pen position whether the pen is up or down. 

The tick length is specified by the tick length instruction, TL. If no tick length is specified, the length defaults to 0.5% of (P2x — Plx) for YT or 0.5% of (P2y — Ply) for XT for each (positive and negative) portion of the tick. Refer to The Tick Length Instruction, TL, which follows. 

## The following example draws a horizontal line 3000 plotter units long, places X-ticks at the endpoints and at X-locations 1200 and 2200, and raises and stores the pen. "IN; SP2;PAZ00,500; PD; XT;PR1000,0;xT;" "PR1000, 0;XT;PR1000,0;XT;PU;SPO;" eHte eee 

The Tick Length Instruction, TL SS HiiMaMe = The tick length instruction, TL, specifies the length of the tick marks drawn by the plotter. The tick lengths are specified as a percentage of the horizontal and vertical distances between the scaling points P1 and P2. | USES | The instruction can be used to set the length of both positive and negative portions of tick marks. The instruction can be used with only one parameter to suppress the negative portion of a tick mark, or with a first parameter of zero to suppress the positive portion of the tick. Setting the tick length, tp, to 100 enables the user to draw grids easily, using XT and YT instructions. 

4-2. ENHANCING THE PLOT 
