## C O N F I D E N T I A L

## GS f

```
[Name] Select font for HRI characters [Format] ASCII GS f n Hex 1D 66 n Decimal 29 102 n [Range] TM-J2000/J2100 , TM-T90 , TM-L90 : n = 0, 1, 48, 49 (Other than Japanese model) 0 ≤ n ≤ 2, 48 ≤ n ≤ 50 (Japanese model) TM-T20 : 0, 1, 48, 49 TM-T88IV , TM-T88V , TM-T70 : n = 0, 1, 48, 49 (Other than South Asia model) n = 0, 1, 48, 49, 97, 98 (South Asia model) TM-P60 : 0 ≤ n ≤ 2, 48 ≤ n ≤ 50 [Default] n = 0
```

[Printers not featuring this command] TM-U230 , TM-U220

[Description]

[Notes]

Selects a font for the Human Readable Interpretation (HRI) characters when printing a bar code, using n as follows:

| n     | Font of HRI characters   |
|-------|--------------------------|
| 0, 48 | Font A                   |
| 1, 49 | Font B                   |
| 2, 50 | Font C                   |
| 97    | Special font A           |
| 98    | Special font B           |

- ■ The font set by this command is effective only for HRI character.
- ■ The composition of the character of each font is different depending on the model.
- ■ Configurations of Font A and Font B are different, depending on the printer model.

SETTING COMMAND
