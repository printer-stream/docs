Only the following commands are available in standard raster graphics mode:

| LF      | Line feed                                      |
|---------|------------------------------------------------|
| CR      | Carriage return                                |
| ESC .   | Print raster graphics                          |
| ESC . 1 | Enter RLE compressed mode                      |
| ESC . 2 | Enter TIFF compressed mode (Stylus COLOR only) |
| ESC ( c | Set page format                                |
| ESC ( V | Set absolute vertical position                 |
| ESC $   | Set absolute horizontal position               |
| ESC r   | Select printing color                          |
| ESC +   | Set n/360-inch line spacing                    |
| FF      | Form feed                                      |
| ESCEM   | Control paper loading/ejecting                 |
| ESC @   | Initialize printer (exit graphics mode)        |
| ESC ( C | Set page length in defined unit                |
| ESC ( v | Set relative vertical position                 |
| ESC \   | Set relative horizontal position               |
| ESCU    | Turn unidirectional on/off                     |
| ESC (U  | Set unit                                       |
| ESC ( i | MicroWeave (Stylus COLOR only)                 |

The following subset of binary mode commands is available in extended raster graphics mode, entered by sending the ESC . 2 command. All other commands are ignored.

&lt;XFER&gt; Transfer raster graphics data &lt;MOVX&gt; Set relative horizontal position &lt;MOVY&gt; Set relative vertical position &lt;COLR&gt; Select printing color &lt;CR&gt; Carriage return to left-most print position &lt;EXIT&gt; Exit TIFF compressed mode &lt;MOVXBYTE&gt; Set &lt;MOVX&gt; unit to 8 dots &lt;MOVXDOT&gt; Set &lt;MOVX&gt; unit to 1 dot

Other commands not listed above are ignored. Also, text cannot be sent during graphics mode.

## Standard raster graphics

ESC/P 2

Raster graphics allows the programmer to send image data in a format similar to that used by televisions, VDT monitors, and laser printers.

Follow these steps to prepare and send raster graphics:

1. Determine the dot density (resolution) of your image.
