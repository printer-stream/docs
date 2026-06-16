ESC/P 2 has new commands that allow for easier vertical and horizontal movement of the print position.

These new commands are:

| ESC (U   | Sets a unit that is used for moving the print position and setting the page format   |
|----------|--------------------------------------------------------------------------------------|
| ESC ( V  | Sets the absolute vertical position on the page                                      |
| ESC ( v  | Sets the relative vertical position on the page                                      |

Horizontal movement is performed with commands available in previous ESC/P versions. However, now the increment of movement is the unit set with the ESC ( U command.

ESC $

ESC \

Sets the absolute horizontal position

Sets the relative horizontal position

The following sections describe moving the print position, with explanations for both ESC/P 2 and previous ESC/P versions.

## Moving the horizontal position

| ESC/P 2   | ESC/P   | 9-Pin ESC/P   |
|-----------|---------|---------------|

The horizontal print position is defined as the position where the left-most printable column of dots is printed for the next character or graphics design.

When you print characters or spaces, the printer automatically moves the print position according to the pitch you select (or the width of each character if you select proportional spacing).

To move the the horizontal print position independent of character printing, the recommended commands are as follows:

ESC $

ESC \

HT

Set the absolute horizontal position

Set the relative horizontal position

Horizontal tab

The format of the ESC $ command is as follows:

ESC $ nL nH

The resulting horizontal position is determined by the formula below.

(horizontal position) = ((nH × 256) + nL) × (defined unit) + (left margin)

<!-- formula-not-decoded -->
