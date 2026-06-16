## Format

```
ASCII ESC w n Hex 1B 77 n Decimal 27 119 n
```

## Parameter range

```
n = 0, 1, 48, 49
```

## Function

Turns on/off double-height printing of all characters, as measured from the current baseline:

```
n = 1 or 49 Turns on double-width 0 or 48 Turns off double-width
```

## Default

Standard-height printing

## Notes

- This command does not affect line spacing.
- The first line of a page is not doubled if ESC w is sent on the first printable line; all following lines are printed at double-height.

Printers not featuring this command

None

Model-dependent variations

None

## Related topics

Selecting the point size
