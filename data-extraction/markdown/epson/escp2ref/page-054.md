## Format

```
ASCII ESC f m n Hex 1B 66 m n Decimal 27 102 m n
```

## Parameter range

```
0 ≤ n ≤ 127 m = 0, 1
```

## Function

Moves the print position depending on the value of m, as follows:

m = 0 Prints n spaces in the current pitch.

```
1 Performs n line feeds, in the current line spacing Moves the horizontal print position to the left-margin position.
```

## Notes

- This is a nonrecommended command.
- Underline is performed between the current and final print positions when this command is used to move the print position horizontally (m = 0).
- Using this command to move the print position vertically (m = 1) cancels double-width printing selected with the SO or ESC SO command.

## Printers not featuring this command

ActionPrinter T-750, ActionPrinter 2500, DFX-5000+, DFX-5000, DFX-8000, FX-850, FX-1050

## Model-dependent variations

None

## Related topics

HT, VT, LF, ESC $, ESC \, Moving the vertical position
