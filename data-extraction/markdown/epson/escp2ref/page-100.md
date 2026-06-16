## Format

ASCII

ESC x n

```
Hex 1B 78 n Decimal 27 120 n
```

## Parameter range

<!-- formula-not-decoded -->

## Function

Selects either LQ or draft printing according to the following values:

```
n = 0 or 48 Draft printing 1 or 49 Letter-quality printing
```

## Notes

If you select proportional spacing with the ESC p command during draft printing, the printer prints an LQ font instead. When you cancel proportional spacing with the ESC p command, the printer returns to draft printing.

Printers not featuring this command

None

Model-dependent variations

None

## Related topics

ESC k, Print quality (draft, LQ, or NLQ)
