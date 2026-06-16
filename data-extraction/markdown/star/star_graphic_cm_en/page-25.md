<!-- image -->

Rev. 2.31

## 3-2) Raster Graphics Command Details

During line mode, these commands are prohibited from being used because they will not be processed be correctly. (Excluding ESC * r R command, ESC * r A command and ESC * r a command.)

## ESC * r R

[Name]

Initialize raster mode

[Code]

ASCII

ESC * r R

Hex

1B 2A 72 52

Decimal

27 42 114 82

[Defined Area]  ---

[Initial Value]

[Function]

---

Executes the initialization of raster mode.

This command is valid for other modes besides raster mode.

The raster mode initialization performed by this command is executed when entering raster mode.

This command initializes the following setting contents.

- ・ Raster page length setting (ESC * r P n NUL)
- ・ Raster print color setting (ESC * r K n NUL)
- ・ Raster top margin setting (ESC * r T n NUL)
- ・ Raster left margin setting (ESC * r T n NUL)
- ・ Raster right margin setting (ESC * r T n NUL)
- ・ Raster EOT mode setting (ESC FF EOT)
- ・ Raster FF mode setting (ESC FF NUL)
- ・ Clear raster image buffer

When entering raster mode, the command executes a process identical to initializing raster mode.

As the following setting is not initialized when entering raster mode, send this initialization command when initializing the contents below,

- ・ Raster data print color setting (ESC * r K n NUL)

(*) Raster print quality setting (ESC * Q n NUL)

--------------------------------------------------------------------------------------
