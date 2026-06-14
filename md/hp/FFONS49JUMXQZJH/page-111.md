The plotter will always output the following: 

; 

## 40 ,40[TERM] 

These factors indicate that there are approximately 40 plotter units per millimetre in the X-axis and in the Y-axis (0.025 mm/plotter unit). [TERM] is the output terminator for the interface installed. 

## The Output Identification Instruction, OI DESCRIPTION iiwirs output identification instruction, OI, is used to out- 

put a plotter identifier. 

WNSH This instruction is especially useful in a remote operating environment to determine which model plotter is on-line. SYNTAX Bieys (terminator) EXPLANATION Bane parameters are used. The instruction will execute even if no terminator is received. 

The plotter will always output the following character string: 

7470A [TERM] 

[TERM] is the output terminator for the interface installed. 

The Output Options Instruction, OO DESCRIPTION Biya output options instruction, OO, is used to output eight option parameters. 

USES Bw instruction is especially useful in a remote operating environment to determine which options are available in the plotter which is on-line. SYNTAX OO (terminator) EXPLANATION ine parameters are used. The instruction will execute even if no terminator is received. 

The plotter will always output the appropriate combination of eight integers in ASCH, separated by commas. The options included in the plotter are indicated by a 1 as defined below. 

0,1,0,0,1,0,0,0[TERM] LT Indicates arcs and circle instructions are included (available only with RS-232-C plotters that have the Serial Prefix number 2308A or higher). 

Indicates pen select capability -is included (available on all plotters). 

[TERM] is the output terminator for the interface installed. 

OBTAINING INFORMATION FROM THE PLOTTER 7-7 
