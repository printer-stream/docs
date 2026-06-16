## Sending Graphics Data

| ESC/P 2   | ESC/P   | 9-Pin ESC/P   |
|-----------|---------|---------------|

Two kinds of graphics printing are possible: bit-image and raster graphics. Although both types of graphics are based on bits in the data bytes, the relationship between the data order and dot printing differs.

## Bit Image

- Bit-image graphics was developed with the layout of the print head in mind. Data is organized to correspond to columns of print head output. Printing takes place after each complete line is sent.
- Bit-image graphics can be mixed with text printing.
- Bit-image graphics is available on all printers.

## Raster Graphics

- Raster graphics treats data in essentially the same way as video displays and laser printers. Data is sent in one-dot high lines. The printer reorganizes the data internally to correspond to the print head layout. Printing may not take place at the end of the line.
- There are two levels of raster graphics: standard and extended. Standard raster graphics is available only on ESC/P 2 printers. Extended raster graphics is available only on the Stylus COLOR and later high-resolution ESC/P 2 printer models.
- Standard raster graphics has a special data compression feature that allows you to economize on the data necessary to print graphics. Extended raster graphics provides two additional data compression schemes.
- Text and raster graphics printing cannot be combined on the same page.

The illustrations below show the difference between raster and bit-image data processing.

<!-- image -->
