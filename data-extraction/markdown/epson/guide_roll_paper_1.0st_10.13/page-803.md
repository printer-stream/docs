## C O N F I D E N T I A L

## GS c

[Name]

Print counter

[Format]

ASCII

GS c

Hex

1D

63

Decimal

29 99

[Range]

None

[Default]

None

[Printers not featuring this command] TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-P60 , TM-U230 , TM-U220

[Description] Stores the serial number counter value in the print buffer and counts up or down the serial number counter

value.

## [Recommended Functions]

This command is supported by some printer models and will not be supported by future models. Future models will not support counter value.

[Notes]

- ■ If the counter value is smaller than minimum value or bigger than maximum value when executing this command, counter value is changed based on the count mode set before stored in the print buffer.
- ■ After setting the current counter value in the print buffer as print data (a character string), the printer updates counter value based on the count mode set.
- In count-up mode, the counter value is updated as [counter value + increase and decrease value].
- In count-down mode, the counter value is updated as [counter value - increase and decrease value].
- In count-stop mode, the counter value is not updated.
- ■ The counter value in the print buffer is printed when the printer receives a print command or is in the buffer-full state.
- ■ In count-up mode, if the counter value is the maximum of the specified counter value, it is forced to convert to the minimum value by this command.
- ■ In count-down mode, if the counter value is the minimum of the specified counter value, it is forced to convert to the maximum value by this command.

EXECUTING COMMAND
