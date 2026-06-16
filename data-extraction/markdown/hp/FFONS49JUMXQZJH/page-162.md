maximum number of bytes sent by an output statement to allow room for the overshoot.

- Once the Xofftrigger character has been sent, when the amount of stored data drops to the Xon threshold level, the plotter sends the Xon trigger character to signal the computer to resume sending data. The Xon threshold level is automatically set at 128bytes. If the Xoffthreshold level is greater than 128,the Xon threshold is reset to send the Xon character when one more byte than required by the Xoffthreshold is available in the plotter's buffer. 5.
- Data is again stored in the buffer until all the data are transferred or until the Xoffthreshold level is exceeded again. 6.

The following conditions can be specified for the Xon-flXoff handshake mode to match the requirements of the computer system, by using the appropriate command:

- Xoffthreshold level (ESC . I command) ©
- Xontrigger character (ESC . I command) ©
- Xofftrigger character (ESC . N command) ©
- Intercharacter delay (ESC . N command) ©

The enquiry character (ESC . I command) must either be defaulted or specified as zero.

## Enquire/Acknowledge Handshake

With the enquire/acknowledge handshake, the computer's operating system or application program initiates the data exchange process by querying the plotter about the availability of buffer space. The format of the exchange is dependent upon the requirements of the computer. The following conditions can be specified for the enquire/ acknowledge handshake modeby using the appropriate command:

- Turnaround delay (ESC . M command) ©
- Output trigger character (ESC . M command) ©
- Echo terminate character (ESC . M command) ©
- Output initiator character (ESC. Mcommand) ©
- Output terminator (ESC . M command) ®
- Intercharacter delay (ESC . N command) ©
- Immediate response string (ESC . N command) ©
- Data block size (ESC . I or ESC . H command) ©
