## The Output Actual Position and Pen Status Instruction, OA

UESCWPTIONThe output actual position and pen status instruction, OA, is used to output the X- and Y-coordinates and pen status (up or down) associated with the actual pen position.

USES This instruction can be used to determine the pen's current position in plotter units. Youmight use that information to position a label or figure, or determine the parameters of some desired window.

SYNTAX OA

(terminator)

EXPLANAHUN Output is always in plotter units.

No parameters are used. The instruction will execute even if no terminator is received.

The pen position and status are output to the computer as integers in ASCII in the form:

## X,Y,P [TERM]

where Xis always the X-coordinate in plotter units, Yis always the Y-coordinate in plotter units, P is the pen status (0 = pen up, 1 = pen down), and [TERM]is the output terminator for the interface installed.

The ranges of the X- and Y-coordinates are the current mechanical limits determined by the setting of the paper switch.

US

A4

0&lt;X&lt; 10300

O&lt;X&lt; 10900

0&lt;Y&lt;7650

O&lt;Y&lt;765O

N0 positive sign is output.

i
