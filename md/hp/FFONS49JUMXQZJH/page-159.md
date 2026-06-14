- e Xon Trigger Character — This specifies the character string the plotter will use to signal the computer that there is sufficient space in the buffer to resume sending data. The DC1 character (decimal equivalent 17) is generally used for the Xon trigger. 

The following discussion of the four handshake methods includes the pertinent variables and identifies the commands which will establish their values. 

## Software Checking 

Software checking is a nonautomatic handshake method in which the user’s program repeatedly asks the plotter how many characters of empty space remain in the buffer. When the plotter response is bigger than the next block of data, the program will transmit the data block to the plotter. This method is inefficient in time-share environments. 

The advantage of software checking is that it is independent of hardware and operating system abilities required to implement other handshake modes; therefore, it usually makes software transportable between computer systems. The limitation of this method of handshaking is that it uses up computer time. 

To match the requirements of the computer system, these variables may be specified for the software checking handshake mode by using the appropriate command: 

- e Turnaround delay (ESC . M command) 

- © Output trigger character (ESC . M command) 

- e Echo terminate character (ESC . M command) 

- © Output initiator character (ESC . M command) 

- e Output terminator (ESC . M command) 

- ® Intercharacter delay (ESC . N command) 

RS-232-C/CCITT V.24 INTERFACING 10-17 
