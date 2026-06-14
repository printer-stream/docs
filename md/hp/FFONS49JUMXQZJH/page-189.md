~ 

## AppendixA An HP-IB Overviewe 

The HP Interface Bus (HP-IB) provides an interconnecting channel for data transfer between devices on the HP-IB. 

The following list defines the terms and concepts used to describe HP-IB (bus) system operations. 

## HP-IB System Terms 

1. Addressing — the characters sent by a controlling device specifying which device sends information on the bus and which device(s) receives the information. 

2. Byte — a unit of information consisting of 8 binary digits (bits). 

3. Device — any unit that is compatible with the ANSI/IEEE 488-1978 Standard. 

4. Device Dependent — a response to information sent on the HP-IB that is characteristic of an individual device’s design, and may vary from device to device. 

5. Operator — the person that operates either the system or any device in the system. 

6. Polling — the process typically used by a controller to locate a device that needs to interact with the controller. There are two types of polling: 

   - ® Serial Poll — a method which obtains one byte of operational information about an individual device in the system. The process must be repeated for each device from which information is desired. 

   - ¢ Parallel Poll — a method for obtaining information about a group of devices simultaneously. 

## Interface Bus Concepts 

Devices which communicate along the interface bus can be classified into three basic categories. 

1. Talkers — devices which send information on the bus when they have been addressed. 

AN HP-IB OVERVIEW A-1 
