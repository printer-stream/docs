## C O N F I D E N T I A L

## GS ( E pL pH fn a d1...dk &lt;Function 11&gt;

```
[Name] Set the configuration item for the serial interface [Format] ASCII GS ( E pL pH fn a d1...dk Hex 1D 28 45 pL pH  0B a d1...dk Decimal 29 40 69 pL pH 11 a d1...dk [Range] 3 ≤ ( pL + pH × 256) ≤ 8 (3 ≤ pL ≤ 8, pH = 0) fn = 11 48 ≤ d ≤ 57 [ a = 1] 48 ≤ d ≤ 50 [ a = 2] d = 48, 49 [ a = 3] d = 55, 56 [ a = 4] 1 ≤ k ≤ 6 TM-J2000/J2100 , TM-T90 , TM-L90 , TM-T20 , TM-U220 : 1 ≤ a ≤ 4 TM-T88IV , TM-T88V , TM-T70 : a = 1 TM-P60 : a = 1, 2 [Default] TM-J2000/J2100 , TM-T90 , TM-L90: d1 ... dk = "19200" [ a = 1] d = 48 [ a = 2] d = 48 [ a = 3] d = 56 [ a = 4] TM-T20 : d1 ... dk = "38400" [ a = 1] d = 48 [ a = 2] d = 48 [ a = 3] d = 56 [ a = 4] TM-T88IV , TM-T88V : d1 ... dk = "38400" [ a = 1] TM-T70 : d1 ... dk = "115200" [ANK model, TM-T88IV-compatible command mode disabled] d1 ... dk = "38400" [ANK model, TM-T88IV-compatible command mode enabled] d1 ... dk = "115200" [Japanese models (58 mm model, 80 mm model)] [a = 1] TM-P60 : d1...dk = "9600" [ a = 1] d = 48 [ a = 2]
```
