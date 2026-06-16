Before sending data, you must also determine the width of your graphics image. The width is also specified in number of dots. Of course, data must be sent in bytes; all data beyond the dot width specified is ignored.

The following illustration shows the dot width and the ignored data.

<!-- image -->

Determine the dot-width parameters for the ESC . command as follows:

<!-- formula-not-decoded -->

Use a combination of the ESC ( V, ESC ( v, ESC $, or ESC \ commands to set the beginning position of the first graphics band. The print position corresponds to the position of the first printable dot in your image.

<!-- image -->
