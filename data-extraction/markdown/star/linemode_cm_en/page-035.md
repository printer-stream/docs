<!-- image -->

## ESC - n

[Name] [Code]

Select/cancels underling mode

ASCII

ESC - n

Hex.

1B 2D n

Decimal

27 45 n

[Defined Area]

n = 0, 1, 48, 49

[Initial Value]

n = 0 (Underline cancelled)

[Function]

Specifies underlining (2 dots).

Underlines are composed of 2 dot lines.

Underlines are not applied to horizontal tabs and to specified horizontal direction positions.

Underlines are expanded if the character expansion is specified. (When double high expansion is

used, underlines are composed of 4 dots.)

Underlines are enabled for white/black inversion.

This command is enabled for ANK characters and Kanji characters.

IBM block ignores underlines.

| n     | Underline           |
|-------|---------------------|
| 0, 48 | Cancels underline   |
| 1, 49 | Specifies underline |

## ESC \_ n

Specify/cancel upperline

[Name]

[Code]

ASCII

ESC \_ n

Hex.

1B 5F n

Decimal

27 95 n

[Defined Area]

n = 0, 1, 48, 49

[Initial Value]

n = 0 (Upperline cancelled)

[Function]

Specifies upperlining (2 dots).

Upperlines are composed of 2 dot lines.

Upperlines are not applied to horizontal tabs and to specified horizontal direction positions.

Upperlines are expanded if the character expansion is specified. (When double high expansion is used, upperlines are composed of 4 dots.)

Upperlines are enabled for white/black inversion.

This command is enabled for ANK characters and Kanji characters.

IBM block ignores upperlines.

| n     | Upperline           |
|-------|---------------------|
| 0, 48 | Cancels upperline   |
| 1, 49 | Specifies upperline |

-----------------------------------------------------------------------------
