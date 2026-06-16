## C O N F I D E N T I A L

## ESC d

[Name]

Print and feed n lines

[Format]

ASCII

ESC d

n

Hex

1B

64

n

Decimal

27

100

n

[Range]

0 ≤ n ≤ 255

[Default]

None

[Printers not featuring this command] None

[Description]

[Notes]

Prints the data in the print buffer and feeds n lines.

- ■ The amount of paper fed per line is based on the value set using the line spacing command ( ESC 2 or ESC 3 ).
- ■ The maximum paper feed amount is 1016 mm {40 inches}. If the specified amount exceeds 1016 mm {40 inches}, the paper feed amount is automatically set to 1016 mm {40 inches}.
- ■ After printing, the print position moves to the beginning of the line. When a left margin is set in standard mode, the position of the left margin is the beginning of the line.
- ■ When this command is processed in page mode, only the print position moves, and the printer does not perform actual printing.
- ■ This command is used to temporarily feed a specific line without changing the line spacing set by other commands.

EXECUTING COMMAND
