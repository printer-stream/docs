<!-- image -->

## ESC GS / 5  n

[Name] [Code]

Set command character switching method

ASCII

ESC GS / 5 n

Hex.

1b 1d 2f 35 n

Decimal

27 29 47 53 n

[Defined Area]

0 ≤ n ≤ 1

[Initial Value]

n = 0

[Function]

Sets the Auto Logo function command character switching method.

This command is registered to the non-volatile memory by the '&lt;ESC&gt; &lt;GS&gt; / W' command.

This command is ignored when Auto Logo is being executed.

|   n | Setting                                                                                      |
|-----|----------------------------------------------------------------------------------------------|
|   0 | Does not print the command character and the following logo number                           |
|   1 | Switches the command character and the following logo number into a space character (0 x 20) |

When '/' is specified  as the  command character, the '/2' embedded in the print data is not a character string, but processed as a command.

At this time, '/2' is processed as a command is not printed.

However, by specifying n = 1 in this command, it is possible to switch '/2' to a space.

-----------------------------------------------------------------------------
