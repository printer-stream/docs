<!-- image -->

The settings above are set individually, so the errors described below may be generated even if there is no particular problem in those settings.  In such case, if the bar code is generated the (3) print command (&lt;ESC&gt; &lt;GS&gt; 'x' 'P') is ignored.

- Error is generated when generating a bar code, due to the combination of the bar code setting commands.
- The bar code data that is generated exceeds the printable size of PDF417.
- Print data exceeds the currently set print region.

It is recommended to use (4) Bar code expansion information acquisition (&lt;ESC&gt; &lt;GS&gt; 'x' 'I') as a means for checking these errors prior to printing.

## (2) Bar code data setting command

This command sets the print data of the bar code.

## (3) Bar code print command

This command prints the bar code according to the settings of (1) and (2).

## (4) Bar code expansion information acquisition

This command checks whether it is possible to print the bar code according to the settings of (1) and (2).

- Precautions for use of commands -
- Unless the following operations are performed, the setting values are maintained for (1) and (2).
- Sending of new setting commands
- Sending an initializing command (&lt;ESC&gt; @, &lt;CAN&gt;)
- The power is turned off
- Sending (3) and (4) when needed
- Printing
-  When printing, position shifting according to the horizontal tab, absolute position specification, relative position specification, and position alignment is valid.
- Upside-down printing and two-color printing are possible.
- When a bar code is printed, always verify it by actual use.

Send the command transmission example last.

1. Bar code type setting
2. Bar code data setting

&lt;ESC&gt; &lt;GS&gt; 'x' 'S' '0' 0 2 3:

Sets the bar code size to USE\_LIMITS = 2:3

&lt;ESC&gt; &lt;GS&gt; 'x' 'S' '1' 3:

Sets ECC level to 3

&lt;ESC&gt; &lt;GS&gt; 'x' 'S' '2' 3:

Sets the module X direction size to 3 dots

&lt;ESC&gt; &lt;GS&gt; 'x' 'S' '3' 3:

Sets module aspect ratio to 3

&lt;ESC&gt; &lt;GS&gt; 'x' 'D' 10 0 '0123456789':

## 3. Printing bar code

To verify whether printing is possible with the current settings, check the bar code expansion information

&lt;ESC&gt; &lt;GS&gt; 'x' 'I':

&lt;ESC&gt; &lt;GS&gt; 'x' 'P':

Bar code expansion information check

Print

-----------------------------------------------------------------------------

Sets the bar code data
