ESC/P 2

ESC/P

9-Pin ESC/P

Use the ESC l command to set the left margin and the ESC Q command to set the right. The format of these commands is as follows:

ESC l m ESC Q m

The m parameter equals the number of characters from the left-most mechanically printable position, in the current character pitch.

The following commands affect the character pitch (see individual commands in the Command Summary for details):

ESC P Selects 1/10-inch character width (10 cpi)

ESC M Selects 1/12-inch character width (12 cpi)

ESC g Selects 1/15-inch character width (15 cpi)

ESC W 1 Doubles the current character width

ESC p 1 Selects proportional spacing. When setting the margins, the character width is considered to be 1/10 inch

ESC SP n Adds extra space between each character (n/180 inch for LQ characters and n/120 inch for draft characters on 24/48-pin printers; n/120 inch on 9-pin printers). The resulting character width is:

(current character width) = (previous character width) + (extra space)

SI Selects condensed printing, resulting in the following character widths:

1/17 inch if 10-cpi is currently selected 1/20 inch if 12-cpi is currently selected

ESC c Sets the character pitch to between 1/360 and 3 inches (available only on ESC/P 2 printers)

ESC X Sets pitch and point of scalable fonts (available only on ESC/P 2 printers).

## Note:

- Once the margins are set, changing the character width does not affect the margins.
