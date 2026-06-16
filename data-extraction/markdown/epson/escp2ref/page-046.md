## Format

<!-- formula-not-decoded -->

## Parameter range

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Function

Moves the vertical print position up or down from the current position, as specified by the following formula:

(horizontal position) = ((mH × 256) + mL) × (defined unit) + (current position)

For positive (down) movement:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For negative (up) movement:

<!-- formula-not-decoded -->

## Notes

- This command is available only on printers featuring ESC/P 2.
- Set the defined unit using the ESC ( U command.
- The default defined unit for this command is 1/360 inch.
- The new position is measured in defined units from the current position.
