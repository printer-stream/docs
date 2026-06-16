## OC The Output Commanded Position and Pen Status Instruction

0C (;)

Purpose:

Used to output the pen position and status at time of command.

Response:

X,Y,P [TERM] -decimal numbers,* in ASCII.

X,Y --32 768 to 32 767.

P -0, pen up or 1, pen down.

Plotter units unless scaling in effect;then in user units.

## OD The Output Digitized Point and Pen Status Instruction

OD (;)

Purpose:

Used to output the physical pen position and status for the last digitized point.

Response:

X,/Y,P[TERM] -integers, in ASCII.

X,Y-In plotter units, within mechanical limits.

P -0, pen up or 1, pen down.

## OE The Output Error Instruction

OE (;)

Purpose:

Used to output the last HP-GL error.

Response:

error number [TERM] - a positive ASCII integer, 0 through 8, excluding 4.

## OF The Output Factors Instruction

0F (;)

Response:

40, 40 [TERM] -integers, in ASCII.

## OI The Output Identification Instruction

01 (;&gt;

Purpose:

Used to output the plotter's identification.

Response:

7470A [TERM] -ASCII string.

*If you have an HP-IB or RS-232-C plotter that has a serial prefix number lower than 2308A,OC parameters are output as integers. For more information, refer to the explanation ofthe OCinstruction on page 7-4.

## B-6 INSTRUCTION SYNTAX

Page7-6

Page 7-7

Page7-5

Page6-3

## Page7-4
