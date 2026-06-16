## Format

<!-- formula-not-decoded -->

## Parameter range

<!-- formula-not-decoded -->

## Function

Puts the printer in multipoint (scalable font) mode, and selects the pitch and point attributes of the font according to the following formulas:

## Pitch:

m = 0

No change in pitch

m = 1

Selects proportional spacing

m ≥ 5

Selects fixed pitch equal to 360/m cpi

## Point size:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

nH = nL = 0 No change in point size

## Default

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Notes

- This command is available only on printers featuring ESC/P 2.
- This command overrides the current pitch setting.
- Only the following point sizes are available: 8, 10 (10.5), 12, 14, 16, 18, 20 (21), 22, 24, 26, 28, 30, 32
- Selecting a combination of 15 cpi and 10 or 20-point characters results in 15-cpi ROM characters being chosen; the height of these characters is about 2/3 that of normal characters. Select the pitch with the ESC C command to obtain normal height 10 or 20point characters at 15 cpi.
