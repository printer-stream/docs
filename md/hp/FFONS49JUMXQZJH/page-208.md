## RS-232-C Instruction Syntax 

This section lists the formal syntax for each RS-232-C device control instruction in alphabetical order of the escape sequence. Refer to the indicated page for details. 

## Plotter On 

Page 10-24 

.( or .Y Purpose: Places the plotter in a programmed-on state. 

## Plotter Off 

## Page 10-24 

.) or Z Purpose: Places the plotter in a programmed-off state. 

## Set Plotter Configuration 

## Page 10-25 

-@ [(<DEC>);(<ASC>) ]: 

Purpose: Enables or disables hardwire handshake mode. 

Parameters: <DEC> — Ignored. 

<ASC> — Data Terminal Ready (CD) line control. ASCII decimal equivalent of 4-bit word (0 to 15). 

## Output Buffer Space 

## Page 10-26 

.B 

Purpose: Outputs the number of byte spaces currently available for data in the buffer. Response: <DEC> [TERM] — 0 to 255. 

## Output Extended Error 

## Page 10-27 

.E 

Purpose: Outputs a decimal code to identify the type of RS-232-C related error that occurred. Response: <DEC> [TERM] — 0, no error, or 10 - 16. 

B-12 INSTRUCTION SYNTAX 
