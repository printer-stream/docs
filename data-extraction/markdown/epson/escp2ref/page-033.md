## Format

| ASCII   |    |
|---------|----|
| Hex     | 0D |
| Decimal | 13 |

## Function

- Moves the print position to the left margin position
- Prints all data in the line buffer

## Notes

- Always send a CR command at the end of each line of text or graphics data.
- When automatic line-feed is selected (through DIP-switch or panel setting), the CR command is accompanied by a LF command.

## Printers not featuring this command

None

## Model-dependent variations

None

## Related topics

LF, ESC l, ESC SO, SO, ESC &lt;, ESC ., Recommended command order, Moving the horizontal position, Send print data
