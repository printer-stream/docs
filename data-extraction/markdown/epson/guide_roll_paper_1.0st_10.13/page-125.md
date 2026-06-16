## C O N F I D E N T I A L

## ESC G

```
[Name] Turn double-strike mode on/off [Format] ASCII ESC G n Hex 1B 47 n Decimal 27 71 n [Range] 0 ≤ n ≤ 255 [Default] n = 0
```

[Printers not featuring this command] TM-P60

[Description]

Turns double-strike mode on or off.

- When the LSB of n is 0, double-strike mode is turned off.
- When the LSB of n is 1, double-strike mode is turned on.

[Notes]

- ■ The double-strike mode is effective for alphanumeric, Kana, multilingual, and user-defined characters.

[Model-dependent variations]

## TM-U230 , TM-U220

## Program Example for all printers

```
PRINT #1, CHR$(&H1B);"G";CHR$(1); ← Select PRINT #1, "AAAAA"; CHR$(&HA); PRINT #1, CHR$(&H1B);"G";CHR$(0); ← Cancel PRINT #1, "BBBBB"; CHR$(&HA);
```

## TM-U220 , TM-U230

Print speed is slow when double-strike mode on because this printer prints with 2 passes in this mode.

```
AAAAA ← Double-strike BBBBB ← Normal
```

## Print Sample

SETTING COMMAND
