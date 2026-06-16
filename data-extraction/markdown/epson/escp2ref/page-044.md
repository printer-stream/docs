## Format

<!-- formula-not-decoded -->

## Parameter range

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Function

Moves the vertical print position to the position specified by the following formula:

(vertical position) = ((mH × 256) + mL) × (defined unit) + (top-margin position)

<!-- formula-not-decoded -->

## Notes

- This command is available only on printers featuring ESC/P 2.
- Set the defined unit using the ESC ( U command.
- The default defined unit for this command is 1/360 inch.
- The new position is measured in defined units from the current top-margin position.
- Moving the print position below the bottom-margin position produces the following results:

Continuous paper Moves the vertical print position to the top-margin positionon the next page

Single-sheet paper Ejects the paper

- The printer ignores this command under the following conditions:
- -The command would move the print position more than 179/360 inch in the negative direction
- -The command would move the print position in the negative direction after a graphics command is sent on the current line, or above the point where graphics have previously been printed
