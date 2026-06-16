<!-- image -->

## &lt;Function	64&gt;	ESC	GS	)	B	pL	pH	fn	m	k	d1…dk	(fn	=	64)

Name

Define the text search string

Code

ASCII

ESC

GS

)

B

pL

pH

fn

n

m

k

d1

...

dk

Hex.

1B

1D

29

42

pL

pH

fn

n

m

k

d1

...

dk

Decimal

27

29

41

66

pL

pH

fn

n

m

k

d1

...

dk

Defined Region

4 ≤ (pL + pH x 256) ≤ 65535  (0 ≤ fn = 64

pL ≤ 255, 0 ≤ pH ≤ 255)

1 ≤ n ≤ 100

1 ≤ m ≤ 100

0 ≤ k ≤ 32

32 ≤ d ≤ 255

Initial Value

Depends on setting registered in the non-volatile memory (At the time of shipment: no string definition)

Function

Defines the text search string for number n.

If the text search string for number n is already defined, it is overwritten.

M specifies the text search macro number to run.

K specifies the size of the defined data in bytes.

d specifies the defined data.

When the parameter has an invalid value, no definition.

This definition is applied to printer operations when this command is processed.

This definition is registered to non-volatile memory by the ESC GS ) B &lt;Function 80) command.

This command is ignored when the text search macro is running.

Disabled in Page Mode.
