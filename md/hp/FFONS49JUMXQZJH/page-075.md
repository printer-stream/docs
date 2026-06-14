EXPLANATION BBXfy parameters are used. Any parameters which follow the instruction are ignored and the standard set is selected. An alphabetic parameter will be interpreted as the first letter of the next mnemonic and may, therefore, cause an error 1 to occur after execution of the SS instruction. 

The standard ASCII character set (set 0) is automatically selected when the plotter is first turned on, initialized, or set to default values. The standard set can be selected within a label command by sending the ASCII control character for shift-in (decimal equivalent 15). 0 

The Select Alternate Set Instruction, SA SHEE §=The select alternate set instruction, SA, provides the means of selecting the alternate set designated by the most recent CA instruction as the character set to be used for all labeling. | USES | The command may be used to shift from the currently designated standard character set to the currently designated alternate character set to access characters in a second set. Sending the control character shift-out inside a label string is equivalent to executing this command. 

SE SA (terminator) EXPLANATION BiBXtn parameters are used. Any parameters which follow the instruction are ignored and the alternate set is selected. An alphabetic parameter will be interpreted as the first letter of the next mnemonic and may, therefore, cause an error 1 to occur following execution of the SA instruction. 

The command should be executed prior to executing a label statement whenever the alternate character set is to be used. The alternate set can be selected within a label command by sending the ASCII control character for shift-out (decimal equivalent 14). Shift-in and shift-out are particularly useful whena line of text must be composed with symbols from two character sets. 

The following commands label using two different character sets where the underline is drawn with and without a backspace. The shift-out character is used to change from the standard to the alternate set. 

"SP2;C50;CH4;55;LBS5_E_T_O_&5_E_T_4_&" 

## S_F_T_ON_SET4 

LABELING 5-5 
