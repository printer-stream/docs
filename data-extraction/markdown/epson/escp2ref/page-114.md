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
n = 0 or 48 Returns to current fixed character pitch 1 or 49 Selects proportional character spacing
```

## Default

Fixed character spacing

## Notes

- Changes made to the fixed-pitch setting with the ESC P, ESC M, or ESC g commands during proportional mode take effect when the printer exits proportional mode.
- Condensed mode is not available when proportional spacing is selected.

## Printers not featuring this command

ActionPrinter Apex 80, ActionPrinter T-1000, ActionPrinter 2000, LX-400, LX-800, LX-810, LX-850, LX-1050

## Model-dependent variations

None

## Related topics

ESC M, ESC P, ESC !, Selecting the pitch
