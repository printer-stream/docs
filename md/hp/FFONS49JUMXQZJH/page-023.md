## SYNTAX Maya terminator EXPLANATION BiRNga parameters are used; a numeric parameter will cause error 2 and the instruction will not execute. A DF command sets the following plotter functions to the conditions shown in the following table. P1 and P2 are not changed. 

## Default Conditions 

**==> picture [320 x 240] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|
|Plotting|mode|Absolute|(PA)|
|Relative|character|direction|||Horizontal|(DR1,0)|
|Line|type|Solid|line|
|Line|pattern|length|4%|of|the|distance|from|P1|to|P2|
|Input window|Mechanical|limits|of plotter|
|Relative|character|size|Width|=|0.75%|of (P2x —|P1x)|
|Height|=|1.5%|of (P2y —|Ply)|
|Symbol|mode|Off|
|Tick|length|tp =|tn|=|0.5%|of (P2x —|P1x)|for|Y-tick|
|and|0.5%|of (P2y —|Ply)|for|X-tick|
|Standard|character|set|Set|0|
|Alternate|character|set|Set|0|
|Character|set|selected|Standard|
|Character|slant|0|degrees|
|Mask|value|223,0,0|
|Digitize|clear|On|
|Scale|Off|
|Pen|velocity|38.1|cm/s|(15|in./s)|
|Label|terminator|ETX|(ASCII|decimal|equivalent|3)|
|Chord|angle*|Set|to|5|degrees|for AA,|AR,|and|CI|

**----- End of picture text -----**<br>


*Applicable only to Option 001 plotters that have the serial prefix number 2308A or higher. 

The Initialize Instruction, IN SHEL §=The initialize instruction, IN, returns the plotter’s graphics conditions to the initial power-on state by program control. This instruction has no effect on handshake protocol or the plotter’s state (programmed on or programmed off) in an RS-232-C environment. UNS The instruction can be used to return the plotter to a known state at the beginning of a graphics program so unwanted graphics parameters such as character size, slant, and scaling are not inherited from another program. P1 and P2 are set to power-on positions. SAUER ZN terminator 

GETTING STARTED 1-11 
