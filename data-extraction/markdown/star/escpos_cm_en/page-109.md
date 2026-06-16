<!-- image -->

## &lt;Function	066&gt;	GS	(	k	pL	pH	m	cn	n		(cn=48,	fn=66)

Name

Set PDF417 number of symbol levels

Code

ASCII GS

( k  pL  pH m cn fn n

Hex. 1D   28  6B  pL  pH  m cn fn n

Decimal   29   40  107  pL  pH m cn fn n

Defined Region

pL = 3, pH = 0

cn = 48, fn = 66

n =  0, 3 ≤ n ≤ 90

Initial Value

n = 0

Function

Sets the number of levels of the PDF417 symbols.

- When n = 0, sets the automatic process.

- When n≠0, specifies the number of positions of symbols to n levels.

Details

The setting of this function affects processes of Functions 081 and 082.

When automatic processing is specified (n = 0), the maximum row number in the data region is 90.

The number of positions when automatic processing is specified (n = 0), calculates based on the current print region, when processing Functions 081, and 082, and module width (Function 068).

This setting is valid until ESC @ is executed, the printer is reset or the power is turned off.

Reference

GS ( k Function 081, 082, 068, ESC @
