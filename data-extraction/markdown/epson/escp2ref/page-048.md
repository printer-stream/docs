## Format

```
ASCII ESC J n Hex 1B 4A n Decimal 27 74 n
```

## Parameter range

```
0 ≤ n ≤ 255
```

## Function

Advances the vertical print position n/180 inch

## Notes

- ESC J does not affect the horizontal print position.
- Moving the print position below the bottom-margin position produces the following results:

Continuous paper

Moves the vertical print position to the top-margin positionon the next page

Single-sheet paper Ejects the paper

## Printers not featuring this command

None

## Model-dependent variations

On non-ESC/P 2 printers:

- Prints all data in the line buffer
- Advances paper to the top-of-form position on the next page if the ESC J command moves the print position below the bottom-margin position set with the ESC N command
- Ejects single-sheet paper if the ESC J command moves the print position beyond the end of the printable area (and paper was loaded by cut-sheet feeder)
- Ejects single-sheet paper and advances the next single sheet the remaining distance if the ESC J command moves the print position beyond the end of the printable area(and paper was loaded manually)

## Related topics

CR, LF, FF, VT, ESC ( U, ESC B, ESC ( V, ESC ( v, Moving the vertical position
