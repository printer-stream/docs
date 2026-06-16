## C O N F I D E N T I A L

## GS ( L pL pH m fn x y &lt;Function 49&gt;

```
[Name] Set the reference dot density for graphics. [Format] ASCII GS ( L pL pH m fn x y Hex 1D 28 4C 04 00 30 fn x y Decimal 29 40 76 4 0 48 fn x y [Range] ( pL + pH × 256) = 4 ( pL = 4, pH = 0) m = 48 fn = 1, 49 x = 50, 51 y = 50 [when x = 50] y = 51 [when x = 51]
```

[Description]

[Notes]

Sets the reference dot density to process the graphics data or bit image data. (dpi: dots per inch)

- [180 dpi × 180 dpi] is selected when x = 50 and y = 50
- [360 dpi × 360 dpi] is selected when x = 51 and y = 51
- ■ Note that certain settings for this function may affect the processing of the types of graphics and bit image data listed in the table below.
- ■ Command: GS ( L and GS 8 L

| Function no.   | Function name                                                |
|----------------|--------------------------------------------------------------|
| Function 67    | Define the NV graphics data (raster format).                 |
| Function 68    | Define the NV graphics data (column format).                 |
| Function 83    | Define the download graphics data (raster format).           |
| Function 84    | Define the download graphics data (column format).           |
| Function 112   | Store the graphics data in the print buffer (raster format). |
| Function 113   | Store the graphics data in the print buffer (column format). |
