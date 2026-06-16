&lt;ASC&gt; . . .&lt;ASC&gt; The fourth parameter is optional and defaults to 13,the decimal equivalent of the single ASCII character, carriage return.

If included, the parameter may be the decimal equiva­ lent(s) of one or two ASCII characters in the range 0 to 127.This becomesthe output terminator. The value 0 is not transmitted and will terminate the string. If a parameter follows, the semicolon must always be in­ cluded, even when this parameter is omitted. If the fifth parameter is specified, this fourth parameter must con­ sist of two characters, or the second character must be specified as null using the semicolon.

- H &lt;ASC&gt;

The fifth parameter is optional and, if omitted, assumes its default value 0 (no output initiator character). If included, it is the decimal equivalent of a single charac­ ter which becomesthe output initiator character. The parameter may be the decimal equivalent of any ASCII character in the range 0 to 127. The parameter is fol­ lowed by a colon.

EXAMPLES See the ESC . N instruction.

The flowchart on the next page depicts plotter output.

## The Set Extended Output and Handshake ModeInstruction, ESC . N

DESCWPHUN The set extended output and handshake mode instruc­ tion, ESC . N, establishes parameters for the plotter's communication format.

USES The instruction is used to specify an intercharacter delay in all handshake modes, the immediate response string for enquire/ acknowledge handshake, or the Xoff trigger character(s) for the Xon­ Xoffhandshake.

<!-- formula-not-decoded -->

DEFAULT . N : No intercharacter delay and no Xoff trigger char­ acter or immediate response string.

EXPLANATIONA colon must be used following the last parameter. Use of the instruction without parameters is equivalent to ESC . N: (see DEFAULT).
