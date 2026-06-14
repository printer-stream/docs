- e Enquiry Character — In some systems the computer sends an enquiry character to ask the plotter if it has room for a block of data, thereby initiating the handshake process. If Xon-Xoff handshake mode is to be established, a NULL character (decimal equivalent 0) must be specified as the enquiry character. If enquire/acknowledge is to be established, an ENQ character (decimal equivalent 5) or any other ASCII character besides the NULL is used. 

- e Immediate Response String — Certain system environments require an immediate response from the plotter acknowledging the enquiry from the computer. Systems of this type include a computer that transmits data to the plotter after a certain time interval but before receiving a go-ahead signal from the plotter. If the plotter’s buffer is full and the computer sends more data, the buffer will overflow. The immediate response string prevents this inadvertent tYansmission of data before the plotter is ready. It is transmitted by the plotter immediately after receipt of an enquiry character and tells the computer, “Wait, I am here and checking my buffer space.’ Computers frequently require a DC3 character (decimal equivalent 19) for the immediate response. 

- e Acknowledgment String — The acknowledgment string specifies the character or characters that the plotter will send to the computer when the plotter’s input buffer has room for another block of data. Computers frequently require that the ACK character (decimal equivalent 6) be used for the acknowledgment string. 

- e Data Block Size — This is the maximum size of each data block the computer will transmit to the plotter. 

- Data Terminal Ready (CD) Line Control — This variable sets the configuration of the plotter’s Data Terminal Ready control line (pin 20) to enable or disable the hardwire handshake mode. Pin 20 is held on (+12 V) if hardwire handshake is disabled. 

- ¢ Xoff Threshold Level — In the Xon-Xoff handshake mode this defines how many empty bytes remain in the buffer when the plotter sends the Xoff trigger character to the computer, telling it to stop sending data. 

- e Xoff Trigger Character — This specifies the character string the plotter will use to signal the computer to temporarily stop sending data while the plotter processes what it has already received. The DC3 character (decimal equivalent 19) is generally used for the Xoff trigger. 

10-16 RS-232-C/CCITT V.24 INTERFACING 
