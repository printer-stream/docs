<!-- image -->

Name

Set partial cut before Auto Logo printing

Code

ASCII ESC GS / 6 n

Hex. 1b 1d 2f 36 n

Decimal 27 29 47 54 n

Defined Region

0 ≤ n ≤ 1

Initial Value

n = 0

Function

Sets a partial cut before the Auto Logo printing.

This command is registered to the non-volatile memory by the '&lt;ESC&gt; &lt;GS&gt; / W' command.

This command is ignored when Auto Logo is being executed.

|   n | Setting                                                       |
|-----|---------------------------------------------------------------|
|   0 | Does not execute a partial cut before the Auto Logo printing. |
|   1 | Executes a partial cut before the Auto Logo printing.         |

When printing Logo2 and Logo3 as Auto Logo printing like the one in the drawing below, this command selects to execute a partial cut before printing Logo2 of the Auto Logo and Logo3.

If a partial cut is executed using this function, it is possible to provide coupons, etc., that are printed using Auto Logo with a partial cut.

Reference

ESC GS / W, ESC GS / C, ESC GS / 1, ESC GS / 2, ESC GS / 3, ESC GS / 4, ESC GS / 5

<!-- image -->
