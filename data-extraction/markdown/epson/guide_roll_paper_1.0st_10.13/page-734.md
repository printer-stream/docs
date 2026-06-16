## C O N F I D E N T I A L

|   ( nL + nH × 256) | Print speed          | Print speed   |
|--------------------|----------------------|---------------|
|                  6 | Print speed level 6  | &#124;        |
|                  7 | Print speed level 7  | &#124;        |
|                  8 | Print speed level 8  | &#124;        |
|                  9 | Print speed level 9  | &#124;        |
|                 10 | Print speed level 10 | &#124;        |
|                 11 | Print speed level 11 | &#124;        |
|                 12 | Print speed level 12 | &#124;        |
|                 13 | Print speed level 13 | Fast          |

- ■ Default character code table (when a = 8)
- See (n) of the ESC t command to select character code table.
- ■ Default international character (when a = 9)
- See (n) of the ESC R command to select international character.
- ■ Column emulation mode (when a = 11)
- ■ Paper autocutting after closing the roll paper cover (when a = 100)
- ■ Automatic replacement of Font A (when a = 111)

|   ( nL + nH × 256) | Column emulation mode   |
|--------------------|-------------------------|
|                  0 | Normal mode             |
|                  1 | 42 column mode          |

|   ( nL + nH × 256) | Paper autocutting after closing the roll paper cover   |
|--------------------|--------------------------------------------------------|
|                  0 | Disabled                                               |
|                  1 | Enabled                                                |

| ( nL + nH × 256)   | Automatic replacement of Font A   |
|--------------------|-----------------------------------|
| 0, 48              | Font A (Same as no replacement)   |
| 1, 49              | Font B                            |
