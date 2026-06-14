Rev.2.52 

## **1. INTERFACE CONFIGURATION 1-1 RS-232 Serial Interface 1-1-1 Specifications  (Conforming to RS-232)** 

Data transmission method Serial Synch method Start-Stop synchronization method Handshake DTR/DSR/XON/XOFF Signal level MARK =  -3v to -15v   Logic ’1’/OFF SPACEK =  +3v to +15v   Logic ’0’/ON Baud rates 2400, 4800, 9600, 19200, 38400, 57,600, 115,200 bps Bit length 7, 8 bits Parity None, odd, even Stop bit: 1 bit  (Fixed) Connector D-SUB 25  (Male)/D-SUB 9  (Male) 

Note: Handshake, bit length, baud rates and parity settings are set by the DIP switches or the memory switches. 

## **1-1-2 Switching Between Online and Offline** 

This printer does not have a switch to go between online and offline.  The following conditions are required to go offline. 

- The time after initializing the mechanism when turning on the power or causing a reset by the interface until communication is possible 

- When executing a self-test • When the cover is open 

- When printing has stopped because there is no paper 

- (When the roll paper end sensor detects that paper is out, or the roll paper near end sensor detects that paper is out using ESCc4, or paper is out when the print stop is enabled.) 

- When waiting to switch at macro execution 

- While there is a temporary error in the power voltage 

- When there is an error 

ESC/POS Command Specifications 

9 
