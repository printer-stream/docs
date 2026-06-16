- The following maximum character widths are recommended.

(height width)

<!-- image -->

·

| Print quality   | Print quality   | 10 cpi   | 12 cpi   | 15 cpi   | Proportional   |
|-----------------|-----------------|----------|----------|----------|----------------|
| Draft           | Normal size     | 24 × 12  | 24 × 10  | 24 × 8   | Not Available  |
| Draft           | Super/subscript | 16 × 12  | 16 × 10  | 16 × 8   | Not Available  |
| LQ              | Normal size     | 24 × 36  | 24 × 30  | 24 × 24  | 24 × 42        |
| LQ              | Super/subscript | 16 × 36  | 16 × 30  | 16 × 24  | 16 × 42        |

- Send the ESC % 1 command to switch to user-defined characters.
- Use the ESC ( ^ command to print characters between 0 and 32.
- Send the ESC % 0 command followed by the ESC t 2 command to copy current userdefined characters to the upper half of the character table. The lower half of the character table is then normal ROM characters.

## Printers not featuring this command

None

## Model-dependent variations

None

## Related topics

ESC %, ESC ( ^, ESC 6, ESC 7, ESC :, ESC t, ESC ( t, Defining user-defined characters, Sending user-defined character data to printer
