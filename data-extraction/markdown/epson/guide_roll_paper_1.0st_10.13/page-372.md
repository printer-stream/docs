## C O N F I D E N T I A L

## GS H

```
[Name] Select print position of HRI characters [Format] ASCII GS H n Hex 1D 48 n Decimal 29 72 n [Range] 0 ≤ n ≤ 3 48 ≤ n ≤ 51 [Default] n = 0
```

[Printers not featuring this command] TM-U230 , TM-U220

[Description]

[Notes]

Selects the print position of Human Readable Interpretation (HRI) characters  when printing a bar code, using n as follows:

| n     | Print position                    |
|-------|-----------------------------------|
| 0, 48 | Not printed                       |
| 1, 49 | Above the bar code                |
| 2, 50 | Below the bar code                |
| 3, 51 | Both above and below the bar code |

- ■ HRI characters are printed using the font specified by GS f .
- ■ This command setting is effective until performing of ESC @ , reset or power-off.

SETTING COMMAND
