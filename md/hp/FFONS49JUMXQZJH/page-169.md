## The Output Extended Error Instruction, 

DESCRIPTION Siwy output extended error instruction, ESC . E, outputs a number which defines any RS-232-C related I/O error and turns off the front-panel ERROR light. 

| USES | The instruction is used to define what type of RS-232-C related I/O error has occurred, if any. SYNTAX _E EXPLANATION Biixen parameters are used. 

## RESPONSE 

- <DEC> The plotter’s response is a decimal number, either 0 orin the range 10-16, followed by the output terminator. The meaning of the response is as defined in the following table. 

**==> picture [251 x 322] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||||
|---|---|---|---|---|---|---|---|
|Error|
|No.|Meaning|
|0|No|I/O|error|has|occurred|
|10|Output|instruction|received|while|another|
|output|instruction|is|executing.|The|original|
|instruction|will|continue|normally;|the|one|
|in|error|will|be|ignored.|
|11|Invalid|byte|received|after|first|two|charac-|
|ters,|H3Q|.,|in|a|device|control|instruction.|
|12|Invalid|byte|received|while|parsing|a|device|
|control|instruction.|The parameter|containing|
|the|invalid byte|and|all|following|parameters|
|are|defaulted.|
|13|Parameter|out|of range.|
|14|Too|many|parameters|received.|Additional|
|parameters|beyond|the|proper number|are|ig-|
|nored;|parsing|of the|instruction|ends|when|a|
|colon|(normal|exit)|or the|first|byte|of another|
|instruction|is|received|(abnormal|exit).|
|15|A|framing|error,|parity|error,|or|overrun|
|error|has|been|detected.|
|16|The input buffer|has|overflowed.|As|a|result,|
|one|or more|bytes|of data|have been|lost,|and|
|‘|therefore|an HP-GL|error|will|probably|occur.|

**----- End of picture text -----**<br>


RS-232-C/CCITT V.24 INTERFACING 10-27 
