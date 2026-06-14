maximum number of bytes sent by an output statement to allow room for the overshoot. 

5. Once the Xoff trigger character has been sent, when the amount of stored data drops to the Xon threshold level, the plotter sends the Xon trigger character to signal the computer to resume sending data. The Xon threshold level is.automatically set at 128 bytes. If the Xoff threshold level is greater than 128, the Xon threshold is reset to send the Xon character when one more byte than required by the Xoff threshold is available in the plotter’s buffer. 

6. Data is again stored in the buffer until all the data are transferred or until the Xoff threshold level is exceeded again. 

The following conditions can be specified for the Xon-Xoff handshake mode to match the requirements of the computer system, by using the appropriate command: 

- ® Xoff threshold level (ESC . I command) 

- ® Xon trigger character (ESC . I command) © Xoff trigger character (ESC . N command) e Intercharacter delay (ESC . N command) The enquiry character (ESC . I command) must either be defaulted or specified as zero. 

## Enquire/Acknowledge Handshake 

- With the enquire/acknowledge handshake, the computer’s operating system or application program initiates the data exchange process by querying the plotter about the availability of buffer space. The format of the exchange is dependent upon the requirements of the computer. The following conditions can be specified for the enquire/acknowledge handshake mode by using the appropriate command: * Turnaround delay (ESC . M command) © Output trigger character (ESC . M command) e Echo terminate character (ESC . M command) e Output initiator character (ESC . M command) ® Output terminator (ESC . M command) @ Intercharacter delay (ESC . N command) ¢ Immediate response string (ESC . N command) 

- e Data block size (ESC . I or ESC. H command) 

10-20 RS-232-C/CCITT V.24 INTERFACING 
