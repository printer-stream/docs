## C O N F I D E N T I A L

## GS L

```
[Name] Set left margin [Format] ASCII GS L nL nH Hex 1D 4C nL nH Decimal 29 76 nL nH [Range] 0 ≤ ( nL + nH × 256) ≤ 65535 (0 ≤ nL ≤ 255, 0 ≤ nH ≤ 255) [Default] ( nL + nH × 256) = 0 ( nL = 0, nH = 0)
```

[Printers not featuring this command] TM-U230 , TM-U220

[Description]

In standard mode, sets the left margin to ( nL + nH × 256) × (horizontal motion unit) from the left edge of the printable area.

[Notes]

- ■ When standard mode is selected, this command is enabled only when processed at the beginning of the line.
- ■ The left margin has no effect in page mode. If this command is processed in page mode, the left margin is set and it is enabled when the printer returns to standard mode.
- ■ If the setting exceeds the printable area, the left margin is automatically set to the maximum value of the printable area.
- ■ If this command and GS W set the print area width to less than the width of one character, the print area width is extended to accommodate one character for the line.
- ■ Horizontal motion unit is used.
- ■ If horizontal motion unit is changed after changing left margin, left margin setting is not changed.
- ■ Left margin setting is effective until ESC @ is executed, the printer is reset, or the power is turned off.
- ■ Left margin position is left edge of the printable area. If left margin setting is changed, left edge of the printable area will move.

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60

See program example and print sample for GS L and GS W .

SETTING COMMAND
