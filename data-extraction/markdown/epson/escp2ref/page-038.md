## Format

ASCII ESC $ nL nH

<!-- formula-not-decoded -->

## Parameter range

0 ≤ nH ≤ 127

<!-- formula-not-decoded -->

## Function

Moves the horizontal print position to the position specified by the following formula:

(horizontal position) = ((nH × 256) + nL) × (defined unit) + (left margin)

<!-- formula-not-decoded -->

## Notes

- Set the defined unit with the ESC ( U command.
- The default defined unit setting for this command is 1/60 inch.
- The new position is measured from the current left-margin position.
- The printer ignores this command if the specified position is to the right of the right margin.

## Printers not featuring this command

None

Model-dependent variations

On non-ESC/P 2 printers:

The unit of movement is fixed at 1/60 inch.

## Related topics

ESC \, ESC l, ESC Q, HT, CR, LF, FF, ESC ( U, Moving the horizontal position
