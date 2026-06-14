| 

2. Listeners — devices which receive information sent on the bus when they have been addressed. 

| 

3. Controllers — devices that can specify the talker and listeners for an information transfer. Controllers can be categorized as one of two types: 

   - e Active Controller — the current controlling device on the bus. Only one device can be the active controller at any time. 

| 

- e controlSystemofController the bus if it —is notthe theonlycurrentcontrolleractivethatcontroller.can takeAlthoughpriority each bus system can have only one system controller, the system 

- ; can have any number of devices capable of being the active controller. 

- A typical HP-IB system is shown below. 

**==> picture [330 x 126] intentionally omitted <==**

**----- Start of picture text -----**<br>
SYSTEM<br>CONTROLLER<br>SOURCE etn |<br>os<br>ef} mere<br>a2<br>VOLT- PRINTER * PLOTTER<br>METER<br>**----- End of picture text -----**<br>


## Message Concepts 

Devices which communicate along the interface bus are transferring quantities of information. The transfer of information can be from one device to another device, or from one device to more than one device. These quantities of information can easily be thought of as “messages.” 

In turn, the messages can be classified into 12 types. The list below gives the 12 message types for the HP-IB. 

1. The Data Message. This is the actual information which is sent from one talker to one or more listeners along the interface bus. 

2. The Trigger Message. This message causes the listening device(s) to perform a device-dependent action when addressed. 

3. The Clear Message. This message causes either the listening device(s) or all of the devices on the bus to return to their predefined device-dependent states. 

A-2 AN HP-IB OVERVIEW 
