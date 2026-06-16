## C O N F I D E N T I A L

## GS ( K &lt;Function 48&gt;

```
[Name] Select the print control mode [Format] ASCII GS ( K pL pH fn m Hex 1D 28 4B 02 00 30 m Decimal 29 49 75 2 0 48 m [Range] TM-J2000/J2100 : ( pL + pH × 256) = 2     ( pL = 2, pH = 0) fn = 48 1 ≤ m ≤ 3, 49 ≤ m ≤ 51 TM-T90 : 1 ≤ m ≤ 4, 49 ≤ m ≤ 52 TM-L90 : 0 ≤ m ≤ 4, 48 ≤ m ≤ 52 TM-P60 : m = 49, 50 [Default] TM-J2000/J2100 : m = 2 TM-T90 , TM-L90 : m = 1 TM-P60 : m = 49
```

[Description]

Selects the print control mode by m .

| m     | Function                           |
|-------|------------------------------------|
| 0, 48 | Print mode when power is turned on |
| 1, 49 | Print control mode 1               |
| 2, 50 | Print control mode 2               |
| 3, 51 | Print control mode 3               |
| 4, 52 | Print control mode 4               |

- The specification of each print control mode differs, depending on the printer model. See modeldependent variations.

[Notes]

None

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60
