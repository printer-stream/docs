<!-- image -->

## &lt;Function	381&gt;	GS	(	k	pL	pH	cn	fn	m	(cn=51,	fn=81)

Name

2D GS1 DataBar: Print symbol data of symbol saving region

Code

ASCII GS ( k  pL  pH cn fn m

Hex. 1D   28  6B  pL  pH cn fn m

Decimal   29   40  107  pL  pH  cn fn m

Defined Region

pL = 3 , pH = 0

cn = 51

fn = 81

m = 48

Function

Executes encoding and printing of the symbol data stored in the symbol saving region by GS ( k function 380.

Note

The user must secure the quiet zone.

Reference

GS ( k Function 380

Function

This command prints bar code data or deploys it to the image buffer.

This command is ignored when one of the following errors occurs:

- Error that occurs when the bar code is generated due to the combination of each barcode setting command.

- When the generated bar code data exceeds the printable size for the GS1 DataBar.
- When the print data exceeds the current set print area.

Make sure you check the printed bar code before actual use.

## For standard mode:

- If unprinted data still exists in the line buffer, the buffered data is printed out, the command is executed, and then the bar code is   printed. Therefore, you cannot print mixed data (characters, bit images, bar codes) on the same line.

## For page mode:

- This command only deploys bar code data to the image buffer.
