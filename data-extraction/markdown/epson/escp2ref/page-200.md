## Format

ASCII ESC r n

```
Hex 1B 72 n Decimal 27 114 n
```

## Parameter range

0 ≤ n ≤ 6

## Function

Selects the color of printing, according to the parameters below:

n = 0 Black

```
1 Magenta 2 Cyan 3 Violet 4 Yellow 5 Red 6 Green
```

## Default

```
n = 0 (Black)
```

## Notes

- The printer ignores this command if color printing is not available.
- Print yellow first when overlapping colors.
- Only black, magenta, cyan, and yellow are available during graphics mode selected with the ESC ( G command.

## Printers not featuring this command

ActionPrinter L-1000, ActionPrinter 3000, ActionPrinter 3250, ActionPrinter 4000, ActionPrinter 5000, ActionPrinter 5500, DLQ-3000, LQ-100, LQ-200, LQ-400, LQ-500, LQ510, LQ-550, LQ-570, LQ-570+, LQ-670, LQ-850, LQ-850+, LQ-870, LQ-950, LQ-1010, LQ1050, LQ-1050+, LQ-1070, LQ-1070+, LQ-1170, LQ-2070, LQ-2170, SQ-870, SQ-1170, SQ2550, TLQ-4800, TSQ-4800, Stylus 300, Stylus 800, Stylus 800+, Stylus 1000, Stylus 400

## Model-dependent variations

None

## Related topics

&lt;COLR&gt;, Selecting print color
