_ 

|E-Mask||Error||
|---|---|---|---|
|BitValue | Bit |Number|||Meaning|
|1|0|1|Instruction not recognized|
|2|1|2|Wrong number ofparameters|
|4|2|3|Bad parameter|
|8|3|4|Not used|
|16|4|5|Unknown character set|
|32|5|6|Position overflow|
|64|6|7|Not used|
|128|7|8|Vector orPD received with pinch|
||||wheelsup|



The default E-mask value of 223 (128 + 64+ 16+8+4+4+42 41) will specify that all errors except error 6 will set the error bit in the status byte and turn on the ERROR LED whenever they occur. Error 6 will not set the error bit or turn on the ERROR LED if it occurs, since it is not included in the E-mask value. Errors 4 and 7 never occur so setting the E-mask to 151 will set the same conditions as the default value 223. 

The S-mask value specified is the sum of any of the bit values shown below. It determines whena service request message will be sent. When a bit of the status byte changes value, the status byte is ANDed with the S-mask in a bit-by-bit fashion to determine if bit 6 of the status byte is to be set and the service request message sent. The status of bit 6 changes as plotter conditions change, and is cleared or set as required. 

|S-Mask|Status Bit|||
|---|---|---|---|
|BitValue|Number||Meaning|
|1|0|Pen down||
|2|1|P1 or P2 changed||
|4|2|Digitized point available||
|8|3|Initialized||
|16|4|Ready for|data; pinch wheels down|
|32|5|Error||
|64|6|Not used||
|128|7|Notused||



For example, an S-mask value of 4 specifies that when a digitized point is available, setting bit 2, the service request message will be sent. Setting other bits will not send the service request message. 

GETTING STARTED 1-13 
