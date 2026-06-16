## Format

| Hex     |   1B |   65 | m   | n   |
|---------|------|------|-----|-----|
| Decimal |   27 |  101 | m   | n   |

## Parameter range

m = 0, 1

## horizontal tabs (m=0)

```
0 ≤ n ≤ 21 10 cpi 0 ≤ n ≤ 25 12 cpi 0 ≤ n ≤ 36 Condensed printing vertical tabs (m=1) 0 ≤ n ≤ 127 (line spacing) × n < (page length)
```

## Function

Sets fixed tabs, as follows:

- m = 0 Sets vertical tabs every n lines in the current line spacing, as measured fromthe top-of-form position

- 1 Sets horizontal tabs every n characters in the current character pitch

## Default

Horizontal tabs:

Every eight characters

Vertical tabs:

None

## Notes

- This is a nonrecommended command.
- Use the VT command to move to the next vertical tab or the HT command to move to the next horizontal tab.
- The ESC e command clears previously set tabs.
- The printer ignores this command if the value for n would make the vertical tab increment longer than the current page length, or if n is greater than the maximum for the current character pitch.
