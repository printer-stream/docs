no enquiry character or acknowledgment string. If, however, the computer is configured to send an ENQ anytime it is ready to send data to the plotter, the plotter will automatically respond with ACK when it receives ENQ. This “dummy handshake” is not dependent upon available buffer space and does not protect against buffer overflow. 

The two instructions, ESC.I and ESC. H, are mutually exclusive. With handshake mode 2, the only parameter of the ESC. M command used when responding to the enquiry or Xon trigger character is the turnaround delay. Refer to the chart under the ESC . H instruction to see which parameters are used in various plotter output situations. Choose your mode using ESC. I or ESC. H, depending on the requirements of your system. 

The parameters for both ESC. H and ESC .I are the same and are described below, first as interpreted for the enquire/acknowledge handshake and then as interpreted for the Xon-Xoff handshake. 

- For Enquire/Acknowledge Handshake <DEC> This first parameter specifies the block size; it is evaluated modulo 256. Default block size set when the parameter is omitted is 80 bytes. 

   - <ASC> This parameter sets the enquiry character. The parameter may be the decimal equivalent of any ASCII character in the range 0 to 127. If the parameter is omitted, it assumes the default value 0 (NULL character) disabling enquire/acknowledge handshake. Any value other than 0 enables enquire/acknowledge handshake. However, the value 5 (enquire character, ENQ) is generally used. 

   - <ASC>...<ASC> This is a list of 1 to 10 parameters, separated by semicolons, which specify the acknowledgment string. Decimal equivalents of ASCII characters 0 to 127 are 

   - valid. The value 0 is not transmitted and will terminate the string. The value 6 (acknowledge character, ACK) is generally used. If the parameter is omitted, it assumes its default value and no characters are sent. 

## For Xon-Xoff Handshake 

- <DEC> This first parameter sets the Xoff threshold level by specifying the number of empty bytes remaining in the buffer when the Xoff character is to be sent. The practical range is 10 to 254. If the Xoff parameter is specified to be greater than 128 (half the buffer size), the Xon threshold level will be reset (from its automatic setting of half the buffer size) so that the Xon character will be sent when one byte more than the Xoff level is available. 

- 10-30 RS-232-C/CCITT V.24 INTERFACING 
