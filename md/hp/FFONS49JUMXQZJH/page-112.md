## The Output Status Instruction, OS 

DESCRIPTION Miausrs output status instruction, OS, is used to output the decimal equivalent of the status byte. 

UNS «This instruction is useful in debugging operations and in digitizing applications. 

SMAUER =OS (terminator) EXPLANATION Bg parameters are used. The instruction will execute even if +0 terminator is received. 

Up: eipt of the OS instruction, the internal eight-bit status byte is eor + red to an integer between 0 and 255. Output is in ASCII in the torm: 

## status [TERM) 

The status bits are defined as follows: 

|Bit|Bit||
|---|---|---|
|Value|Position|Meaning|
|1|0|Pen down.|
|2|1|P1 or P2 changed; cleared by reading|
|||output ofOP in HP-IB or HP-IL system|
|||or by actual output ofP1,P2 in RS-232-C|
|||system.|
|4|2|Digitized point available; cleared by|
|||reading digitized value in HP-1B or|
|||HP-IL system orby output ofpoint in|
|||RS-232-C system.|
|8|3|Initialized; cleared by reading OS output|
|||in HP-IB or HP-IL system or by output|
|||ofthe status byte in RS-232-C system.|
|16|4|Ready for data; pinch wheels down.|
|32|5|Error; cleared by reading OE output in|
|||HP-IB or HP-IL system or by output of|
|||the error in RS-232-C system.|
|64|6|Require service message set (always 0|
|||for OS ;0or 1 for HP-IB serial poll).|
|128|7|Notused|



Upon power up, the status is decimal 24, the sum of 8 (initialized) and 16 (ready for data). Upon output of the status byte after an OS command, bit position 3 is cleared. 

7-8 OBTAINING INFORMATION FROM THE PLOTTER 
