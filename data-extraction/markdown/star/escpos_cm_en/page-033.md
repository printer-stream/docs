<!-- image -->

## 4-3 Command	Details 4-3-1 Standard	Commands

HT

Name

Horizontal tab

Code

ASCII

HT

Hex.

09

Decimal

9

Function

Moves print position to next horizontal tab position.

Details

- This command is ignored if the next tab is not set.

- If the next tab position exceeds the print region, the print position is moved to [print region + 1].

- The horizontal tab position is set by ESC D (Set/cancel horizontal tab position).

- When the print position is at the [print region + 1] position and this command is received, the current line buffer full is printed and a horizontal tab is executed from the top of the next line.

- The initial value of the horizontal tab position is every 8 characters of Font A (the 9 th , 17 th , 25 th positions, etc.)

Reference

ESC D
