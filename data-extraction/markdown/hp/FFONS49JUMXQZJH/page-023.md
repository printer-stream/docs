<!-- image -->

EXPLANATIONNo parameters are used; a numeric parameter will cause error 2 and the instruction will not execute.

A DF command sets the following plotter functions to the conditions shown in the following table. P1 and P2 are not changed.

## Default Conditions

| Function                                                                                                                                                                                                                                                                                               | Conditions                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plotting mode Relative character direction Line type Line pattern length Input window Relative character size Symbol mode Tick length Standard character set Alternate character set Character set selected Character slant Mask value Digitize clear Scale Pen velocity Label terminator Chord angle* | Absolute (PA) Horizontal (DR1,0) Solid line 4% of the distance from P1 to P2 Mechanical limits of plotter Width = 0.75%of (P2X-Plx) Height = 1.5%of (P2y -Ply) Off tp = tn = 0.5%of (P2X- Plx) for Y-tick and 0.5% of (P2y -Ply) for X-tick Set 0 Set 0 Standard 0 degrees 223,0,0 On Off 38.1cm/s (15in./s) ETX (ASCII decimal equivalent 3) Set to 5 degrees for AA, AR, and CI |

## The Initialize Instruction, IN

UESCWP-'UN The initialize instruction, IN, returns the plotter's graphics conditions to the initial power-on state by program control. This instruction has no effect on handshake protocol or the plotter's state (programmed on or programmed off) in an RS-232-C environment.

<!-- image -->

The instruction can be used to return the plotter to a known state at the beginning of a graphics program so unwanted graphics parameters such as character size, slant, and scaling are not inherited from another program. P1 and P2 are set to power-on positions. a known

SYNTAX IN

terminator

<!-- image -->
