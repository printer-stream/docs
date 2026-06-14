NOTE: The receipt of something other than another parameter, a semicolon, or a colon will result in error 12 overwriting error 14. @ 

## [TERM] 

The terminator defaults to carriage return, CR, unless it is set by an ESC. M. 

## The Set Handshake Mode 1 Instruction, ESC ..H 

SHTML =6The set handshake mode 1 instruction, ESC. H, may be used with the enquire/acknowledge or Xon-Xoff handshake to establish parameters for the plotter’s communication format. ’ 

| USES 4 It establishes the data block size, the enquiry character, and the acknowledgment string when the computer requires that the parameters set in the ESC. M instruction be used in response to the enquiry character or Xon character. SYNTAX . H[ (<DEC>) ; (< ASC>) ; (KASC>(,...<ASC>)) ]: NGS Gea.H: See ESC. I default. Pe) =6The two instructions, ESC. H and ESC.I, are mutually exclusive. The parameter descriptions are the same for both instructions and are given under the ESC. I instruction. 

Handshake mode 1, established by this command, uses defaulted or specified parameters of the ESC.M and ESC.N commands when responding to the handshake enable or Xon trigger character. 

The parameters used with handshake mode 1, handshake mode 2, and output responses are shown in the following table. Choose the mode and use handshake mode 1 (ESC. H) or handshake mode 2 (ESC. I) depending on the requirements of your system. 

10-28 RS-232-C/CCITT V.24 INTERFACING 
