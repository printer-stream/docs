[TERM]

NOTE:The receipt of something other than another parameter, a semicolon, or a colon will result in error 12 overwriting error 14. I

The terminator defaults to carriage return, CR,unless it is set by an ESC . M.

## The Set Handshake Mode1Instruction, ESC . H

DE3cRlP-'UN The set handshake mode 1 instruction, ESC . H, may be used with the enquire/ acknowledge or Xon-Xoff handshake to estab­ lish parameters for the p1otter'scommunication format. ,

EB It establishes the data block size,the enquiry character, and the acknowledgment string when the computer requires that the para­ meters set in the ESC . M instruction be used in response to the enquiry character or Xon character.

SYNTAX . H [ (&lt;DEC&gt;) ; (&lt;ASC&gt;) ; (&lt;ASC&gt;(; . . .&lt;ASC&gt;)) 1;

DEFAULT. H: SeeESC . I default.

EXPLANATIONThe two instructions, ESC. H and ESC. I, are mu­ tually exclusive. The parameter descriptions are the same for both instructions and are given under the ESC . I instruction.

Handshake mode 1, established by this command, uses defaulted or specified parameters of the ESC. M and ESC. N commands when responding to the handshake enable or Xontrigger character.

The parameters used with handshake mode 1,handshake mode 2, and output responses are shown in the following table. Choose the mode and use handshake mode 1 (ESC . H) or handshake mode 2 (ESC . 1) depending on the requirements of your system.
