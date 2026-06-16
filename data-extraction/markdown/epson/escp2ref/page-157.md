## Format

ASCII ESC ( ^ nL nH d1 . . . dk

<!-- formula-not-decoded -->

## Parameter range

0 ≤ nH ≤ 127

<!-- formula-not-decoded -->

## Function

- Prints data bytes d1 through dk as characters, not control codes
- The amount of data to be sent is calculated as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Default

Control-code data treated as control codes

## Notes

- This command is available only on printers featuring ESC/P 2.
- The printer ignores data if no character is assigned to that character code in the currently selected character table.

## Printers not featuring this command

All non-ESC/P 2 printers

Model-dependent variations

None

## Related topics

ESC 6, ESC 7
