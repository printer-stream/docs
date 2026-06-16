executed while the alternate set is selected will not change the set used for labeling until the standard set is selected.

A command CS with no parameters defaults to set 0. A CS command with an invalid first parameter will set an error condition (error 3),and the command will be ignored.

## The Designate Alternate Character Set Instruction, CA

DESRIPTIUN The designate alternate character set instruction, CA, provides the means of designating one of the five character sets (0 through 4)as the alternate character set.

USES The instruction can be used to provide an additional character set that can be easily accessed from a program, especially when a single label contains characters found in two different sets.

SYN TAX CA

character set number (terminator)

EXPLANATIONThe character set number may be from 0 through 4. The set designated by the CA instruction is used for all labeling opera­ tions when the alternate set is selected by the SA instruction or by the control character shift-out(decimal equivalent 14) in a label string. Character set 0 is automatically designated as the alternate character set whenever the plotter is initialized or set to default values.

A CA command executed while the alternate set is selected will imme­ diately change the character set used for labeling. CA commands executed while the standard set is selected will not change the set used for labeling until the alternate set is selected.

A command CA with no parameters defaults to set 0. A CA command with an invalid first parameter will set an error condition (error 3),and the command will be ignored.

## The Select Standard Set Instruction, SS

DESCRIPTIONThe select standard set instruction, SS, provides the means of selecting the standard set designated by the CS instruction as the character set to be used for all labeling.

The command may be used to shift from the currently desig­ nated alternate character set to the currently designated standard character set so characters in another set may be accessed. Using the control character shift-in inside a label string is equivalent to executing this command. desig-

3YNTAX

SS (terminator)
