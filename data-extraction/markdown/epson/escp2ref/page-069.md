## Format

|         |    |    | 1   | 2   |       | k   |    |
|---------|----|----|-----|-----|-------|-----|----|
| Hex     | 1B | 44 | n 1 | n 2 | . . . | n k | 00 |
| Decimal | 27 | 68 | n 1 | n 2 | . . . | n k |  0 |

## Parameter range

```
0 ≤ k ≤ 32 1 ≤ n ≤ 255 nk > n(k-1)
```

## Function

Sets horizontal tab positions (in the current character pitch) at the columns specified by n1 to nk, as measured from the left-margin position

## Default

Every eight characters

## Notes

- The values for n must be in ascending order; a value of n less than the previous n ends tab setting (like the NUL code).
- Changing the character pitch does not affect current tab settings.
- Send an ESC D NUL command to cancel all tab settings.
- The tab settings move to match any movement in the left margin.
- A maximum of 32 horizontal tabs can be set.
- The printer does not move the print position to any tabs beyond the right-margin position. However, all tab settings are stored in the printer's memory; if you move the right margin, you can access previously ignored tabs.
- The printer calculates tab positions based on 10 cpi if proportional spacing is selected with the ESC p command.
- Sending the ESC D command clears any previous tab settings.

## Printers not featuring this command

None

## Model-dependent variations

None

## Related topics

ESC $, ESC \, ESC P, ESC M, ESC p, ESC l, ESC Q, Setting the left and right margins, Moving the horizontal position
