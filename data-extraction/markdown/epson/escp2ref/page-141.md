## Format

| ASCII   | SI   |
|---------|------|
| Hex     | 0F   |
| Decimal | 15   |

## Function

Enters condensed mode, in which character width is reduced as follows:

| Selected pitch   | Condensed pitch   |
|------------------|-------------------|
| 10 cpi           | 17.14 cpi         |
| 12 cpi           | 20 cpi            |
| Proportional     | 1/2 width         |

## Default

Noncondensed printing

## Notes

- This command is ignored under the following two conditions:
- -The printer is in multipoint mode.
- -15-cpi printing has been selected with the ESC g command.
- This command cancels the HMI (horizontal motion index) set with the ESC c command.
- This command reduces character width by about 50% when proportional spacing is selected with the ESC p command.
- Cancel condensed printing with the DC2 command.

## Printers not featuring this command

None

## Model-dependent variations

None

## Related topics

DC2, Selecting the pitch
