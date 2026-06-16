<!-- image -->

With ESC/P 2, you can select from four active character tables. See 'Assign character tables' for details.

<!-- image -->

With previous ESC/P versions, you can select from two character tables: italics and graphics.

<!-- image -->

The character table is one attribute of the font. Selecting a different character table selects a different font.

During multipoint mode, sending the commands below results in the following:

| Commands ignored   | Commands ignored                                 | Commands that cancel multipoint mode   | Commands that cancel multipoint mode   |
|--------------------|--------------------------------------------------|----------------------------------------|----------------------------------------|
| ESC W              | Double-width                                     | ESC P                                  | Select 10cpi                           |
| ESC w              | Double-height                                    | ESC M                                  | Select 12cpi                           |
| ESC SP             | Additional space                                 | ESC g                                  | Select 15cpi                           |
| SI                 | Condensed printing                               | ESC p                                  | Select proportional                    |
| SO                 | Double-width                                     | ESC !                                  | Master select                          |
| DC2                | Cancel condensed                                 | ESC @                                  | Reset                                  |
| DC4                | Cancel double-width                              |                                        |                                        |
| ESC k              | (if typeface is not available inmultipoint mode) |                                        |                                        |

## Selecting the character table

Use the ESC t command to select the character table. The format for this command is as follows:

ESC t n

The parameter n is the number of the character table.
