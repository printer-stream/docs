## Format

```
ASCII ESC p n Hex 1B 70 n Decimal 27 112 n
```

## Parameter range

```
n = 0, 1, 48, 49
```

## Function

Selects either proportional or fixed character spacing according to the following values:

```
n = 0 or 48 1 or 49 Selects proportional spacing
```

Returns to current fixed character pitch

## Default

Fixed character spacing

## Notes

- This command cancels the HMI set with the ESC c command.
- This command cancels multipoint mode.
- Changes made to the fixed-pitch setting with the ESC P, ESC M, or ESC g commands during proportional mode take effect when the printer exits proportional mode.
- The printer automatically switches to LQ printing when proportional spacing is selected.

Printers not featuring this command

None

Model-dependent variations

None

## Related topics

ESC M, ESC P, ESC g, ESC !, ESC X, ESC c, Selecting the pitch
