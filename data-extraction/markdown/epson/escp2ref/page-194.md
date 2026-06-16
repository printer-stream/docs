## Format

|         |    |    | L   | H   | 1   | 2   |       | k   |
|---------|----|----|-----|-----|-----|-----|-------|-----|
| Hex     | 1B | 59 | n L | n H | d 1 | d 2 | . . . | d k |
| Decimal | 27 | 89 | n L | n H | d 1 | d 2 | . . . | d k |

## Parameter range

0 ≤ nL ≤ 255

0 ≤ nH ≤ 31

0 ≤ d ≤ 255

## Function

Prints bit-image graphics in 8-dot columns, at a density of 120 horizontal by 60 vertical dpi, according to the following parameters:

Specify the total number of columns (k) of graphics data following,

nL, nH according to the formula

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

d1 . . . d k Bytes of graphics data

## Notes

- This is a nonrecommended command. The ESC * 2 command is identical to this command; use ESC * 2 instead of this command.
- The speed is double because consecutive horizontal dots cannot be printed; the printer ignores the second continuous horizontal dot.
- The dot density printed with this command can be redefined with the ESC ? command.

## Printers not featuring this command

None

Model-dependent variations

None

## Related topics

ESC *
