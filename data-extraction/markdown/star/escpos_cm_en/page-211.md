<!-- image -->

Name

Set command character

Code

ASCII ESC GS / 3 n

Hex. 1b 1d 2f 32 n

Decimal 27 29 47 50 n

Defined Region

32 ≤ n ≤ 127, n = 0

Initial Value

n = 0

Function

Sets the Auto Logo function command character.

This command is registered to the non-volatile memory by the '&lt;ESC&gt; &lt;GS&gt; / W' command.

This command is ignored when Auto Logo is being executed.

| n         | Setting                      |
|-----------|------------------------------|
| 32 to 127 | Command Character            |
| 0         | No Command Character Setting |

A command character is a character that is a command for specifying the logo number to print with the Auto Logo printing.

When '/' is specified as the command character, '/2/3' is embedded in the print data.

The printer does not process the '/' as character data but as a command and stores number that follows at the end and prints it as an Auto Logo in the order that it is stored.  Therefore, if '/2/3' is embedded, Auto Logo will print Logo2 and Logo3 in that order.  If the specified logo has not been registered, logo printing will be ignored.

Also, if there is no set command character setting, a logo will not be printed.

Note that '/2/3' is processed as a command is not printed.

However, using the '&lt;ESC&gt; &lt;GS&gt; /5 n' command it is possible to switch '/2/3' to a space.

In the same way as with '/2/3/2/2' if a logo is duplicated, only the initial logo is printed.

A maximum of 32 logos can be stored as Auto Logos.

Continuing after the command character, the following shows the defined area of the character d that specifies the logo number.

'1' ≤ d ≤ '9'  (49 ≤ d ≤ 57) → Logo number 1 to 9

'A' ≤ d ≤ 'F'  (65 ≤ d ≤ 70) → Logo number 10 to 16

The logo of key codes kc1 and kc2 defined by 'GS ( L &lt;fn=67&gt;' or 'GS 8 L &lt;fn=67&gt;' is possible to print by the Logo number of this command.

The following table shows he key codes and logo number.

| n   |   kc1 |   kc2 | n   |   kc1 |   kc2 |
|-----|-------|-------|-----|-------|-------|
| '1' |     0 |     1 | '9' |     0 |     9 |
| '2' |     0 |     2 | 'A' |     1 |     0 |
| '3' |     0 |     3 | 'B' |     1 |     1 |
| '4' |     0 |     4 | 'C' |     1 |     2 |
| '5' |     0 |     5 | 'D' |     1 |     3 |
| '6' |     0 |     6 | 'E' |     1 |     4 |
| '7' |     0 |     7 | 'F' |     1 |     5 |
| '8' |     0 |     8 |     |       |       |

Reference

ESC GS / W, ESC GS / C, ESC GS / 1, ESC GS / 3, ESC GS / 4, ESC GS / 5, ESC GS / 6
