## C O N F I D E N T I A L

## GS P

SETTING COMMAND

```
[Name] Set horizontal and vertical motion units [Format] ASCII GS P x y Hex 1D 50 x y Decimal 29 80 x y [Range] 0 ≤ x ≤ 255 0 ≤ y ≤ 255 [Default] TM-J2000/J2100 , TM-T88IV , TM-T88V : x = 180, y = 360 TM-T20 : x = 203, y = 406 x = 180, y = 360 [when 'Column emulation: 42 column mode' is selected] TM-T90 : x = 180, y = 360 [Other than Japanese model] x = 203, y = 406 [Japanese model] TM-T70 : x = 180, y = 180 [ANK model, TM-T88IV command-compatible mode disabled] x = 180, y = 360 [ANK model, TM-T88IV command-compatible mode enabled] x = 203, y = 203 [Japanese model] TM-L90 : x = 203, y = 406
```

[Printers not featuring this command] TM-P60 , TM-U230 , TM-U220

[Description]

[Notes]

Sets the horizontal and vertical motion units to approximately 25.4/ x mm {1/ x "} and approximately 25.4/ y mm {1/ y "}, respectively.

- When x = 0, the default value of the horizontal motion unit is used.
- When y = 0, the default value of the vertical motion unit is used.
- ■ The horizontal direction is perpendicular to the paper feed direction and the vertical direction is the paper feed direction.
- ■ The horizontal and vertical motion units indicate the minimum pitch used for calculating the values of related commands (shown on the next screen).
- ■ In standard mode, the following commands use x or y .
- Commands using x : ESC SP , ESC $ , ESC \ , FS S , GS ( P , GS L , and GS W
- Commands using y : ESC 3 , ESC J , ESC K , GS ( P and GS V
