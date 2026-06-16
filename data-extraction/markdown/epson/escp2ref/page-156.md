## Format

ASCII

ESC w n

```
Hex 1B 77 n Decimal 27 119 n
```

## Parameter range

```
n = 0, 1, 48, 49
```

## Function

Turns on/off double-height printing of all characters, as measured from the current baseline:

n = 1 or 49 Turns on double-width 0 or 48 Turns off double-width

## Default

Standard-height printing

## Notes

- This command does not affect line spacing.
- The first line of a page is not doubled if the ESC w command is sent on the first line; all following lines are printed at double-height.
- Double-height printing overrides super/subscript, condensed, and high-speed draft printing; super/subscript, condensed, and high-speed draft printing resume when double-height printing is canceled.

## Printers not featuring this command

ActionPrinter Apex 80, ActionPrinter T-1000, DFX-5000, DFX-5000+, LX-Series printers

## Model-dependent variations

None

## Related topics

Selecting the point size
