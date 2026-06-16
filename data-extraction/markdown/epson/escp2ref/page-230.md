## Format

Class 1 ASCII  &lt;MOVXBYTE&gt; Binary  0010 0100B

## Function

- Sets the increment of &lt;MOVX&gt; unit to 8.
- Starts printing of stored data.
- Moves the horizontal print position to 0 (left-most print position).
- Does not move the vertical print position.

## Notes

- The unit for this command is determined by the ESC ( U set unit command.
- This command is available when ESC . 2 TIFF compressed mode is selected.
- Execute command ESC ( G before sending this command.
- Execute this command immediately after entering raster graphics mode by sending the ESC . 2 command.

## Printers featuring this command

Stylus COLOR

Model-dependent variations

None

## Related topics

ESC . 2, ESC ( i, ESC ( G
