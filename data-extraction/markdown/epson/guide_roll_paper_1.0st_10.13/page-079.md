## C O N F I D E N T I A L

## LF

[Name]

Print and line feed

[Format]

ASCII

LF

Hex

0A

Decimal

10

[Range]

None

[Default]

None

[Printers not featuring this command] None

[Description]

Prints the data in the print buffer and feeds one line, based on the current line spacing.

[Notes]

- ■ The amount of paper fed per line is based on the value set using the line spacing command ( ESC 2 or ESC 3 ).
- ■ After printing, the print position moves to the beginning of the line. When a left margin is set in standard mode, the position of the left margin is the beginning of the line.
- ■ When this command is processed in page mode, only the print position moves, and the printer does not perform actual printing.

[Model-dependent variations] TM-L90

## Program Example for all printers

```
PRINT #1, "AAAAA"; CHR$(&HA); PRINT #1, "BBBBB"; CHR$(&HA);
```

## TM-L90

When the origin of layout is selected to bottom of label or top of black mark in standard mode and a paper feed amount that exceeds the remaining printable area of the label is sent, the printer executes one of the following:

- ■ If the printer will print a line that is higher than the remaining printable area of the label, the printer feeds the label to the next print starting position and the printer executes this command.

Print Sample

AAAAA

BBBBB

EXECUTING COMMAND
