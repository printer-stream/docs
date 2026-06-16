## C O N F I D E N T I A L

## GS ( k &lt;Function 480&gt;

```
[Name] Composite Symbology: Store the data in the symbol storage area [Format] ASCII GS ( k pL pH cn fn m a b d1...dk Hex 1D 28 6B pL pH 34 50 30 a b d1...dk Decimal 29 40 107 pL pH 52 80 48 a b d1...dk [Range] cn = 52 fn = 80 m = 48 a =  48, 49 65 ≤ b ≤ 77 [ when (a = 48)] b = 65, 66 [ when (a = 49)] k = ( pL + pH × 256) - 5 TM-P60 : 6 ≤ ( pL + pH × 256) ≤ 2366  (0 ≤ pL ≤ 255, pH = 9) (when a = 48) 8 ≤ ( pL + pH × 256) ≤ 2366  (0 ≤ pL ≤ 255, pH = 9) (when a = 49) TM-T88V : 7 ≤ ( pL + pH × 256) ≤ 2366  (0 ≤ pL ≤ 255, pH = 9) (when a = 48) 8 ≤ ( pL + pH × 256) ≤ 2366  (0 ≤ pL ≤ 255, pH = 9) (when a = 49)
```

The domain of (d) differs with the type of line element and 2D composite element. Refer to the [Function] table.

## [Description]

Composite Symbology ( d1...dk ) is saved in the symbol storage area.

- When ( a = 48), b specifies the type of line element.

|    | Symbol data (SP indicates a   | space)   | space)             | space)      |
|----|-------------------------------|----------|--------------------|-------------|
| m  | Line element type             | Data (k) | Characters (ASCII) | Data ( d )  |
| 65 | EAN8                          | k = 7    | "0"~"9"            | 48 ≤ d ≤ 57 |
| 66 | EAN13                         | k = 12   | "0"~"9"            | 48 ≤ d ≤ 57 |
| 67 | UPC-A                         | k = 11   | "0"~"9"            | 48 ≤ d ≤ 57 |
