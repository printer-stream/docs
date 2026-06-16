## C O N F I D E N T I A L

[Notes]

- ■ The character size set by this command is effective for alphanumeric, Kana, multilingual, and user-defined characters.
- ■ When the characters are enlarged with different heights on one line, all the characters on the line are aligned at the baseline.
- ■ When the characters are enlarged widthwise, the characters are enlarged to the right, based on the left side of the character.
- ■ ESC ! can also turn double-width and double-height modes on or off.
- ■ In standard mode, the character is enlarged in the paper feed direction when double-height mode is selected, and it is enlarged perpendicular to the paper feed direction when double-width mode is selected. However, when character orientation changes in 90° clockwise rotation mode, the relationship between double-height and double-width is reversed.
- ■ In page mode, double-height and double-width are on the character orientation.
- ■ The setting of the character size of alphanumeric and Katakana is effective until ESC ! is executed, ESC @ is executed, the printer is reset, or the power is turned off.
- ■ The setting of the character size of Kanji and multilingual characters is effective until FS ! is executed, FS W is executed, ESC @ is executed, the printer is reset, or the power is turned off.

[Model-dependent variations]

TM-P60

## Program Example for all printers

PRINT #1, CHR$(&amp;H1D);"!";CHR$(17);

PRINT #1, "AAAAA"; CHR$(&amp;HA); PRINT #1, CHR$(&amp;H1D);"!";CHR$(0); PRINT #1, "BBBBB"; CHR$(&amp;HA);

## TM-P60

## [Peeler model]

With special fonts (24 × 48), enlargement of [width: times 1 to times 4 / height: times 1 to times 4] is possible. Even when 5 times or more is specified for special fonts (24 × 48), they are printed at 4 times enlargement.

## Print Sample

AAAAA ← Select quadruple (double-height x double-width) BBBBB
