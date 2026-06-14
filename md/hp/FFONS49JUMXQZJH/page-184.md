For more detailed information on HP-IL and how your computer sends commands and data through the interface, refer to your HP-IL and computer documentation. Typically, BASIC statements are used to send interface commands and messages. 

## HP-IL Implementation on the 7470 

The HP-IL capability subsets for the 7470 are listed in the following table. 

|R|Receiver.|Complete capability.|
|---|---|---|
|AH|Acceptor handshake.|Complete capability.|
|SH1|Source handshake.|Complete capability.|
|D|Driver.|Complete capability.|
|Ll|Listener.|Basic listener.|
|L3|Listener.|Unaddress ifaddressed|
|||to talk (MTA).|
|LEO|Extended listener.|No capability.|
|Tl|Talker.|Basic talker; send data.|
|T2|Talker.|Send status. (Returns a|
|||byte containing the|
|||status that is sent with|
|||the HP-GL output|
|||status command, OS.|
|||Does not reset bit|
|||number 3, the initialize|
|||flag, in the status byte.)|
|T3|Talker.|Send device ID.|
|||(Returns the string|
|||“HP7470A” followed|
|||by a carriage return|
|||anda line feed.)|
|T4|Talker.|Send accessory ID.|
|||(Returns a byte with|
|||thefollowing bit|
|||pattern: 0110 0000 or|
|||60 hex.)|
|T6|Talker.|Unaddress ifaddressed|
|||tolisten(MLA).|



11-2. HP-ILINTERFACING 
