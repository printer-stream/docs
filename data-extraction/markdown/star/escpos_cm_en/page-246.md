<!-- image -->

## &lt;Function	66&gt;	ESC	GS	)	B	pL	pH	fn	n	t	(fn	=	66)

Name

Define the text search macro

Code

ASCII ESC GS ) B pL pH fn n t

Hex. 1B 1D 29 42 pL pH fn n t

Decimal

27

29

41

66

pL

pH

fn

n

t

Defined Region

pL  = 3, pH  = 0

fn = 66

1 ≤ n ≤ 100

t  = 0, 1

Initial Value

Depends on setting registered in the non-volatile memory (At the time of shipment: Soon after cutting )

Function

Sets when to execute a text search macro when there is a match for text search string n.

|   t | Setting             |
|-----|---------------------|
|   0 | soon after cutting  |
|   1 | soon before cutting |

No setting when the parameter is not a valid value.

This setting is applied to printer operations when this command is processed.

This setting is registered to non-volatile memory by the ESC GS ) B &lt;Function 80) command.

This command is ignored when the text search macro is running.

Disabled in Page Mode.
