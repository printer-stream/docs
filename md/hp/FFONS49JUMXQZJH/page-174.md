## SYNTAX 

## iJ 

eM §=6This instruction aborts any single device control instruction that may be partially decoded or executed. Unspecified parameters of aborted instructions are defaulted. All pending or partially transmitted output requests, from either HP-GL or device control instructions, are immediately terminated, including output responses and handshake parameters. Intermediate output operations such as turnaround delay and echo suppression are aborted, and the buffer input is enabled. The handshake and output mode parameters remain as specified. 

## The Abort Graphic Instruction, ESC . K USHUMUL Z 

USHUMUL Z =The abort graphic instruction, ESC. K, aborts any partially decoded HP-GL instruction and discards instructions in the buffer. 

| USES | The instruction can be used as part of an initialization sequence when starting a new program or to terminate plotting of HP-GL instructions in the buffer. 

SYNTAX .K 

EXPLANATION Any partially decoded HP-GL instruction is aborted and all instructions in the buffer are discarded. A partially executed instruction is allowed to finish. 

## The Output Buffer Size Instruction, ESC . L 

DESCRIPTION Biiwirs output buffer size instruction, ESC . L, outputs the size, in bytes, of the plotter’s buffer. 

| USES | The instruction is used to obtain information on the size of the plotter’s buffer. This information might be used to determine parameters of commands which set up handshaking. 

SYNTAX .L 

EXPLANATION Bing parameters are used. The instruction causes the 7470 to output, in ASCII, a decimal number equal to the number of bytes in the plotter’s buffer. 

## RESPONSE 

<DEC> 255 

[TERM] Defaults to carriage return, CR, or is as set by ESC. M. 

10-32 RS-232-C/CCITT V.24 INTERFACING 
