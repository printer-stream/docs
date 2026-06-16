## C O N F I D E N T I A L

## FS W

[Name]

[Format]

Turn quadruple-size mode on/off for Kanji characters

```
ASCII FS W n Hex 1C 57 n Decimal 28 87 n
```

[Printers not featuring this command] None

[Range]

0 ≤ n ≤ 255

[Default]

n = 0

[Description]

Turns quadruple-size mode on or off for multi-byte code character.

- When the LSB of n is 0, quadruple-size mode is turned off and normal size is specified.
- When the LSB of n is 1, quadruple-size mode is turned on.
- ■ Settings of this command affect multilingual characters and user-defined characters.
- ■ When a double-height mode is specified, a character is enlarged based on a baseline of the character and when a double-width mode is specified, a character is enlarged based on the left side of the character.
- ■ Settings of this command are effective until FS ! is executed, GS ! is executed, ESC @ is executed, the printer is reset, or the power is turned off.

```
Program Example ← Specify quadruple-size mode Print Sample ← Normal size ← Quadruple size
```

```
PRINT #1, CHR$(&H1C);"C";CHR$(0); Select JIS code system PRINT #1, CHR$(&H1C);"&"; PRINT #1, CHR$(&H1C);"W";CHR$(0); ← Cancel quadruple-size mode PRINT #1, CHR$(&H34);CHR$(&H41); PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA); PRINT #1, CHR$(&H1C);"W";CHR$(1); ← PRINT #1, CHR$(&H34);CHR$(&H41); PRINT #1, CHR$(&H3B);CHR$(&H7A);CHR$(&HA); PRINT #1, CHR$(&H1C);".";
```

[Notes]

SETTING COMMAND
