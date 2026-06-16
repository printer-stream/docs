## Format

<!-- formula-not-decoded -->

## Parameter range

0 ≤ nH ≤ 127

<!-- formula-not-decoded -->

## Function

Moves the horizontal print position left or right from the current position, as specified by the following formula:

(horizontal position) = ((nH × 256) + nL) × (defined unit) + (current position)

For positive (right) movement:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For negative (left) movement:

<!-- formula-not-decoded -->

## Notes

- Set the defined unit with the ESC ( U command.
- The default defined unit for this command is 1/120 inch in draft mode, and 1/180 inch in LQ mode.
- The printer ignores this command if it would move the print position outside the printing area.
