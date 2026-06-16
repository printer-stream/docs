<!-- image -->

<!-- image -->

<!-- image -->

[Name]

Command initialization

[Code]

ASCII

ESC @

Hex.

1B 40

Decimal

27 64

[Defined Area]

- - -

[Initial Value]

- - -

[Function]

Initializes each command after printing data in the line buffer.

However, printers with memory switch settings are initialized to the memory switch settings. DIPSW re-reading is not performed.

- ANK characters, Kanji character adornment, expansion

- Kanji character mode

- ANK right space

- Kanji character left/right spaces

- Character pitch

- International characters

- Code page

- Set slash zero

- Set specify/cancel external character (external register character data is retained)

- Page length

- Current position (move to top of page, top of line)

- Horizontal tab/Vertical tab

- Line feed amount

- Set upside-down, position alignment

- Left/right margins

The following shows the specifications that are not initialized by this command.

- Set print density

- Set print speed

- Set 2 color print mode

- Print color in 2 color print mode

- External device drive condition

-----------------------------------------------------------------------------
