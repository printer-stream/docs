<!-- image -->

The method of setting the printing area differs between ESC/P 2 and former ESC/P levels. Both methods are described in the following sections.

With ESC/P 2, the following commands allow for improved page layout control:

- ESC ( U Set unit This command sets the unit for horizontal and vertical movement and

measurement. You can use this command to set the unit as small as 1/360 inch, allowing for precise page layout measurement.

- ESC ( C Set page length The page length is based on the unit set with the ESC ( U command.
- ESC ( c Set page format Based on the unit in ESC ( U, you can use this command to set the top and bottom margins. Because you can now set a top margin, the settings you make for the page actually match the physical page.

Because you can set the top and bottom margins for single-sheet paper, you can handle single-sheets the same as continuous paper.

Manually fed single sheets are now treated the same as paper fed from a cutsheet feeder (cut-sheet feeder mode has been eliminated).

<!-- image -->

Set the print area as follows:

1. Set the left and right margins.
2. Set the page length.
3. Set the top and bottom margins ESC/P 2 printers

Set the bottom margin only Non-ESC/P 2 printers (continuous paper only)
