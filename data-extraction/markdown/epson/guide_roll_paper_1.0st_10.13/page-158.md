## C O N F I D E N T I A L

## GS b

[Name]

Turn smoothing mode on/off

[Format]

ASCII

GS b n

Hex

1D 62 n

Decima

29

98

n

[Range]

0 ≤ n ≤ 255

[Default]

n = 0

[Printers not featuring this command] TM-U230 , TM-U220

[Description]

[Notes]

Turns smoothing mode on or off.

- When the LSB of n is 0, smoothing mode is turned off.
- When the LSB of n is 1, smoothing mode is turned on.
- ■ The smoothing mode is effective for quadruple-size or larger characters [alphanumeric, Kana, multilingual, and user-defined characters.]
- ■ This command is effective until ESC @ is executed, the printer is reset, or the power is turned off.

[Model-dependent variations]

None

## Program Example for all printers

```
PRINT #1, CHR$(&H1D);"!";CHR$(68); ← Select font size PRINT #1, CHR$(&H1D);"b";CHR$(1); ← Select smoothing PRINT #1, "AAAAA"; CHR$(&HA);
```

Print Sample

AAAAA

SETTING COMMAND
