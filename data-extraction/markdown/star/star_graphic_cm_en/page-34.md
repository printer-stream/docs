<!-- image -->

Rev. 2.31

## ESC * r Y n NUL

[Name]

Moving position in the vertical direction (line break of a specified dot)

[Code]

ASCII

ESC * r Y n NUL

Hex

1B 2A 72 59 n 00

Decimal

27

42

114

89

n

0

[Defined Area]  ---

[Initial Value]

[Function]

---

Performs position movement of the raster vertical direction.

With this command it will move the position of n dot.

If the specified movement makes you go over the page

- ・ If the page length settings are in continuous print mode, and the n dot is the maximum page length (see ESC * r P n NUL command)
- ・ Page length set at the specified page length mode, and the n dot exceeds the specified page length to do this, you print the data up to the end page, and the section that is overflow will be treated as data from the beginning of the next page.

nI is a decimal notation using ASCII characters (up to 255 digits)

## ESC FF NUL

[Name]

Execute FF mode

[Code]

ASCII

ESC FF NUL

Hex

1B

0C

00

Decimal 27 12 0

[Defined Area]  ---

[Initial Value]

---

[Function]

Executes FF mode.

It runs the operation specified in FF mode setting command (ESC * r F n NUL).

If raster data exists in the image buffer for raster mode, FF mode is implemented after printing.

If raster data does not exist in the image buffer for raster mode, this command is ignored.

(TSP100IIU) if the print paper length to be cut is less than 24mm, then empty feed is automatically added before cutting so that the printing paper length is 24mm.

## ESC FF EOT

[Name]

Execute EOT mode

[Code]

ASCII

ESC FF EOT

Hex

1B 0C 04

Decimal

27 12 4

[Defined Area]  ---

[Initial Value]

---

[Function]

Executes EOT mode.

It runs the operation specified in EOT mode setting command (ESC * r E n NUL).

If raster data exists in the image buffer for raster mode, EOT mode is implemented after printing.

If raster data does not exist in the image buffer for raster mode, this command is ignored.

(TSP100IIU) if the print paper length to be cut is less than 24mm, then empty feed is automatically added before cutting so that the printing paper length is 24mm.

--------------------------------------------------------------------------------------
