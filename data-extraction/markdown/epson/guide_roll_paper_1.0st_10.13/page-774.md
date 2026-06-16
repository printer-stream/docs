## C O N F I D E N T I A L

## GS ( E pL pH fn a d1...dk &lt;Function 15&gt;

```
[Name] Set conditions for USB interface communication [Format] ASCII GS ( E pL  pH  fn  a  d1 ... dk Hex 1D 28 45 pL  pH  fn  a  d1 ... dk Decimal 29 40 69 pL  pH  fn  a  d1 ... dk [Range] ( pL + pH × 256) = 3  ( pL = 3, pH = 0) fn = 15 a = 1 48 ≤ d ≤ 49
```

[Description]

Sets  the set value of USB interface communication specified by a .

- a Configuration item

1

Class

- ■ Class settings ( a = 1)

|   d1 | Class                |
|------|----------------------|
|   48 | Vendor-defined class |
|   49 | Printer class        |

[Notes]

- ■ The configuration item set by this function is enabled by executing GS ( E &lt;Function 2&gt; or restarting the printer.  Note that the host PC must be set to enable the printer to communicate with the host PC.

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 , TM-U220

TM-U220

TM-J2000/J2100 , TM-T90 , TM-T88IV , TM-T70 , TM-L90 , TM-P60 ,

This function is not supported.

## TM-T20 , TM-T88V

The printer supports this function.
