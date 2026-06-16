## HP-IB Implementation on the 7470

The HP-IB conforms to ANSI/IEEE 488-1978specifications, and direct interconnection of the HP-IB is via a connector on the rear panel.

The HP-IB functions implemented in the 7470 are as follows:

1. Source Handshake (SH1)
2. Acceptor Handshake (AH1) Talker (T2) . . won
3. Listener (L2) . fF
4. Service Request (SR1) .
5. No Remote Local (RLO) .
6. Parallel Poll (PPOif lon; PP2 if addr &lt;8; PPOotherwise) .
7. Device Clear (DC1)
8. N0 Device Trigger (DTO) .

omonti

- No Controller (C0) 0-' $3.©° .*'S3.°'t'.° .N'

## Interface Switches and Controls

The 7470 plotter functions in either of two modes, addressable mode and listen-only mode. In addressable mode, the plotter can function as a talker or as a listener depending on the instructions it receives from the controller. In listen-only mode, it can only listen and it hears all activity on the bus.

## Addressingthe Plotter

Rear panel switches provide for selection of the plotter address or listen­ only mode. Each HP-IB interface can have as many as 15 devices con­ nected to it, set to different specific address codes. The plotter can be set to any one of 31 HP-IBaddresses, ranging from 0 through 30. Each address can be selected by setting the switches on the rear panel to the appropriate binary bit positions for the particular address value desired. The address selected establishes the 7470'sdevice address. When using the plotter with an HP desktop computer, do not use 21 which is reserved for the desktop computer's address. When not using an HP desktop computer, be sure the computer and plotter do not have the same address. (Refer to the documentation for your computer.) Address 31 is used to set the plotter to listen-only mode.

The plotter is set to an address code of 05 at the factory. This corres­ ponds to a listen character of % and a talk character of E. Check the following figure for the factory-set address switch positions.
