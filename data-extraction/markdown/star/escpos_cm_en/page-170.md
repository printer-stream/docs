<!-- image -->

Name

Specify/cancel double-tall, double wide Chinese characters

Code

ASCII

FS W n

Hex.

1C 57 n

Decimal 28 87 n

Defined Region

0 ≤ n ≤ 255

Initial Value

n = 0

Function

Specifies or cancels quadruple size Chinese characters.

- Cancels quadruple size when n = &lt;*******0&gt;B.

- Specifies quadruple size when n = &lt;*******1&gt;B.

Details

- n is effective only when it is the lowest bit.

- Quadruple size characters are those characters that have both vertical and horizontal directions expanded simultaneously.

- If quadruple size is cancelled using this command, the next Chinese character data is printed at normal size.

- The base line for characters is the same when there are characters having different vertical direction ratios in the same line.

- The FS ! (Batch specify Chinese character print mode) command or GS ! (Specify character size) can also specify the Chinese character size, but the setting of the last received command is effective.

STAR

- This command is ignored when the memory switch location of use is specified as SBCS (single byte countries).

Reference

FS !, GS !
