## Bus Messages

Since interface functions are the physical agency through which bus messages are implemented, each device must implement one or more functions to enable it to send or receive a given bus message.

The following table lists the functions required to implement each bus message. Each device's operating manual lists the functions imple mented by that device. Some devices, such as the 98034AInterface, list the functions implemented directly on the device.

## Functions Used by Each Bus Message

| Bus Message                                                                                                                      | sender function -~ receiver function(s) Functions Required (support functions)                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Trigger Clear Remote Local Local Lockout Require Service Status Byte Status Bit Pass Control Abort Clear Lockout/ Set Local | T ~ L* (SH, AH) C ~ DT* (L, SH, AH) C ~ DC* (L, SH, AH) CS-~ RL* (SH, AH) C ~ RL* (L, SH, AH) C ~ RL* (SH, AH) CS "' RL* SR* -~C T - L*(SH, AH) PP*-'C cA~ CB (T, SH, AH) CS-~T,L *0 |
