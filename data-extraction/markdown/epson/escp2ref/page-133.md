## Format

```
ASCII ESC -n Hex 1B 2D n Decimal 27 45 n
```

## Parameter range

```
n = 0, 1, 48, 49
```

## Function

Turns on/off printing of a line below all characters and spaces following this command:

```
n = 1 or 49 Turns on underline 0 or 48 Turns off underline
```

## Default

Normal (non-underlined) printing

## Notes

- The underline is printed with the following characteristics: draft, LQ, bold, or doublestrike.
- The underline is not printed across the distance the horizontal print position is moved with the following commands:

```
ESC $ ESC \ (when the print position is moved to the left)
```

HT

- Graphics characters are not underlined.

## Printers not featuring this command

None

Model-dependent variations

None

## Related topics

Score
