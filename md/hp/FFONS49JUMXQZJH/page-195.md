## Interface Functions 

Interface functions provide the physical capability, to communicate via HP-IB. These functions are defined in the ANSI/IEEE 488-1978 Standard. This standard, which is the designer’s guide to the bus, defines each interface function in terms of state diagrams that express all possible interactions. 

Bus capability is grouped under 10 interface functions, for example: Talker, Listener, Controller, Remote/Local. The following table lists the functions, including two special cases of Controller. 

## HP-IB Interface Functions 

|SH|Source Handshake|
|---|---|
|AH|Acceptor Handshake|
|T|Talker (orTE = Extended Talker)*|
|L|Listener (orLE = Extended Listener)*|
|SR|Service Request|
|RL|Remote Local|
|PP|Parallel Poll|
|DC|Device Clear|
|DT|Device Trigger|
|Cc|Any Controller|
|Cn|A Specific Controller (for example: Ca, Cp...)|
|Cg|TheSystemController|



*Extended Talkers and Listeners use a two-byte address. Otherwise, they are the same as Talker and Listener. 

AN HP-IB OVERVIEW A-7 
