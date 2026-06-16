## Format

```
ASCII ESC l n Hex 1B 6C n Decimal 27 108 n
```

## Parameter range

```
1 ≤ n ≤ 255 0 ≤ (left margin) <(right margin)
```

## Function

Sets the left margin to n columns in the current character pitch, as measured from the leftmost printable column

## Default

The left-most column (column 1)

## Notes

- Set the left margin at the beginning of a line; the printer ignores any data preceding this command on the same line in the buffer.
- The following commands affect character pitch: ESC P, ESC M, ESC g, ESC W, ESC p, ESC SP, and SI.
- The printer calculates the left margin based on 10 cpi if proportional spacing is selected with the ESC p command.
- Always set the pitch before setting the margins. Do not assume what the pitch setting will be.
- Always set the margins at the beginning of a print job.
- Always set the left margin to be at least two columns (at 10 cpi) less than the right.
- Moving the left margin position moves the tab settings by the same distance.

## Printers not featuring this command

None

Model-dependent variations

None

## Related topics

ESC Q, ESC $, ESC \, ESC D, HT, Set the Printing Area, Setting left and right margins
