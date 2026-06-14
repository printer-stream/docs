**==> picture [359 x 161] intentionally omitted <==**

**----- Start of picture text -----**<br>
ODO YOU HAVE BUFFER SPACE FOR A 100-BYTE BLOCK OF DATA<br>“ENQ” (HANDSHAKE ENABLE)<br>THIS ENOS REQUEST, PLEASE ACKNOWLEDGE<br>Hos T ve te<br>COMPUTER DC1" {OUTPUT TRIGGER CHARACTER) PLOTTER<br>YES, THERE IS ROOM FOR 100 BYTES<br>_ 250 MS DELAYED “ACK” (HANDSHAKE STRING}<br>ECHO|<br>I THIS IS END OF MY MESSAGE Houenmeied<br>rian “CR” (OUTPUT TERMINATOR) [es<br>ECHO ! ~ “ACK” oo DATA<br>Lt _| — CLOSED<br>“LF” (ECHO TERMINATE CHARACTER) —<br>°<br>100-BYTE DATA BLOCK<br>**----- End of picture text -----**<br>


ENQ/ACK Handshake Protocol Example 2 

## Hardwire Handshake 

As the name implies, the hardwire handshake takes place in the hardware rather than the firmware or software. The plotter controls the data exchange sequence by setting the electrical voltage on pin 20 of the connector (CD line) to the computer to signal the computer when to send another block of data. If there is enough room in the plotter’s buffer to accept and store another block of data, the plotter sets the Data Terminal Ready, CD, line to a high state. If there is insufficient space, it sets the line low. By monitoring this line, the computer knows when it can or cannot safely transmit another block of data. 

The hardwire handshake mode is enabled at power on or by setting the Data Terminal Ready, CD, line control using the ESC . @ command. 

## RS-232-C Device Control Instructions 

Device control instructions establish the handshake protocol to be used by the 7470 plotter. All communications conform to the protocol established by these instructions. The instructions serve two purposes: to control the format by which data is transferred between the computer and the plotter (input/output operations), and to give the computer the ability to query and to receive information from the plotter. 

Each instruction’s name gives an immediate clue to its purpose: if “output” is the first word in the name of the instruction, the computer wants a response from the plotter. Otherwise, the instruction concerns the I/O functions. The word “set” in the title indicates the command establishes conditions under which subsequent I/O is to occur. 

10-22 RS-232-C/CCITT V.24 INTERFACING 
