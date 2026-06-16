<!-- image -->

## (3)	Set	Star	page	mode

This command sets the expansion starting position and rotation information for bar code data expansion.

## (4)	Print	Bar	code

This command prints bar codes based on the settings of (1) to (3).

## = Precautions on using these commands =

- The setting values for (1) to (3) are held unless any of the following operations are performed.
- Sending a new setting command
- Sending an initialize command (&lt;ESC&gt; @, /)
- Turning the power OFF
- When there is an error in sending a command with (2), the set data is cleared and the command itself is disabled.
- (4) is sent when necessary.
- Printing:
- When printing, position movement using specify absolute position, specify relative position, and align position are enabled.
- Upside down printing and 2-color printing are possible.
- Printed bar codes should always be checked in an actual use.

The following is an example showing the sending of the commands.

- (1) Set	bar	code	type

&lt;ESC&gt; &lt;GS&gt; 'y' 'S' '0' 1

Sets to model 1.

&lt;ESC&gt; &lt;GS&gt; 'y' 'S' '1' 0

Sets mistake correction level to L.

&lt;ESC&gt; &lt;GS&gt; 'y' 'S' '2' 3

Sets cell size to 3 dots.

- (2) Set	bar	code	data

• &lt;ESC&gt; &lt;GS&gt; 'y' 'D' '1' 0 20 0 '2005, January, 1 (SAT)' &lt;LF&gt; Sets bar code data (Data automatic analysis)

Sets bar code data (Data manual analysis)

$$• <ESC> <GS> 'y' 'D' '2' 9  1 4 0 '2005' ','$$

4 2 0 'Year' ','

1 1 0 '1' ','

4 2 0 'Month' ','

1 1 0 '1' ','

4 2 0 'Day' ','

4 2 0 '(' ','

2 3 0 'SAT' ','

4 2 0 ')' ','

- (3) Print	bar	code

$$<ESC> <GS> 'y' 'p' Print$$
