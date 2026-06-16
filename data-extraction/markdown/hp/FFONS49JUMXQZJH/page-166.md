Default Values; Omitting Parameters Any parameter may be omitted or, if the parame­ ter is required, it can be set to its default value by omitting the parameter and entering only the semicolon as a delimiter. All parameters may be omitted and therefore set to default values by entering only the colon terminator after the instruction.

<!-- image -->

Denotes the single ASCII character, Escape, which in most computers is accessed by striking a single key on the keyboard.

NOTE: There is no delimiter (semicolon) be­ tween the three-character command sequence, e.g., . O,andthefirstparameter. I 3

## The Plotter OnInstruction, ESC.( or ESC . Y

DESCRIPHDN The plotter on instruction, ESC . ( or ESC . Y, places a plotter which is powered on into the on-line, programmed-onmode so that it will accept incoming data and interpret it as plotter instructions.

M This instruction is used when the rear-panel switch labeledY/D is set to Yto ready the plotter to accept other instructions. It is sent at the beginning of any plotting program or when the user wishes to resume plotting after the plotter has been turned off by an ESC . ) or ESC . Z command or a Break.

<!-- image -->

EXPLANATIONThis instruction is ignored when the rear-panel switch labeled Y/Dis set to Dsince, in that case, turning on the power places the plotter in the programmed-onstate.

Beginning with the next character, the plotter will accept incoming data and interpret it as plotter instructions. If the plotter is already in the programmed-on state, it will ignore this instruction.

## The Plotter OffInstruction, ESC.) or ESC . Z

The plotter off instruction, ESC . ) or ESC . Z, takes the plotter out of on-line, programmed-on state so that it neither accepts nor interprets incoming data until another plotter on instruction is received. Z, takes the
