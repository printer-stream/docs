## Format

ASCII

DC3

| Hex     |   13 |
|---------|------|
| Decimal |   19 |

## Function

Deselects the printer

## Default

Printer is selected

## Notes

- This is a nonrecommended command. The  SLCT IN  signal on the interface must be high to use this command. This command is nearly always unnecessary.
- The printer remains deselected until it receives a DC1 command, or power is turned off then on again. The printer ignores the ESC @ command (initialize printer) when it is deselected.
- The printer cannot be reselected by pressing the on-line button.

Printers not featuring this command

None

Model-dependent variations

None
