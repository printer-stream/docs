The plotter acts on device control instructions immediately upon receipt. It does not store them in the data buffer. 

## Command Syntax for Device Control Instructions 

Device control instructions are three-character escape code sequences comprised of “ESC” and “.” followed by one of the characters @, B, E, H, I, J, K, L, M,N, or O, R, (,), Y, or Z. 

- When an instruction is put together with its required parameters, delimiters, and/or terminators, it becomes a “command.” These syntax conventions are used with the commands discussed in this chapter: 

- [ ] Brackets indicate that all parameters enclosed are optional. 

- ( ) 

   - Parentheses indicate that each individual parameter is optional. 

- ; The semicolon follows and delimits parameters. If a semicolon appears without a parameter, the parameter is defaulted. 

- : The colon terminates any command which may have parameters and can occur after any valid number of parameter entries. Any parameter that is not specified is defaulted. 

- <DEC> 

- <ASC> 

sae 

- [TERM] 

- This symbol specifies a decimal value parameter. For example, the characters 10 would represent the decimal value ten; the characters 13 would represent the decimal value thirteen. 

- This symbol specifies the decimal equivalent for an ASCII character (see the ASCII Character Equivalents table in Appendix C). In this case, the characters 10 would represent the ASCII line feed character, LF, and 13 would represent the ASCII carriage return character, CR. 

Specifies a number of optional parameters. Each parameter must be followed by a delimiter (;) or the terminator (:). 

Unless changed by an ESC. M command, all RS-232-C output responses include a CR as a terminator. 

RS-232-C/CCITT V.24 INTERFACING 10-23 
