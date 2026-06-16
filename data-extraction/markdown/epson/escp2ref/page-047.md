- Moving the print position below the bottom-margin position produces the following results:
- Continuous paper Moves the vertical print position to the top-margin positionon the next page
- Single-sheet paper Ejects the paper
- The printer ignores this command under the following conditions:
- -The command would move the print position more than 179/360 inch in the negative direction.
- -The command would move the print position in the negative direction after a graphics command is sent on the current line, or above the point where graphics have previously been printed.
- -The command would move the print position above the top-margin position.

## Printers not featuring this command

All non-ESC/P 2 printers

## Model-dependent variations

None

## Related topics

CR, LF, FF, VT, ESC ( U, ESC B, Moving the vertical position
