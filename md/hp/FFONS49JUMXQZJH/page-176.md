- <ASC>...<ASC> The fourth parameter is optional and defaults to 13, the decimal equivalent of the single ASCII character, carriage return. 

If included, the parameter may be the decimal equivalent(s) of one or two ASCII characters in the range 0 to 127. This becomes the output terminator. The value 0 is not transmitted and will terminate the string. If a parameter follows, the semicolon must always be included, even when this parameter is omitted. If the fifth parameter is specified, this fourth parameter must consist of two characters, or the second character must be specified as null using the semicolon. 

## <ASC> 

## OME 

- fd 

- The fifth parameter is optional and, if omitted, assumes its default value 0 (no output initiator character). If included, it is the decimal equivalent of a single character which becomes the output initiator character. The parameter may be the decimal equivalent of any ASCII character in the range 0 to 127. The parameter is followed by a colon. 

- See the ESC. N instruction. 

The flowchart on the next page depicts plotter output. 

The Set Extended Output and Handshake Mode Instruction, ESC .N SHUM §=The set extended output and handshake mode instruction, ESC . N, establishes parameters for the plotter’s communication format. WN The instruction is used to specify an intercharacter delay in all handshake modes, the immediate response string for enquire/ acknowledge handshake, or the Xoff trigger character(s) for the XonXoff handshake. 

SYNTAX . N[(<DEC>) ; (KASC>(;...<ASC>)) ]: DEFAULT -N: No intercharacter delay and no Xoff trigger character or immediate response string. ee =A colon must be used following the last parameter. Use of the instruction without parameters is equivalent to ESC. N: (see DEFAULT). 

10-34 RS-232-C/CCITT V.24 INTERFACING 
