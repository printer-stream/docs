important for you to be aware of the HP-IB functions implemented on each device in your HP-IB system to ensure the operational compati­ bility of the system.

## The HP Interface Bus

## HP-IB Lines and

## Operations

The HP Interface Bus transfers data and commands between the components of an instrumentation system on 16signal lines. The interface functions for each system component are performed , , within the component so only passive cabling is needed to connect the systems. The cables connect all instruments, controllers, and other components of the system in parallel to the signal lines.

\_ . The eight Data I/O lines (DIO1 through DIO8) are reserved for the transfer of data and other messages in a byte-serial, bit-paral1el manner. Data and message transfer is asynchronous, coordinated by the three handshake lines: Data Valid (DAV),Not Ready For Data (NRFD), and Not Data Accepted (NDAC).The other five lines are for management of bus activity. See the figure on the right.

HP-IB Signal Lines

<!-- image -->

Devices connected to the bus may be talkers, listeners, or controllers. The controller dictates the role of each of the other devices by setting the ATN (attention) line true and sending talk or listen addresses on the data lines. Addresses are set into each device at the time of system configuration either by switches built into the device or by jumpers on

V
