## C O N F I D E N T I A L

## GS B

```
[Name] [Format] ASCII GS B n Hex 1D 42 n Decimal 29 66 n [Range] 0 ≤ n ≤ 255 [Default] n = 0
```

Turn white/black reverse print mode on/off

[Printers not featuring this command] TM-U230 , TM-U220

[Description]

Turns white/black reverse print mode on or off.

- When the LSB of n is 0, white/black reverse print mode is turned off.
- When the LSB of n is 1, white/black reverse print mode is turned on.
- ■ The white/black reverse print mode is effective for alphanumeric, Kana, multilingual, and user-defined characters.
- ■ When white/black reverse print mode is turned on, it also affects the right-side character spacing set by ESC SP .
- ■ When white/black reverse print mode is turned on, it does not affect the space between lines.
- ■ When underline mode is turned on, the printer does not underline white/black reverse characters.
- ■ This command is effective until ESC @ is executed, the printer is reset, or the power is turned off.
- ■ In white/black reverse print mode, characters are printed in white on a black background.

[Notes]

SETTING COMMAND
