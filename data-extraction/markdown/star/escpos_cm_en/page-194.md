<!-- image -->

Name

Set presenter paper recovery function and automatic recovery time

Code

ASCII ESC  SYN 1 n

Hex. 1B 16 31 n

Decimal 27 22 49 n

Defined Region

0 ≤ n ≤ 255

Initial Value

Memory Switch Setting

Function

Sets presenter paper automatic recovery function and automatic recovery time.

This command is ignored when a presenter is not connected.

Settings using this command are effective from the next sheet when the printer processes this command and paper has already been supplied to the presenter.

| n           | Function                                                                                             |
|-------------|------------------------------------------------------------------------------------------------------|
| n = 0       | Paper automatic recovery function invalid.                                                           |
| 1 ≤ n ≤ 255 | Paper automatic recovery function valid. Automatic recovery time: n x 0.5 sec (0.5 sec to 127.5 sec) |

Reference

ESC SYN 0, ESC SYN 2, ESC SYN 3, ESC SYN 4
