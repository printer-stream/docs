<!-- image -->

## &lt;Function	367&gt;	GS	(	k	pL	pH	cn	fn	n	(cn=51,	fn=67)

Name

2D GS1 DataBar: Set module siz

Code

ASCII GS ( k  pL  pH cn fn n

Hex. 1D   28  6B  pL  pH

cn fn n

Decimal   29   40  107  pL  pH  cn fn n

Defined Region

pL = 3, pH = 0

cn = 51

fn = 67

2 ≤ n ≤ 8

Initial Value

n = 2

Function

The width of one module of the 2D GS1 DataBar is set to n dots.

Note

The setting for this function affects the processing of function 381.

This setting is enabled until ESC@ is executed, the printer is reset, or the power is turned off.

The set unit is 1 dot.

The width is set as 0.125 mm (1/203 inches).

Reference

GS ( k Function 381, ESC @

## &lt;Function	371&gt;	GS	(	k	pL	pH	cn	fn	nL	nH	(cn=51,	fn=71)

Name

2D GS1 DataBar: Set The maximum width of the 2D GS1DataBar Expanded Stacked

Code

ASCII GS ( k  pL  pH cn fn nL nH

Hex. 1D   28  6B  pL  pH cn fn nL nH

Decimal   29   40  107  pL  pH  cn fn nL nH

Defined Region

pL = 4, pH = 0

cn = 51

fn = 71

106 ≤ n ≤ 3952

Initial Value

(nL + nH x 256) = 141 (nL = 141, nH = 0)

Function

The maximum width of the 2D GS1DataBar Expanded Stacked is set to n dots.

Note

The setting for this function affects the processing of function 381.

This setting is enabled until ESC@ is executed, the printer is reset, or the power is turned off.

The set unit is 1 dot.

The width is set as 0.125 mm (1/203 inches).

Reference

GS ( k Function 381, ESC @
