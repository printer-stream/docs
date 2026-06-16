<!-- image -->

The following is an example showing the sending of the commands.

- (1) Set bar code type
- (2) Set bar code data

&lt;ESC&gt; &lt;GS&gt; 'y' 'S' '0' 1

Sets to model 1.

&lt;ESC&gt; &lt;GS&gt; 'y' 'S' '1' 0

Sets mistake correction level to L.

&lt;ESC&gt; &lt;GS&gt; 'y' 'S' '2' 3

Sets cell size to 3 dots.

· &lt;ESC&gt; &lt;GS&gt; 'y' 'D' '1' 0 20 0

'2005, January, 1 (SAT)' &lt;LF&gt;

Sets bar code data (Data automatic analysis)

Sets bar code data (Data manual analysis)

<!-- formula-not-decoded -->

## (3) Print bar code

To verify whether to print with the current settings, check the bar code expansion information.

&lt;ESC&gt; &lt;GS&gt; 'y' 'I'

Check bar code expansion information

&lt;ESC&gt; &lt;GS&gt; 'y' 'p'

Print

-----------------------------------------------------------------------------
