## Set Output Mode

Page10-33

. M [(&lt;DEC&gt;) ; (&lt;ASC&gt;) ; (&lt;ASC&gt;) ; (&lt;ASC&gt;( ; (&lt;ASC&gt;)); (&lt;ASC&gt;) ] : ;

Purpose:

Sets parameters for output.

Parameters:

&lt;DEC&gt; -Turnaround delay, 0-54 612.

&lt;ASC&gt; -Output trigger character, ASCII 0-127.

&lt;ASC&gt; -Echo terminator character, ASCII 0-127.

&lt;ASC&gt; . . . &lt;ASC&gt; -1or 2 output terminators, ASCII 0-127,0 terminates string.

&lt;ASC&gt; -Output initiator character, ASCII 0-127.

## Set Extended Output and Handshake Mode Page10-3

$$. N [(<DEC>) ;(<ASC>(; ... <ASC>))l:$$

Purpose:

Establishes extended parameters for any output command.

Parameters:

&lt;DEC&gt; -Delay between output characters, 0-54 612.

&lt;ASC&gt; . . . &lt;ASC&gt; -Immediate response string of 1 to 10 characters. ASCII 0-127, 0 terminates string; or Xoff trigger characters.

## Output Extended Status .0

Page10-3

Purpose:

Outputs the decimal equivalent value of a 16-bitimmediate status word.

Response:

&lt;DEC&gt; [TERM] -a value 40 or less.

## Reset Handshake .R

Purpose:

Page10-40

Resets the handshake to its default value. It is the same as sending the commands ESC . @, ESC . H , ESC . I , ESC . M , and ESC . N without parameters.
