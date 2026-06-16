## Format

```
ASCII ESC ( U nL nH m Hex 1B 28 55 nL nH m Decimal 27 40 85 nL nH m
```

## Parameter range

```
nL = 1, nH = 0 m = 5 , 10, 20, 30, 40, 50, 60
```

## Function

Sets the unit to m/3600 inch. The printer uses this unit when moving the print position, setting the page length, and setting the top and bottom margins with the following commands: ESC ( V, ESC ( v, ESC \, ESC $, ESC ( C, ESC ( c, &lt;MOVX&gt; , and &lt;MOVY&gt; .

## Default

The default unit varies depending on the command and print quality, as follows:

```
ESC ( V 1/360 inch ESC ( v 1/360 inch ESC ( C 1/360 inch ESC ( c 1/360 inch ESC \ (LQ mode) 1/180 inch ESC \ (draft mode) 1/120 inch ESC $ 1/60 inch <MOVX> (dot) 1/360 inch <MOVY> 1/360 inch
```

## Notes

- This command is available only on printers featuring ESC/P 2.
- The parameter and related commands highlighted in bold are new to this command and only apply to the Stylus COLOR and later inkjet printer models.

## Printers not featuring this command

All non-ESC/P 2 printers

## Model-dependent variations

None

## Related topics

HT, VT, CR, LF, FF, Set the Printing Area, Select the print position, Graphics mode
