## C O N F I D E N T I A L

## ESC T

```
[Name] Select print direction in page mode [Format] ASCII ESC T n Hex 1B 54 n Decimal 27 84 n [Range] 0 ≤ n ≤ 3, 48 ≤ n ≤ 51 [Default] n = 0
```

[Printers not featuring this command] TM-U230 , TM-U220

[Description]

[Notes]

In page mode, selects the print direction and starting position using n as follows:

| n     | Print direction   | Starting position             |
|-------|-------------------|-------------------------------|
| 0, 48 | Left to right     | Upper left (A in the figure)  |
| 1, 49 | Bottom to top     | Lower left (B in the figure)  |
| 2, 50 | Right to left     | Lower right (C in the figure) |
| 3, 51 | Top to bottom     | Upper right (D in the figure) |

<!-- image -->

- ■ The print direction set by this command is effective only in page mode.
- ■ This command setting has no effect in standard mode. If this command is processed in standard mode, an internal flag is activated, and this flag is enabled when the printer selects page mode.
- ■ The parameters for the horizontal or vertical motion unit differ, depending on the starting position of the print area as follows:
- If the starting position is the upper left or lower right of the print area: These commands use horizontal motion units: ESC SP , ESC $ , ESC \ These commands use vertical motion units: ESC 3 , ESC J , GS $ , GS \

SETTING COMMAND
