## The Set Output Mode Instruction, ESC . M 

SHEE §=The set output mode instruction, ESC. M, establishes parameters for the plotter’s communication format. 

| USES | The instruction is used to establish a turnaround delay, an output trigger character, an echo terminate character, and an output initiator character. It is also used to change the output terminator from its default value, carriage return. 

- SYNTAX . M[(KDEC>) ; (KASC>) ; («KASC>) ; (KASC>(; (KASC>)) ;(<ASC>) ]: 

DEFAULT .M: Sets the carriage return character (decimal equivalent 13) as the output terminator. It also specifies that there is no turnaround delay and no output trigger, echo terminate, or output — initiator character . 

Ag UUEUULE =A colon must be used following the last parameter (if any). Use of the instruction without parameters is equivalent to ESC. M: (see DEFAULT). 

A description of the instruction’s parameters follows. 

- <DEC> The first parameter is optional. If present, it is the turnaround delay. The delay implemented is ((parame ter X 1.1875)mod 65 536)/1.2 milliseconds. The parameter range is 0 to 54 612. If parameters follow, the semicolon must be included even if this decimal parameter is omitted. 

- <ASC> The second parameter is also optional and, if omitted, assumes its default value of 0 (no trigger character). If included, it specifies a single character which becomes the output trigger character. The parameter may be the decimal equivalent of any ASCII character in the range 0 to 127. If parameters follow, the semicolon must always be included, even when this parameter is omitted. 

- <ASC> The third parameter is optional and, if omitted, assumes its default value 0 (no echo terminate character). If included, it specifies a single character which becomes the echo terminate character. The parameter may be the decimal equivalent of any ASCII character in the range 0 to 127. If parameters follow, the semicolon must always be included, even when this parameter is omitted. 

RS-232-C/CCITT V.24 INTERFACING 10-33 
