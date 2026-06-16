|   Bit No. | Logic State   | Description                                                                                    |
|-----------|---------------|------------------------------------------------------------------------------------------------|
|         0 | 0             | Set and hold line high (disable hard­ wire handshake).                                         |
|           | 1             | Enable hardwire handshake mode.*                                                               |
|         1 | X             | Ignored.                                                                                       |
|         2 | 0             | Establish monitor mode 0 (all bytes displayed on terminal as they are parsed from the buffer). |
|           | 1             | Establish monitor mode 1 (all bytes displayed as they are received).                           |
|           |               | Disable monitor mode. H Enable the monitor mode established                                    |
|           | 1             | by bit 2.                                                                                      |

EXAMPLE . @;13: will establish monitor mode 1 where all bytes are displayed on the terminal as they are received by the plotter.

## The Output Buffer Space Instruction, ESC.B

DESCRIPHUN The output buffer space instruction, ESC . B, outputs the plotter's available buffer space.

IIEE This command is used in a software checking handshake to interrogate the plotter regarding available buffer space.

SYNTAX , B

EXPLANATION No parameters are used.

## RESPONSE

&lt;DEC&gt;

[TERM]

The plotter's response is a decimal number in the range 0 to 255, and represents the number of bytes of buffer space currently available for storing graphic instructions sent from the computer.

This decimal number is followedby the output termina­ tor which defaults to carriage return, CR, or is as set by ESC . M.
