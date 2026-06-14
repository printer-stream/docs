## The Define Terminator Instruction, DT 

The define terminator instruction, DT, provides the means to specify the character to be used as the label terminator. 

The command can be used to change the label terminator from its default value if ETX (decimal equivalent 3) cannot be used by your computer. 

## DT t (terminator) wheret is the label terminator. 

The label mode can only be terminated by sending a label terminator at the end of the label character string. ASCII control characters (decimal equivalent 1 through 32) can be defined as label terminators and will not print when invoked, although the function normally performed by the character will be performed (i.e., LF will terminate a label but will also cause a line feed). ASCII characters with decimal equivalent values 33 through 127 can also be defined as the terminator, but the character will be printed at the end of the label character string. The ASCII control characters NULL (decimal equivalent 0) and ESC (decimal equivalent 27) cannot be used as label terminators. Also in the RS-232-C environment, ENQ (decimal equivalent 5) is not a valid terminator. 

NOTE: A DT command with no parameter does not establish ETX as the default terminator, since the character immediately following the mnemonic DT is taken as a parameter. Only a DF or IN command or use of the ETX character itself as the instruction’s parameter can be used to reestablish ETX as the label terminator. @ 

The following examples of text in a label command demonstrate the use of the label terminator. 

"TN; SP2;SC0,5000,0,5000;" "PAO, 4500;LBDefault contral character ETH Rr & "LBterminates by performing end-Qtr&" "LBof-text function.&" "PAC, 3900; 07T#;LBPrinting characters terminate, gle" "LEbut are also printed.#" "PAD, 3400; DT; LBContral characters terminatelre” "LBand perform their function.®" 

5-6 LABELING 
