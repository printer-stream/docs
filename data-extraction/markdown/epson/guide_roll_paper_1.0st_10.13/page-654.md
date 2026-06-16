## C O N F I D E N T I A L

## GS ( k &lt;Function 472&gt;

```
[Name] Composite Symbology: Select font  HRI characters [Format] ASCII GS ( k pL pH cn fn n Hex 1D 28 6B 03 00 34 48 n Decimal 29 40 107 3 0 52 72 n [Range] ( pL + pH × 256) = 3 ( pL =3, pH =0) cn = 52 fn = 72 TM-P60 : 0 ≤ n ≤ 3, 48 ≤ n ≤ 51 TM-T20 : 0 ≤ n ≤ 2, 48 ≤ n ≤ 50 TM-T88V : 0 ≤ n ≤ 2, 48 ≤ n ≤ 0 ≤ n ≤ 2, 48 ≤ n ≤ 50, n = 97, 98 (South Asia model)
```

## [Range] [Description]

[Notes]

```
50 (Other than the following model) n = 0
```

Selects a font for the Human Readable Interpretation (HRI) characters when printing Composite Symbology, using n as follows:

| n     | Font of HRI characters                            |
|-------|---------------------------------------------------|
| 0, 48 | HRI characters are not added.                     |
| 1, 49 | HRI characters are added. (Select Font A)         |
| 2, 50 | HRI characters are added. (Select Font B)         |
| 3, 51 | HRI characters are added. (Select Font C)         |
| 97    | HRI characters are added. (Select Special font A) |
| 98    | HRI characters are added. (Select Special font B) |

The character structure of each font depends on the model.

- ■ The settings of this function affect the processing of &lt;Function 481&gt; and &lt;Function 482&gt; of this command.
