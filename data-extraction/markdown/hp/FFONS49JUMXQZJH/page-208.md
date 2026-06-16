## RS-232-CInstruction Syntax

This section lists the formal syntax for each RS-232-Cdevice control instruction in alphabetical order of the escape sequence. Refer to the indicated page for details.

## Plotter On

. ( or . Y .( or .Y

Purpose:

Places the plotter in a pr0grammed-0nstate.

## Plotter Off

. ) or ESC . Z -) Z

Purpose:

Places the plotter in a programmed-off state.

## Set Plotter Configuration

Page10-24

Page10-24

Page10-25

. @ [(&lt;DEC&gt;) ; (&lt;ASC&gt;) ]; ]:

Purpose:

Enables or disables hardwire handshake mode.

Parameters:

&lt;DEC&gt; -Ignored.

&lt;ASC&gt; -Data Terminal Ready (CD)line control. ASCII decimal equivalent of 4-bit word (0 to 15).

## Output Buffer Space

. B .B

Purpose:

Outputs the number of byte spaces currently available for data in the buffer.

Response:

&lt;DEC&gt; [TERM] -Oto 255.

## Output Extended Error

. E .E

Purpose:

Outputs a decimal code to identify the type of RS-232-C related error that occurred.

Response:

&lt;DEC&gt; [TERM] -0, no error, or 10 - 16.

Page10-27

Page10-26
