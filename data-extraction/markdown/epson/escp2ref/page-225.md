## Format

$$Class 2 ASCII <MOVX> nL nH Binary 010F xxxxB nL nH$$

## Parameter range

#BC = Low nibble value

F = 0, 1

0 ≤ nL ≤ 255

0 ≤ nH ≤ 127

| F     | #BC value   | Positioning parameter                | (k)Command   |
|-------|-------------|--------------------------------------|--------------|
| F = 0 | #BC = k     | #BC (-8 ~ 7)                         | <MOVX>       |
| F = 1 | #BC = 1     | n L (-128 ~ 127)                     | <MOVX> n L   |
| F = 1 | #BC = 2     | n L + n H × 256 n H (-32768 ~ 32767) | <MOVX> n H   |

Increment unit is 8 or 1 and is selected by the &lt;MOVXDOT&gt; or &lt;MOVXBYTE&gt; command

## Function

- This command is available when the ESC . 2 TIFF compressed graphics mode is selected.
- Sets relative horizontal position. The new horizontal position = current position + (parameter) × &lt;MOVX&gt; unit.
- &lt;MOVX&gt; unit is set by the &lt;MOVXDOT&gt; or &lt;MOVXBYTE&gt; command.
- If #BC has a negative value, it is described with two's complement.

## Notes

- The unit for this command is determined by the ESC ( U set unit command.
- The parameter of the new horizontal position should be a multiple of eight when the dot unit horizontal move is used.
- Settings that exceed the right or left margin will be ignored.

## Printers featuring this command

Stylus COLOR

Model-dependent variations

None

## Related topics

ESC . 2, ESC ( U, &lt;MOVXDOT&gt;, &lt;MOVXBYTE&gt;
