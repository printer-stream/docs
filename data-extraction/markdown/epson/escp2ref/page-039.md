## Format

ASCII ESC $ nL nH

$$Hex 1B 24 nL nH Decimal 27 36 nL nH$$

## Parameter range

0 ≤ nH ≤ 127

0 ≤ nL ≤ 255

## Function

Moves the horizontal print position to the position specified by the following formula:

<!-- formula-not-decoded -->

## Notes

- The new position is measured from the current left-margin position.
- The printer ignores this command if the specified position is to the right of the right margin.

## Printers not featuring this command

ActionPrinter Apex 80, ActionPrinter T-1000, ActionPrinter 2000, ActionPrinter 2250, ActionPrinter 2500, LX-100, LX-300, LX-400, LX-800, LX-810, LX-850, LX-1050

## Model-dependent variations

None

## Related topics

ESC \, ESC l, ESC Q, HT, CR, LF, FF, Moving the horizontal position
