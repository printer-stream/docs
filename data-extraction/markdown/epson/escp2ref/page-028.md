## Format

```
ASCII ESC Q n Hex 1B 51 n Decimal 27 81 n
```

## Parameter range

```
1 ≤ n ≤ 255 (left margin) < (current pitch) × n ≤ (printable area width)
```

## Function

Sets the right margin to n columns in the current character pitch, as measured from the leftmost printable column

## Default

The right-most column

## Notes

- Set the right margin at the beginning of a line; the printer ignores any data preceding this command on the same line in the buffer.
- The following commands affect character pitch: ESC P, ESC M, ESC g, ESC W, ESC p, ESC SP, SI, SO, ESC !, ESC X, and ESC c.
- The printer calculates the right margin based on 10 cpi if proportional spacing is selected with the ESC p command.
- Always set the pitch before setting the margins. Do not assume what the pitch setting will be.
- Always set the margins at the beginning of a print job.
- Always set the right margin to be at least one column (at 10 cpi) larger than the left.

## Printers not featuring this command

None

Model-dependent variations

None

## Related topics

ESC l, ESC $, ESC \, HT, ESC D, Set the Printing Area, Setting left and right margins
