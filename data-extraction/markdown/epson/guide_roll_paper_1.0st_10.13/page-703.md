## C O N F I D E N T I A L

## GS ( E pL pH fn d1 d2 &lt;Function 1&gt;

[Name] Change into the user setting mode [Format] ASCII GS ( E pL pH fn d1 d2 Hex 1D 28 45 03 00 01 49 4E Decimal 29 40 69 3 0 1 73 78 [Range] ( pL + pH × 256) = 3 ( pL = 3, pH = 0) fn = 1 d1 = 73 d2 = 78

[Description]

[Notes]

Enters the user setting mode and transmits the mode change notice.

- "ESC/POS transmission handshake" is unnecessary with this function.
- ■ If the printer is in standard mode, this command is valid only at the beginning of the line.
- ■ If the printer is in page mode, this command is ignored.
- ■ Do not use this function while defining macros, because macros cannot be included with this function.
- ■ When the printer goes into the user setting mode, it transmits a 'mode change notice' back to the host.
- ■ When it has executed this function, send the next commands after checking the 'mode change notice.'
- ■ See previous [Notes for transmission process] for process sending data group.

| Transmit data   | Hex   |   Decimal | Data quantity   |
|-----------------|-------|-----------|-----------------|
| Header          | 37H   |        55 | 1 byte          |
| Identifier      | 20H   |        32 | 1 byte          |
| NUL             | 00H   |         0 | 1 byte          |
