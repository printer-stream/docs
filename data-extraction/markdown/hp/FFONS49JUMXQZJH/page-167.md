<!-- image -->

M The instruction is used to deactivatethe plotter.It is used at the end of a graphics program or in some environments to allow data to be passed through the plotter to the terminal.

SYNTAX.) 01' .Z

EXPLANATIONThis instruction is ignored when the rear-panel switch labeled Y/Dis set to D.When that switch is set to D,it is not possible to turn the plotter off programmatically.

Beginning with the next character, the plotter will assume a passive state and remain in that state until a plotter on instruction is received.

Any HP-GL instructions remaining in the buffer at the time that a i plotter off instruction is received are executed. However, no additional HP-GL instructions will be accepted by the plotter.

NOTE:A Break signal from the terminal will have the same effect as a plotter off instruction. I

## The Set Plotter Configuration Instruction, ESC . @

UESCRIP-'UN The set plotter configuration instruction, ESC . @, sets parameters necessary for hardwire handshake modeand monitor mode.

'E3 Theinstructionis usedto enable or disablehardwire handshake or monitor mode.

SYNTAX . @[ (&lt;DEC&gt;) ; (&lt;ASC&gt;) ]:

A

DEFAULT . @: Enables hardwire handshake and disables moni­ tor mode.

EXPLANATION Use of the instruction without parameters enables hard­ wire handshake and disables monitor mode.

Adescription of the instruction's parameters follows:

- &lt;DEC&gt;
- &lt;ASC&gt;

The first parameter is not required; if a parameter is included it is ignored. The semicolon must precede any second parameter.

The second parameter establishes Data Terminal Ready, CD, line control. Only bits 0, 2, and 3 of the parameter are used, as shown in the following table.
