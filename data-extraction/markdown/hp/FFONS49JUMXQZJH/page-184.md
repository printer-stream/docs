For more detailed information on HP-IL and how your computer sends commands and data through the interface, refer to your HP-IL and computer documentation. Typically, BASIC statements are used to send interface commands and messages.

## HP-IL Implementation on the 7470

The HP-ILcapability subsets for the 7470 are listed in the following table.

| Function   | Description         | Implementation                                                                                                                                                                  |
|------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R          | Receiver.           | Complete capability.                                                                                                                                                            |
| AH         | Acceptor handshake. | Complete capability.                                                                                                                                                            |
| SH1        | Source handshake.   | Complete capability.                                                                                                                                                            |
| D          | Driver.             | Complete capability.                                                                                                                                                            |
| L1         | Listener.           | Basic listener.                                                                                                                                                                 |
| L3         | Listener.           | Unaddress if addressed to talk (MTA).                                                                                                                                           |
| LEO        | Extended listener.  | No capability.                                                                                                                                                                  |
| T1         | Talker.             | Basic talker; send data.                                                                                                                                                        |
| T2         | Talker.             | Send status. (Returns a byte containing the status that is sent with the HP-GLoutput status command, OS. Does not reset bit number 3, the initialize flag, in the status byte.) |
| T3         | Talker.             | Send device ID. (Returns the string 'HP747OA' followed by a carriage return and a line feed.)                                                                                   |
| T4         | Talker.             | Send accessory ID. (Returns a byte with the following bit pattern: 0110 0000 or 60 hex.)                                                                                        |
| T6         | Talker.             | Unaddress if addressed to listen (MLA).                                                                                                                                         |
