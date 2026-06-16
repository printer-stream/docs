## Format

| ASCII   | LF   |
|---------|------|
| Hex     | 0A   |
| Decimal | 10   |

## Function

- Advances the vertical print position one line (in the currently set line spacing)
- Moves the horizontal print position to the left-margin position
- Prints all data in the buffer

## Notes

- You should always send a CR command before the LF command.
- The LF command cancels one-line double-width printing selected with the SO or ESC SO commands.
- If the LF command moves the print position below the bottom margin on continuous paper, the printer advances to the top-of-form position on the next page.
- If the LF command moves the print position beyond the end of the printable area on single-sheet paper, the printer ejects the paper.

## Printers not featuring this command

None

## Model-dependent variations

None

## Related topics

FF, ESC l, ESC SO, SO, ESC &lt;, ESC ., ESC C, ESC N, Recommended command order, Select the print position, Graphics mode, Moving the vertical position, Send print data
