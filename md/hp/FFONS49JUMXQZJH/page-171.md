Parameter Usage in Plotter/Computer Communication 

||With Handshake|Characters|With Plotter||
|---|---|---|---|---|
||||Output||
|Parameter|In Mode 1|In Mode 2|Commands||
|turnaround|yes|yes|yes||
|delay|||||
|output trigger|yes|no|yes||
|character|||||
|echo|yes|no|yes||
|terminator|||||
|output|yes|no|yes|:|
|terminator|||||
|output|no|no|yes||
|initiator*|||||
|intercharacter|yes|yes|yes||
|delay|||||



*If an output initiator is required on enquiry responses, it should be specified as the first character of the acknowledgment string and/or the immediate response string, depending on the system. 

Mes =See ESC. I and ESC. N. 

## The Set Handshake Mode 2 Instruction, 

SHEE §=The set handshake mode 2 instruction, ESC . I, may be used with the enquire/acknowledge or Xon-Xoff handshake to establish parameters for the plotter’s communication format. | USES | It establishes the data block size, the enquiry character, and the acknowledgment string for the enquire/acknowledge handshake when the computer expects only the turnaround delay, and not the other parameters set by ESC. M, to be included in the response to the enquiry character. It sets the Xoff threshold level and the Xon trigger character for Xon-Xoff handshake. 

SYNTAX . LL (KDEC>) ; («KASC>) ; (KASC>(;...<ASC>)) ]: DEFAULT . 1: (or .H:) Neither Xon-Xoff nor enquire/ acknowledge handshake is enabled. Block size is 80 bytes, and there is 

RS-232-C/CCITT V.24 INTERFACING 10-29 
