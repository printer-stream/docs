## C O N F I D E N T I A L

## GS C 0

[Name]

Select counter print mode

[Format]

ASCII GS C 0 n m Hex 1D 43 30 n m Decimal 29 67 48 n m

[Range]

0 ≤ n ≤ 5

0 ≤ m ≤ 2, 48 ≤ m ≤ 50

[Default]

n = 0, m = 0

[Printers not featuring this command] TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-P60 , TM-U230 , TM-U220

[Description]

Selects the print format for the serial number counter value (the number of printed digits and the print position within the entire range of printed digits).

- n specifies the number of digits to be printed.
- m specifies the layout within the specified range of printed digits, as follows:

| n   | Function                                                |
|-----|---------------------------------------------------------|
| 0   | Prints the actual digits indicated by the number value. |
| 1-5 | Prints the last n digits of the serial number.          |

| m     | Justification   | Layout within digits less than those specified                        |
|-------|-----------------|-----------------------------------------------------------------------|
| 0, 48 | Align right     | Adds spaces to the left if the digits are less than those specified.  |
| 1, 49 | Align right     | Adds 0 to the left if the digits are less than those specified.       |
| 2, 50 | Align left      | Adds spaces to the right if the digits are less than those specified. |

## [Recommended Functions]

This command is supported by some printer models but may not be supported by future models. Future models will not support counter value.

SETTING COMMAND
