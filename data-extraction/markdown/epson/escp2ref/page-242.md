For single sheets, the printer calculates the page length as the distance between the top and bottom margins.

<!-- image -->

Also, to simplify movement of the horizontal and vertical print position, ESC/P 2 provides the ESC ( U command for setting the unit of movement and measurement. The page length is set with the ESC ( C command, based on this unit.

Always set the unit before setting the page length. The unit can be set as small as 1/360 inch; set the unit to the minimum size necessary for vertical and horizontal movement within the current print job.

## Note:

- Always set the page length before paper is loaded or when the print position is at the top-of-form position. Otherwise, the current print position becomes the top-of-form position, results in undesirable contradictions between the actual and logical page settings.
- Setting the page length cancels any previously set top or bottom margins.
- The maximum page length is 22 inches.
- Changing the unit after the page length has been set does not affect the page length.

The following commands set the page length to 11 inches, based on a unit of 1/360 inch.

| ESC ( U1010        | Sets a unit of 1/360 inch                        |
|--------------------|--------------------------------------------------|
| ESC ( C 2 0 120 15 | Selects a page length of 11 inches (3,960 units) |
