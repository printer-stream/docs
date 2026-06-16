<!-- image -->

Rev. 2.31

## ESC * r A

[Name]

Enter raster mode

[Code]

ASCII

ESC * r A

Hex

1B 2A 72 41

Decimal

27 42 114 65

[Defined Area]  ---

[Initial Value]

---

[Function]

Enters raster mode.

This command is ignored during raster mode.

When entering raster mode, raster mode is initialized.

The corresponding initialization contents are listed below.

- ・ Raster page length setting (ESC * r P n NUL)

- ・ Raster top margin setting (ESC * r T n NUL)

- ・ Raster left margin setting (ESC * r T n NUL)

- ・ Raster right margin setting (ESC * r T n NUL)

- ・ Raster EOT mode setting (ESC FF EOT)

- ・ Raster FF mode setting (ESC FF NUL)

- (*) Raster print color setting(ESC * r K n NUL)is not initialized when entering raster mode.

- (*) Raster print quality setting (ESC * Q n NUL)is not initialized when entering raster mode.

If the printer is in command emulator mode and there is unprinted data, this command is processed after the unprinted data is printed. (Cutting and feeding operations are not performed.)

## ESC * r B

[Name]

Quit raster mode

[Code]

ASCII ESC * r

B

Hex

1B 2A 72 42

Decimal

27 42 114 66

[Defined Area]  ---

[Initial Value]

---

[Function]

Ends raster mode.

When raster mode ends, and if raster data still remains in the image buffer of the raster mode, after executing raster EOT mode, terminate the raster mode.

## ESC * r C

[Name]

Clear raster data

[Code]

ASCII ESC * r C

Hex

1B 2A 72 43

Decimal 27 42 114 67

[Defined Area]  ---

[Initial Value] ---

[Function] Clears the image buffer data of raster mode.

--------------------------------------------------------------------------------------
