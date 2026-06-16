## Format

| ASCII   | ESC   | k   | n   |
|---------|-------|-----|-----|
| Hex     | 1B    | 6B  | n   |
| Decimal | 27    | 107 | n   |

## Parameter range

0 ≤ n ≤ 9

## Function

Selects the typeface for LQ printing according to the following values:

| 0            |   Roman | 7 Orator    |
|--------------|---------|-------------|
| 1 Sans serif |       8 | Orator-S    |
| 2 Courier    |       9 | Script C    |
| 3 Prestige   |      10 | Roman T     |
| 4 Script     |      11 | Sans serifH |
| 5 OCR-B      |      30 | SV Busaba   |
| 6 OCR-A      |      31 | SV Jittra   |

## Default

```
n = 0 (Roman)
```

## Notes

- The printer ignores this command if the user-defined character set is selected.
- The Roman typeface is selected if the selected typeface is not available.
- If draft mode is selected when this command is sent, the new LQ typeface will be selected when the printer returns to LQ printing.

## Printers not featuring this command

None

## Model-dependent variations

Not all printers feature all typefaces; see the Command Table section for the typefaces available on each printer model.

## Related topics

ESC x, ESC X, ESC %, ESC :, Selecting the typeface, Copying ROM characters to RAM memory
