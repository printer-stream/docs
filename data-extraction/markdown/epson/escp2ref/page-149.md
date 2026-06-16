## Format

ASCII

| Hex     |   1B |   0E |
|---------|------|------|
| Decimal |   27 |   14 |

## Function

Doubles the width of all characters, spaces, and intercharacter spacing (set with the ESC SP command) following this command on the same line.

## Default

Normal (nondouble-width) printing

## Notes

- This is a nonrecommended command; use the SO command instead.
- This command is canceled when the buffer is full, or the printer receives the following commands: LF, FF, VT, DC4, ESC W 0.
- This command is not canceled by the VT command when it functions the same as a CR command.
- This command cancels the HMI (horizontal motion index) set with the ESC c command.

## Printers not featuring this command

None

## Model-dependent variations

On non-ESC/P 2 printers:

This command is also canceled when the printer receives the following commands: CR and VT (when it functions the same as a CR command).

## Related topics

SO, DC4

ESC SO
