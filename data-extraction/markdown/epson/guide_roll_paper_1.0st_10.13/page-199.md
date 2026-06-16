## C O N F I D E N T I A L

## GS \

```
[Name] [Format] ASCII GS \ nL nH Hex 1D 5C nL nH Decimal 29 92 nL nH [Range] -32768 ≤ ( nL + nH × 256) ≤ 32767 [Default] None
```

Set relative vertical print position in page mode

[Printers not featuring this command] TM-U230 , TM-U220

[Description]

In page mode, moves the vertical print position to ( nL + nH × 256) × (vertical or horizontal motion unit) from the current position.

[Notes]

- ■ This command is enabled only in page mode. If this command is processed in standard mode, it is ignored.
- ■ The printer ignores any setting that exceeds the print area set by ESC W .
- ■ A positive number specifies movement downward, and a negative number specifies movement upward. N pitch movement downward: ( nL + nH × 256) = N. Use the complement of N for setting N pitch movement upward: ( nL + nH × 256) = 65536 - N.
- ■ The horizontal or vertical motion unit is used for the print direction set by ESC T .
- When the starting position is set to the upper left or lower right of the print area using ESC T , the vertical motion unit is used.
- When the starting position is set to the upper right or lower left of the print area using ESC T , the horizontal motion unit is used.
- ■ Even if vertical or horizontal motion unit is changed after changing the print position, the setting of print position will not be changed.
- ■ '\' is corresponds to '\' in JIS code set.

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60
