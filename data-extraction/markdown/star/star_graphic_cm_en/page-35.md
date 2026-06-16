<!-- image -->

Rev. 2.31

## ESC * r a

[Name]

Start block

[Code]

ASCII ESC * r a

Hex

1B 2A 72 61

Decimal

[Defined Area]  ---

[Initial Value]

---

[Function]

Starts the block

Enters the command emulator mode.

This command is ignored during command simulator mode.

When it enters the command emulator mode, initialize the command emulator mode.

The corresponding initialization contents are listed below.

- ・ Raster page length setting (ESC * r P n NUL)
- ・ Raster top margin setting (ESC * r T n NUL)
- ・ Raster left margin setting (ESC * r T n NUL)
- ・ Raster right margin setting (ESC * r T n NUL)
- ・ Raster EOT mode setting (ESC FF EOT)
- ・ Raster FF mode setting (ESC FF NUL)
- ・ Clear raster image buffer
- (*) Raster page length setting (ESC * r P n NUL), is initialized to 0.
- (*) Raster print color setting (ESC * r K n NUL)is not initialized when entering raster mode.
- (*) Raster print quality setting (ESC * Q n NUL)is not initialized when entering raster mode.

## ESC * r b

[Name]

End the block

[Code]

ASCII

ESC * r b

Hex

1B 2A 72 62

Decimal 27 42 114

98

[Defined Area]  ---

[Initial Value]

---

[Function]

Ends the block

Maintains a command emulator.

If raster data remains in the image buffer of the raster mode, command emulator is maintained when raster EM mode is executed.

--------------------------------------------------------------------------------------

27 42 114 97
