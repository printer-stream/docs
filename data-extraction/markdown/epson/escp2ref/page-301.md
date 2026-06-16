The order for sending data depends on the mode selected with the m parameter. The table at the beginning of this section lists the number of bytes of data required for each column.

<!-- image -->

Count the number of resulting columns in each line. The nL and nH parameters tell the printer how many columns to expect. Calculate nL and nH as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If you are going to send more than one line of graphics, send the following commands to set the line spacing:

| 24/48-pin printers   | ESC + 48   | 48/360-inch line spacing   |
|----------------------|------------|----------------------------|
| 9-pin printers       | ESC 3 24   | 24/216-inch line spacing   |

This matches the line spacing to the height of the print head. After this, sending the CR and LF commands moves the vertical print position so the next line of graphics begins right where the previous line ended, with no space between.

Now send the data for the first line to the printer as follows:

<!-- formula-not-decoded -->

k

k
