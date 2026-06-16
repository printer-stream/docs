<!-- image -->

## &lt;Function	49&gt;	ESC	GS	)	B	pL	pH	fn	m		(fn	=	49)

Name

Set the number of times to run the text search macro

Code

ASCII ESC GS ) B pL pH fn m

Hex. 1B 1D 29 42 pL pH fn m

Decimal 27 29 41 66 pL pH fn m

Defined Region

pL = 2, pH = 0

fn = 49

m=0, 1

Initial Value

Depends on setting registered in the non-volatile memory (At the time of shipment: m = 0)

Function

Sets the number of times to run the text search macro when the strings match.

|   m | Set                                       |
|-----|-------------------------------------------|
|   0 | Run one time                              |
|   1 | Run for the number of times strings match |

No setting when the parameter is not a valid value.

This setting is applied to printer operations when this command is processed.

This setting is registered to non-volatile memory by the ESC GS ) B &lt;Function 80) command.

This command is ignored when the text search macro is running.

Disabled in Page Mode.
