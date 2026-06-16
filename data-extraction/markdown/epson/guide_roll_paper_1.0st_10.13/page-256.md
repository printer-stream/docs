## C O N F I D E N T I A L

- ■ The data for byte k of d1 ... dk is processed as a single item of defined NV graphics data. The defined data ( d ) specifies '1' for bits corresponding to dots that will be printed and '0' for bits corresponding to dots that will not be printed.
- ■ NV graphics data is defined using the dot density set by Function 49.
- ■ Specify single data groups [ c d1 ... dk ] when monochrome is selected ( b = 1) as the color.
- ■ Specify b number of data groups [ c d1 ... dk ] when multiple colors are selected ( b ≠ 1). It is also important to specify different colors in units of data groups when specifying color ( c ).
- ■ NV graphics data is printed using Function 69.
- ■ Note that it is not possible to create definitions for both NV graphics data (this command) and NV bit image data ( FS q ). NV bit image data definitions are deleted when this command is used.
- ■ The relationship between NV graphics data (column format) and print results is shown in the table below.

<!-- image -->

| d1   | dY +1   | ...   | :     |
|------|---------|-------|-------|
| d2   | dY +2   | ...   | dk -2 |
| :    | :       | ...   | dk -1 |
| dY   | dY x2   | ...   | dk    |

[Model-dependent variations]

Y = ( yL + yH ✕ 256)

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60

## TM-J2000/J2100

This printer is equipped with a print head configured in column format, which makes it faster to define data using this function than with Function 67 (raster format).

The [data value ( k ) + control information data value (32 bytes)] area of the NV graphics data domain is used when this function is executed.
