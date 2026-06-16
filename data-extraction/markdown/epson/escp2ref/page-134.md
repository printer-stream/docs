## Format

| ASCII   | ESC   |   ( | -   | n L   | n H   | m   | d1   | d2   |
|---------|-------|-----|-----|-------|-------|-----|------|------|
| Hex     | 1B    |  28 | 2D  | n L   | n H   | m   | d1   | d2   |
| Decimal | 27    |  40 | 45  | n L   | n H   | m   | d1   | d2   |

## Parameter range

```
nL = 3, nH = 0 m = 1 1 ≤ d1 ≤ 3 d2 = 0, 1, 2, 5, 6
```

## Function

Turns on/off scoring of all characters and spaces following this command, according to the parameters below:

d1 = 1 Underline

2 Strikethrough

3 Overscore

```
d2 = 0 Turn off scoring 1 Single continuous line 2 Double continuous line 5 Single broken line 6 Double broken line
```

## Default

No scoring

## Notes

- This command is only available on 24 and 48-pin printers.
- Each type of scoring is independent of other types; any combination of scoring methods may be set simultaneously.
- The position and thickness of scoring depends on the current point size setting.
- The score is printed with the following characteristics: draft, LQ, bold, or double- strike.
- Graphics characters are not scored.
- Scoring is not printed across the distance the horizontal print position is moved with the following commands:

```
ESC $ ESC \ (when the print position is moved to the left) HT
```
