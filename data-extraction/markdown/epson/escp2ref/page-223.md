## Binary Mode Commands

To accommodate the high-resolution printing capabilities of the Stylus COLOR printer, EPSON has added a raster graphics data compression mode to the existing ESC/P 2 graphics command set: ESC . 2 TIFF compression. This new compression mode also required the introduction of a set of binary commands. For detailed information on programming in compressed raster graphics mode, see the discussion in Recommended Operations.

Binary commands are available only when a compressed raster graphics mode is selected with the ESC . 2 command. In this mode the band height m is always set to 1. The binary commands applicable to the TIFF compression mode are listed below.

&lt;XFER&gt; Transfer raster graphics data &lt;MOVX&gt; Set relative horizontal position &lt;MOVY&gt; Set relative vertical position &lt;COLR&gt; Select printing color &lt;CR&gt; Carriage return to left-most print position &lt;EXIT&gt; Exit TIFF compressed mode &lt;MOVXBYTE&gt; Set &lt;MOVX&gt; unit to 8 dots (one byte) &lt;MOVXDOT&gt; Set &lt;MOVX&gt; unit to 1 dot

The command descriptions for the binary mode commands follow.
