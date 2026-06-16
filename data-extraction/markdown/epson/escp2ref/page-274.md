| ESC/P 2   | ESC/P   | 9-Pin ESC/P   |
|-----------|---------|---------------|

The following attributes are limited during draft printing:

- Typeface Draft typeface only
- Point size 10.5 and 21-point sizes only

Use the ESC x command to select the print quality, according to the following format:

| ESC x 0   | Selects draft print quality                                                              |
|-----------|------------------------------------------------------------------------------------------|
| ESC x 1   | Selects LQ print quality for ESC/P 2 and ESC/P Selects NLQ print quality for 9-Pin ESC/P |

Standard and scalable fonts (multipoint mode)

<!-- image -->

Both ESC/P 2 and previous ESC/P level printers can print the standard 10.5point fonts. You can modify the point size (height) and pitch of these characters with the following commands:

| Size    |                                         |
|---------|-----------------------------------------|
| SO,ESCW | Double-width printing                   |
| ESCw    | Double-height printing                  |
| SI      | Condensed printing                      |
| Spacing |                                         |
| ESC P   | Select 10 cpi                           |
| ESCM    | Select 12 cpi                           |
| ESC g   | Select 15 cpi (24/48-pin printers only) |
| ESC p   | Select proportional spacing             |
| ESC SP  | Add additional space between characters |

By using ESC/P 2's ESC X command to enter multipoint mode, you can select scalable fonts. Scalable fonts allow you to directly specify the point size and pitch of your characters.

Not all typefaces are available in multipoint mode; see the Command Table for the typefaces available in multipoint mode on each printer.
