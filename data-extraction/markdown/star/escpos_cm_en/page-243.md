<!-- image -->

## &lt;Function	50&gt;	ESC	GS	)	B	pL	pH	fn	m		(fn	=	50)

Name

Set to print the string that matches in the text search

Code

ASCII

ESC

GS

)

B

pL

pH

fn

m

Hex.

1B

1D

29

42

pL

pH

fn

m

Decimal 27 29 41 66 pL pH fn m

Defined Region

pL = 2, pH = 0

fn = 50

m=0, 1, 2

Initial Value

Depends on setting registered in the non-volatile memory (At the time of shipment: m = 0)

Function

Sets the string print operation when strings match.

|   m | Set                                        |
|-----|--------------------------------------------|
|   0 | Prints the string                          |
|   1 | Does not print the string                  |
|   2 | Switches the string with a blank character |

No setting when the parameter is not a valid value.

This setting is applied to printer operations when this command is processed.

This setting is registered to non-volatile memory by the ESC GS ) B &lt;Function 80) command.

This command is ignored when the text search macro is running.

Disabled in Page Mode.
