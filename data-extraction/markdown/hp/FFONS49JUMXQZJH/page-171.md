## Parameter Usage in Plotter/ Computer Communication

|                          | WithHandshake Characters   | WithHandshake Characters   | with P10tte1' Output Commands   |
|--------------------------|----------------------------|----------------------------|---------------------------------|
| Parameter                | In Mode 1                  | In Mode2                   |                                 |
| turnaround delay         | yes                        | yes                        | yes                             |
| output trigger character | yes                        | no                         | yes                             |
| echo terminator          | yes                        | no                         | yes                             |
| output terminator        | yes                        | no                         | yes                             |
| output initiator*        | no                         | no                         | yes                             |
| intercharacter delay     | yes                        | yes                        | yes                             |

<!-- image -->

See ESC . I and ESC . N.

## The Set Handshake Mode2 Instruction, ESC . I

DESCWPTIUN The set handshake mode 2 instruction, ESC . I, may be used with the enquire/ acknowledge or Xon-Xoff handshake to establish parameters for the plotter's communication format.

It establishes the data block size, the enquiry character, and the acknowledgment string for the enquire/acknowledge handshake when the computer expects only the turnaround delay, and not the other parameters set by ESC . M, to be included in the response to the enquiry character. It sets the Xoff threshold level and the Xon trigger character for Xon-Xoff handshake. and

SYNTAX . I[(&lt;DEC&gt;) ; (&lt;ASC&gt;) -, (&lt;ASC&gt;(; . . .&lt;ASC&gt;))]: ]:

DEFAULT . I: (or . H1) Neither Xon-Xoffnor enquire/ acknowledge handshake is enabled. Block size is 80 bytes, and there is
