| USES | The instruction is used to deactivate the plotter. It is used at the end of a graphics program or in some environments to allow data to be passed through the plotter to the terminal. 

## SYNTAX 

.) 

**==> picture [10 x 6] intentionally omitted <==**

**----- Start of picture text -----**<br>
or<br>**----- End of picture text -----**<br>


.Z 

Ae EEULE =6This instruction is ignored when the rear-panel switch labeled ¥/D is set to D. When that switch is set to D, it is not possible to turn the plotter off programmatically. 

Beginning with the next character, the plotter will assume a passive state and remain in that state until a plotter on instruction is received. Any HP-GL instructions remaining in the buffer at the time that a_ plotter off instruction is received are executed. However, no additional HP-GL instructions will be accepted by the plotter. 

NOTE: A Break signal from the terminal will have the same effect as a plotter off instruction. m 

## The Set Plotter Configuration Instruction, 

- DESCRIPTION Miswerswerse plotter configuration instruction, ESC . @, sets 

- parameters necessary for hardwire handshake mode and monitor mode. | USES | The instruction is used to enable or disable hardwire handshake or monitor mode. SYNTAX - @[(<DEC>);(<ASC>) J: DEFAULT -@: Enables hardwire handshake and disables moni- 

- tor mode. ACU = Use of the instruction without parameters enables hard- 

- wire handshake and disables monitor mode. A description of the instruction’s parameters follows: <DEC> The first parameter is not required; if a parameter is included it is ignored. The semicolon must precede any second parameter. 

   - <ASC> The second parameter establishes Data Terminal Ready, CD, line control. Only bits 0, 2, and 3 of the parameter are used, as shown in the following table. 

RS-232-C/CCITT V.24 INTERFACING 10-25 
