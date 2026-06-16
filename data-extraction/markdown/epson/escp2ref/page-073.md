## Format

|         |    |    |    | 1   |       | k   |    |
|---------|----|----|----|-----|-------|-----|----|
| Hex     | 1B | 62 | m  | n 1 | . . . | n k | 00 |
| Decimal | 27 | 98 | m  | n 1 | . . . | n k |  0 |

## Parameter range

```
0 ≤ m ≤ 7 1 ≤ n ≤ 255 nk > n(k-1) 1 ≤ k ≤ 16
```

## Function

Sets vertical tab positions at the lines specified by n1 to nk (in the current line spacing) in tab set m, as measured from the top-of-form position

## Notes

- This is a nonrecommended command.
- Up to eight sets of tabs can be set.
- The value for m specifies the number of the tab set being changed; these sets of tabs are called vertical formatting unit (VFU) channels.
- The values for n must be in ascending order; a value of n less than the previous n ends tab setting (like the NUL code).
- Send the ESC / command to select a VFU channel other than channel 0; the VT (tab vertically) command then uses the settings for the selected channel.
- Changing the line spacing does not affect previous tab settings.
- Sending the ESC b command clears any previous tab settings in that tab set.
- Send an ESC b m NUL command to cancel all tab settings in tab set m.
- A maximum of 16 vertical tabs can be set in each VFU channel.
- The printer stores all tab settings, even if outside the printing area; if you increase the page length to include previously set tabs, you can move to those positions with the VT (tab vertically) command.

## Printers not featuring this command

None

## Model-dependent variations

None

## Related topics

ESC /, VT, ESC 0, ESC 2, ESC 3, Setting page length, Setting bottom margin, Moving the vertical position
