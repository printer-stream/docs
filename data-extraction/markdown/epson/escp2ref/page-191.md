## Format

|         |    |    | L   | H   | 1   | 2   |       | k   |
|---------|----|----|-----|-----|-----|-----|-------|-----|
| Hex     | 1B | 4B | n L | n H | d 1 | d 2 | . . . | d k |
| Decimal | 27 | 75 | n L | n H | d 1 | d 2 | . . . | d k |

## Parameter range

0 ≤ nL ≤ 255

0 ≤ nH ≤ 31

0 ≤ d ≤ 255

## Function

Prints bit-image graphics in 8-dot columns, at a density of 60 horizontal by 72 vertical dpi, according to the following parameters:

Specify the total number of columns (k) of graphics data following,

nL, nH according to the formula

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

d1 . . . d k Bytes of graphics data

## Notes

- This is a nonrecommended command. The ESC * 0 command is identical to this command; use ESC * 0 instead of this command.
- The dot density printed with this command can be redefined with the ESC ? command.

Printers not featuring this command

None

Model-dependent variations

None

Related topics

ESC *
