e Enquiry character (ESC . I or ESC. H command) 

e Acknowledgment string (ESC . I or ESC . H command) 

In its simplest form, the data exchange looks like this: 

**==> picture [327 x 85] intentionally omitted <==**

**----- Start of picture text -----**<br>
DBO YOU HAVE BUFFER SPACE FOR A DATA BLOCK?<br>YES, THERE IS ROOM IN MY BUFFER<br>COMPUTER PLOTTER<br>“ACK”<br>:<br>**----- End of picture text -----**<br>


ENQ/ACK Handshake Protocol Example 1 

In a more complex form, the communication might look like the following example, where the two commands - M250;17;10;138: and G&@ . H100;5;6: have been sent to specify the variables as: 

turnaround delay = 250 ms 

output trigger character = ASCII character DC1 (decimal equivalent 17) 

echo terminate character = ASCII character LF (decimal equivalent 10) 

output terminator = ASCII character CR (decimal equivalent 13) data block size = 100 bytes 

enquiry character = ASCII character ENQ (decimal equivalent 5) acknowledgment string = ASCII character ACK (decimal equivalent 6) 

RS-232-C CCITT/V.24 INTERFACING 10-21 
