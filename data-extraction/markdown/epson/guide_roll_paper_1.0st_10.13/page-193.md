## C O N F I D E N T I A L

## GS T

[Name]

Set print position to the beginning of print line

[Format]

ASCII

GS

T

n

Hex

1D

54

n

Decimal

29

84

n

[Range]

n = 0, 1, 48, 49

[Default]

None

[Printers not featuring this command] TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-P60 , TM-U230 , TM-U220

[Description]

[Notes]

In standard mode, moves the print position to the beginning of the print line after performing the operation specified by n .

| n     | Function                                |
|-------|-----------------------------------------|
| 0, 48 | Cancel data in the current print buffer |
| 1, 49 | Print data in the current print buffer  |

- ■ In page mode, this command is ignored.
- ■ This command is ignored if the print position is already the beginning of the line.
- ■ If the print position is not set to the beginning of the line, when n = 1, 49, this command functions the same as LF .
- ■ Setting values of each command, definitions, and receive buffer content are not changed.
- ■ By processing this command, the print position moves to the left of the print area. The printer will be in the beginning of the line and data will not be in the print buffer.
- ■ When using commands that are enabled only at the beginning of the line, these commands are sure to be executed if GS T is used immediately before using those commands.

EXECUTING COMMAND
