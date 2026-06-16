<!-- image -->

## ESC % n

Name

Specify/cancel download character set

Code

ASCII ESC % n

Hex.

1B 25 n

Decimal 27 37 n

Defined Region

0 ≤ n ≤ 255

Initial Value

n = 0

Function

Specifies or cancels the download character set.

- When n  =  &lt;*******0&gt;B, the download character set is cancelled.

- When n  =  &lt;*******1&gt;B, the download character set is specified.

Details

- n is effective only when it is the least significant bit.

- When the download character set is cancelled, the internal character set is automatically specified.

STAR

Because ESC&amp; (define download characters) and GS* (define download bit images) are used in the same region, they cannot both be defined simultaneously.

- a. When download characters are defined, previously defined download bit images are cleared.

- b. Conversely, when download bit images are defined, previously defined download characters are cleared and the definition returns to same the internal character set.

Reference

ESC &amp;, ESC ?
