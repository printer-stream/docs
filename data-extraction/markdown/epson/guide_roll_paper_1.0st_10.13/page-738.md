## C O N F I D E N T I A L

- ■ Thai character print mode setting ( a = 7)

|   ( nL + nH × 256) | Thai character print mode   |
|--------------------|-----------------------------|
|                  0 | Thai 3 pass                 |
|                  1 | Thai 1 pass                 |

## ■ Number of division of thermal head energizing ( a = 97)

|   ( nL + nH × 256) | Division number   |
|--------------------|-------------------|
|                  1 | Divide into one   |
|                  2 | Divide into two   |
|                  4 | Divide into four  |
|                128 | Automatic control |

- The setting value does not affect printing in single-color printing control mode.
- When two-color printing control is specified, the setting is "Fixed at two-part energizing."
- Print control (single-color/two-color) is specified with this function ( a =116).
- ■ Setting values of print control ( a =116)
- When "Two-color printing control (257)" is specified, always use two-color paper.
- ■ Selects the black-color density in two-color printing ( a = 118)
- This setting's value affects printing in black for two-color printing.

|   ( nL + nH × 256) | Print control                 |
|--------------------|-------------------------------|
|                  1 | Single-color printing control |
|                257 | Two-color printing control    |

|   ( nL + nH × 256) | The black-color density   |
|--------------------|---------------------------|
|                 70 | Light                     |
|                 85 | Standard                  |
