New commands are available in ESC/P 2 that simplify setting the vertical print position. These commands are:

ESC ( V

Set absolute vertical print position

ESC ( v

Set relative vertical print position

The unit of movement for both these commands is the unit set with the ESC ( U command. See ESC ( U in the Command Summary and 'Setting the page length' for more information.

The format for the ESC ( V command is as follows:

ESC ( V 2 0 mL mH

The resulting vertical position is determined by the following formula:

(vertical position) = ((mH × 256) + mL) × (defined unit) + (top-margin position)

<!-- formula-not-decoded -->

The format for the ESC ( v command is as follows:

<!-- formula-not-decoded -->

(horizontal position) = ((mH × 256) + mL) × (defined unit) + (current position)

To move in the positive direction (down the page), the formula is as follows:

<!-- formula-not-decoded -->

To move in the negative direction (up the page), the formula is as follows:

<!-- formula-not-decoded -->
