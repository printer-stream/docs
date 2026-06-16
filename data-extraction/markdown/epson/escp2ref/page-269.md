<!-- image -->

The method of accessing characters in other areas varies depending on the type of printer.

There are two ways to access user-defined characters 0 to 31.

The first method is available only on ESC/P 2 printers. After changing to RAM characters with the ESC % 1 command, use the ESC ( ^ command to send character data. All data sent with the ESC ( ^ command is treated as character data. See ESC ( ^ in the Command Summary for details.

The table of accessible characters is as follows:

<!-- image -->
