NOTE: A buffer overflow condition may also cause an HP-GL error to occur. In this case, an HP-GLIN or OF command or a front-panel reset must be executed in order to clear the ERROR light. See Chapter 7 for an explanation of the output error instruction, OE. 

## Handshaking 

The 7470 uses a 255-byte input buffer to synchronize the processing of data with the rate at which it is received. The presence of an input buffer requires that the computer and the plotter transfer information to one another in such a way that data will not be lost or misinterpreted. This is the purpose of handshaking. 

The 7470 is capable of using any one of four handshaking methods to prevent buffer overflow and the resulting loss of data. The computer system’s capabilities and requirements dictate which handshake method is appropriate. 

- e Hardwire Handshake — uses a physical wire, pin 20 of the RS-232-C cable, to control handshaking. It can be used if the computer system can or does monitor pin 20 (DTR). 

- e Xon-Xoff Handshake — is managed by the peripheral device. It can be used if the computer system follows an Xon-Xoff protocol (control characters are transmitted from the peripheral to the computer). 

- e Enquire/Acknowledge Handshake — is managed by the computer system and interface. This handshake is often used in HewlettPackard systems and is so named because the ASCII characters ENQ and ACK may be used to control the handshake. 

- e Software Checking Handshake — is managed by the applications programmer. It can be used on almost any computer system, but it must be used if the system cannot implement any of the other three handshaking methods. 

Once the handshake method is selected, the 7470 can be programmatically instructed to match the computer system requirements, implement the chosen handshake method, and function properly within the system-dependent communication environment. This is done by specifying certain variables in device control commands which are issued to the 7470 at the beginning of each computer session or graphics program. The variables, which may be specified by using the decimal value of the character desired to establish one of the four handshake methods available to the 7470, are: 

- e Output Trigger Character — The output trigger character, when used, is the last character output by the computer when making a request of a graphics peripheral. Defining this character in a command tells the plotter, “Don’t respond to my request until you receive 

- 10-14 RS-232-C/CCITT V.24 INTERFACING 
