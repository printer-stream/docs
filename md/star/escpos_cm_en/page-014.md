Rev.2.52 

## **1-2 Bi-directional Parallel Interface (IEEE1284) 1-2-1 Compatibility Mode (Host – Printer Communications: Conforms to Centronix)** 

## 1. General Description 

The Compatibility Mode is a mode that uses the Centronix interface as standard, which is widely in use. 

2. Specifications 

Data transmission method: 8 Bit Parallel Synch method: According to externally supplied nStrobe signal Handshake: According nAck signals and Busy signals Signal level: All signals are TTL compatible 

## 3. Switching Between Online and Offline 

This printer does not have a switch to go between online and offline.  The following conditions are required to go offline. 

- The time after initializing the mechanism when turning on the power or causing a reset by the interface until communication is possible 

- When executing a self-test 

- When the cover is open 

- When the paper is out and printing has stopped (paper out selected by ESCc4) 

- When waiting to switch at macro execution 

- When errors occur 

## **1-2-2 Reverse Mode (Printer to Host Communications)** 

Status data transfer from the printer to the host is performed in either Nibble or Byte Mode. 

## **General Description** 

Data transmissions from asynch printers controlled by the host are regulated.  Nibble Mode data transmissions use an existing control line to transmit data 4 bits (Nibble) at a time.  The Byte Mode uses bidirectional communications to transfer 8 bits of data lines.  In either case, communications are in half-duplex because it is not possible to execute both simultaneously with the Compatibility Mode. 

ESC/POS Command Specifications 

14 
