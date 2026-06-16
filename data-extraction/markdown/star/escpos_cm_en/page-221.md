<!-- image -->

= ESC/POS Page Mode = (1) Specify page mode &lt;ESC&gt; 'L': Select page mode

## (2) Set bar code type

&lt;ESC&gt; &lt;GS&gt; 'x' 'S' '0' 0 2 3: Set bar code size to USE LIMITS = 2:3 &lt;ESC&gt; &lt;GS&gt; 'x' 'S' '1' 3: Set ECC level to 3 &lt;ESC&gt; &lt;GS&gt; 'x' 'S' '2' 3: Set module X direction size to 3

&lt;ESC&gt; &lt;GS&gt; 'x' 'S' '3' 3: Set module aspect ratio to 3

(3) Set bar code data

&lt;ESC&gt; &lt;GS&gt; 'x' 'D' 10 0 '0123456789': Select bar code data

Check the bar code expansion information to check whether to print using the current settings. &lt;ESC&gt; &lt;GS&gt; 'x' 'I': Check bar code expansion information &lt;ESC&gt; &lt;GS&gt; 'x' 'P': Expand bar code

Print

(4) Print bar code &lt;ESC&gt; &lt;FF&gt;:
