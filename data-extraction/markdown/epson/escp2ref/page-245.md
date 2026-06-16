Use one of the following commands to set the line spacing:

ESC 2 Selects 1/6-inch line spacing

ESC 0 Selects 1/8-inch line spacing

ESC + n Selects n/360-inch line spacing (24/48-pin printers only)

ESC 3 n Selects n/180-inch line spacing (24/48-pin printers)Selects n/216-inch line spacing (9-pin printers)

Note:

- Sending the ESC N command cancels any previous top or bottom margin setting.
- The bottom margin set with the ESC N command is ignored when printing on single sheets.
- Avoid using this command with ESC/P 2 printers. By using ESC/P 2's ESC ( c command instead, the bottom margin is effective for both single-sheet and continuous paper.
- The distance from the top edge of the page to the bottom-margin position must be less than the page length.
- Use the ESC O command to cancel the bottom margin.
- Always set the line spacing before setting the bottom margin with the ESC N command. Do not assume what the line spacing setting will be.

The following commands set a bottom margin of 1 inch when 8 1/2 by 11-inch paper is used (assuming the top-of-form position is at the perforation between pages).

ESC 2 Selects 1/6-inch line spacing

ESC N 6 Sets a bottom margin 1 inch (6 lines) above the next page's top-of-form position.
