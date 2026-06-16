## Interface Functions

Interface functions provide the physical capability,to communicate via HP-IB. These functions are defined in the ANSI/IEEE 488-1978 Standard. This standard, which is the designer's guide to the bus, defines each interface function in terms of state diagrams that express all possible interactions.

Bus capability is grouped under 10 interface functions, for example: Talker, Listener, Controller, Remote/ Local. The following table lists the functions, including two special cases of Controller.

HP-IB Interface Functions

| Mnemonic                         | Interface Function Name                                                                                                                                                                                                                                              |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SH AH T L SR RL PP DC DT C CN CS | Source Handshake Acceptor Handshake Talker (orTE = Extended Talker)* Listener (or LE = Extended Listener)* Service Request Remote Local Parallel Poll Device Clear Device Trigger Any Controller A Specific Controller (for example: CA,CB...) The System Controller |
