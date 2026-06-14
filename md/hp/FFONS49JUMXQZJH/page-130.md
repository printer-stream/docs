## HP-IB Implementation on the 7470 

The HP-IB conforms to ANSI/IEEE 488-1978 specifications, and direct interconnection of the HP-IB is via a connector on the rear panel. 

The HP-IB functions implemented in the 7470 are as follows: 

1. Source Handshake (SH1) 

2. Acceptor Handshake (AH1) 

3. Talker (T2) 

4. Listener (L2) 

5. Service Request (SR1) 

6. No Remote Local (RLO) 

7. Parallel Poll (PPO if lon; PP2 if addr <8; PPO otherwise) 

- 8 Device Clear (DC1) 

9. No Device Trigger (DT0) 

10. No Controller (CO) 

## Interface Switches and Controls 

The 7470 plotter functions in either of two modes, addressable mode and listen-only mode. In addressable mode, the plotter can function as a talker or as a listener depending on the instructions it receives from the controller. In listen-only mode, it can only listen and it hears all activity on the bus. 

## Addressing the Plotter 

Rear panel switches provide for selection of the plotter address or listenonly mode. Each HP-IB interface can have as many as 15 devices connected to it, set to different specific address codes. The plotter can be set to any one of 31 HP-IB addresses, ranging from 0 through 30. Each address can be selected by setting the switches on the rear panel to the appropriate binary bit positions for the particular address value desired. The address selected establishes the 7470’s device address. When using the plotter with an HP desktop computer, do not use 21 which is reserved for the desktop computer’s address. When not using an HP desktop computer, be sure the computer and plotter do not have the same address. (Refer to the documentation for your computer.) Address 31 is used to set the plotter to listen-only mode. 

The plotter is set to an address code of 05 at the factory. This corresponds to a listen character of % and a talk character of E. Check the following figure for the factory-set address switch positions. 

9-2 HP-IB INTERFACING 
