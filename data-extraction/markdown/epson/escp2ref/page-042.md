## Format

ASCII ESC \ nL nH

<!-- formula-not-decoded -->

## Parameter range

0 ≤ nH ≤ 127

<!-- formula-not-decoded -->

## Function

Moves the horizontal print position left or right from the current position, as specifiedby the following formula:

(horizontal position) = ((nH × 256) + nL) × (1/120 inch) + (current margin)

For positive (right) movement:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For negative (left) movement:

<!-- formula-not-decoded -->

## Notes

The printer ignores this command if it would move the print position outside the printable area.
