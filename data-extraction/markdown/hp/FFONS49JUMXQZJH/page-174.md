## SYNTAX \_ J

EXPLANAHDNThis instruction aborts any single device control instruc­ tion that may be partially decodedor executed.Unspecified parameters of aborted instructions are defaulted. All pending or partially trans­ mitted output requests, from either HP-GL or device control instructions, are immediately terminated, including output responses and handshake parameters. Intermediate output operations such as turnaround delay and echo suppression are aborted, and the buffer input is enabled. The handshake and output mode parameters remain as specified.

## The Abort Graphic Instruction, ESC. K

DESCMPHUN The abort graphic instruction, ESC. K, aborts any partially decoded HP-GL instruction and discards instructions in the buffer. A

NEE The instruction can be used as part of an initialization sequence when starting a new program or to terminate plotting of HP-GL instructions in the buffer. |

## SYNTAX\_ K

EXPLANATIONAny partially decoded HP-GL instruction is aborted and all instructions in the buffer are discarded. A partially executed instruction is allowed to finish.

## The Output Buffer Size Instruction, ESC . L

DESCRIPTION The output buffer size instruction, ESC . L, outputs the size, in bytes, of the plotter's buffer.

USES The instruction is used to obtain information on the size of the plotter's buffer. This information might be used to determine parameters of commands which set up handshaking. |

## SYNTAX ,1, En

EXPLANATIONNo parameters are used. The instruction causes the 7470 to output, in ASCII, a decimal number equal to the number of bytes in the plotter's buffer.

## RESPONSE

&lt;DEC&gt;

[TERM]

255

Defaults to carriage return, CR, or is as set by ESC . M.
