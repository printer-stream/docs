<!-- image -->

## 3.3.16. Oth

<!-- image -->

ers

Cancel print data and initialize commands

ASCII

CAN

Hex.

18

Decimal

24

[Defined Area]

[Initial Value]

[Function]

- - -

- - -

When the reception buffer and line buffer are cleared, the set commands are initialized.

Immediately executed not when taking out from the reception buffer, but when received from the host.

DIPSW re-reading is not performed.

The following shows the specifications that are not initialized by this command.

- Set print density
- Set print speed
- Set 2 color print mode
- Print color in 2 color print mode
- External device drive condition

-----------------------------------------------------------------------------
