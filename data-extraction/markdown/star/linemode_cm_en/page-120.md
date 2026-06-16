<!-- image -->

## ESC SYN 3 n

[Name] [Code]

Acquire presenter paper counter

ASCII

ESC  SYN 3 n

Hex.

1B 16 33 n

Decimal

27 22 51 n

[Defined Area]

[Initial Value] [Function]

n = 0, 1

n = 48, 49 ('0',  '1')

- - -

Acquires presenter paper counter.

This command is ignored when a presenter is not connected.

Counter can count to 0xFFFFFFFF sheets.

Counter is cleared to zero when the following conditions are met.

- At a printer reset
- At the &lt;CAN&gt; command
- At the &lt;ESC&gt; &lt;SYN&gt; 4 n command

The paper counter using this command sends the counter value at the time this command is processed.

The counter is counted up when paper is completely recovered or when pulled out.

The counter counts from when the power is turned ON, excluding the following.

- When paper is discharged because of an error
- When printing using self-print
- When paper in the presenter is discharged when the power is turned ON

| N         | Counter                         |
|-----------|---------------------------------|
| n = 0, 48 | Acquires paper reel counter     |
| n = 1, 49 | Acquires paper recovery counter |

&lt;Counter transmission format from printer:  When using the paper reel counter&gt;

Printer transmission:  ESC SYN  3  n  c1  c2  c3  c4

Reel counter:   c4 + (c3 x 256) + (c2 x 256 x 256) + (c1 x 256 x 256 x256)

-----------------------------------------------------------------------------
