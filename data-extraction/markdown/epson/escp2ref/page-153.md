## Format

ASCII ESC W n

```
Hex 1B 57 n Decimal 27 87 n
```

## Parameter range

```
n = 0, 1, 48, 49
```

## Function

Turns on/off double-width printing of all characters, spaces, and intercharacter spacing (set with the ESC SP command) following this command as follows:

```
n = 1 or 49 Turns on double-width 0 or 48 Turns off double-width
```

## Default

Normal (nondouble-width) printing

## Notes

This command cancels the HMI (horizontal motion index) set with the ESC c command.

## Printers not featuring this command

None

Model-dependent variations

None

## Related topics

SO, DC4
