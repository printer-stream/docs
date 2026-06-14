## Bus Messages 

Since interface functions are the physical agency through which bus messages are implemented, each device must implement one or more functions to enable it to send or receive a given bus message. 

The following table lists the functions required to implement each bus message. Each device’s operating manual lists the functions imple mented by that device. Some devices, such as the 98034A Interface, list the functions implemented directly on the device. 

## Functions Used by Each Bus Message 

**==> picture [323 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||
|---|---|---|---|---|---|---|
|Functions|Required|
|sender|function|—|receiver|function(s)|
|Bus Message|(support|functions)|
|Data|T —|L*|(SH,|AH)|
|Trigger|C —|DT*|(L,|SH, AH)|
|Clear|C|—|DC*|(L,|SH,|AH)|
|Remote|Cg|RL*|(SH, AH)|
|Local|C —|RL*|(L,|SH,|AH)|
|Local|Lockout|C|—|RL*|(SH,|AH)|
|Clear Lockout/Set|Local|| Cg ~ RL*|
|Require|Service|SR* —C|
|Status|Byte|T —|L*|(SH,|AH)|
|Status|Bit|PP*|—|C|
|Pass|Control|Ca-|Cp|(T,|SH,|AH)|
|Abort|Cg —|T,|L¥#C|

**----- End of picture text -----**<br>


*Since more than one device can receive (or send) this message simultaneously, each device must have the function indicated by an *. 

A-8 AN HP-IB OVERVIEW 
