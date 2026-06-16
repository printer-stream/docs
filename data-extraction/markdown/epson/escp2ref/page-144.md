## Format

ASCII

ESC SI

| Hex     |   1B |   0F |
|---------|------|------|
| Decimal |   27 |   15 |

## Parameter range

No parameters

## Function

Enters condensed mode, in which characters width is reduced as follows:

| Selected pitch   | Condensed pitch   |
|------------------|-------------------|
| 10 cpi           | 17.14 cpi         |
| 12 cpi           | 20 cpi            |

## Default

Noncondensed printing

## Notes

- This is a nonrecommended command; use the SI command instead.
- Cancel condensed printing with the DC2 command.

Printers not featuring this command

None

Model-dependent variations

None

Related topics

SI, DC2, Selecting the pitch
