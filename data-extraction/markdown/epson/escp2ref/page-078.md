## Format

ASCII ESC a n

```
Hex 1B 61 n Decimal 27 97 n
```

## Parameter range

```
0 ≤ n ≤ 3
```

## Function

Selects from four types of justification, as follows:

```
n = 0 or 48 Flush left 1 or 49 Centered 2 or 50 Flush right 3 or 51 Full justification (flush right and left)
```

## Default

## Flush left

## Notes

- This is a nonrecommended command.
- This command has been deleted in ESC/P 2 printers.
- Always set justification at the beginning of a line.
- The printer performs full justification only if the width of the current line is greater than 75% of the printing area width. If the line width is less than 75%, the printer left-justifies text.
- You should not use commands that adjust the horizontal print position during full justification. These commands are: DEL, HT, BS, ESC f 0, ESC $, and ESC \.
- Justification is based on the font selected when the justification command is sent. Changing the font after setting justification can cause unpredictable results.

## Printers not featuring this command

All ESC/P 2 printers, ActionPrinter 3000, LQ-200

## Model-dependent variations

None

## Related topics

ESC P, ESC M, ESC g, SO, ESC SP, ESC $, ESC \, Moving the horizontal position, Selecting the pitch
