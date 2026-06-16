For non-ESC/p 2 printers, set the page length with the following commands:

ESC C Sets the page length in lines, according to the currentline spacing

ESC C NUL Sets the page length in 1-inch increments

To set the page length in lines, you must first set the line spacing. The maximum number of lines you can set with the ESC C command is 127.

Use the following commands to set the line spacing:

ESC 2 Selects 1/6-inch line spacing

ESC 0 Selects 1/8-inch line spacing

ESC + n Selects n/360-inch line spacing (24/48-pin printers only)

ESC 3 n Selects n/180-inch line spacing (24/48-pin printers)Selects n/216-inch line spacing (9-pin printers)

## Note:

- Always set the page length before paper is loaded or when the print position is at the top-of-form position. Otherwise, the current print position becomes the top-of-form position, which results in undesirable contradictions between the actual and logical page settings.
- Setting the page length cancels any previously set bottom margin.
- The maximum page length is 22 inches.
- Changing the line spacing after the page length has been set does not affect the page length.
- Always set the line spacing before setting the page length with the ESC C command. Do not assume what the line spacing will be.

The following commands select 1/6-inch line spacing and a page length of 11 inches (66 lines).

ESC 2 Selects 1/6-inch line spacing

ESC C 66 Sets a page length of 11 inches (66 lines)

The following command also selects a page length of 11 inches.

ESC C NUL 11 Sets a page length of 11 inches
