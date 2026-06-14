important for you to be aware of the HP-IB functions implemented on each device in your HP-IB system to ensure the operational compatibility of the system. 

**==> picture [360 x 415] intentionally omitted <==**

**----- Start of picture text -----**<br>
The HP Interface Bus<br>HP-IB Lines and<br>Operations<br>The HP Interface Bus trans- DEVICE A ney einen,<br>fers data and commands be- pole tore =i= M-+——ines)<br>tween the components of an control HHH p<br>instrumentation system on (eg. Ee++4++4~4<br>16 signal lines. The interface calculator) [TET<br>functions for each system TELE LH<br>component are performed Data Byte<br>withinonly passivethe componentcabling sois ceeand listen.  =iFT (il TransterCont<br>needed to connect the sys- eg. FER { )<br>tems. The cables connect all multimeter) p+ t+ 1+<br>instruments,other componentscontrollers, of the and sys- TL penera.<br>lines.tem in parallel to the signal OnlyDEVICE able C aT NA Management<br>. . to [14 i)<br>The listen Gee: )<br>(DIO1eightthroughData I/ODIO8)linesare (e.g...generator) signal =H)PH||<br>reservedof data andfor otherthe messagestransfer EEL<br>inmanner.a byte-serial, Data andbit-parallel message DEVICE D sy=i<br>transfer is asynchronous, ony we EET<br>coordinated by the three leg countenf EEE<br>handshake lines: Data Valid po }o10<br>(DAV), Not Ready For Data wav.<br>(NRFD), and Not Data NREe<br>Accepted (NDAC). The other IFC<br>five lines are for manage- ary<br>ment of bus activity. See the REN<br>figure on the right.<br>**----- End of picture text -----**<br>


## HP-IB Signal Lines 

Devices connected to the bus may be talkers, listeners, or controllers. The controller dictates the role of each of the other devices by setting the ATN (attention) line true and sending talk or listen addresses on the data lines. Addresses are set into each device at the time of system configuration either by switches built into the device or by jumpers on 

A-4 AN HP-IB OVERVIEW 
