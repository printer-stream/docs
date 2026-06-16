## C O N F I D E N T I A L

- ■ The functions used to define downloaded graphics data are this function and Function 84. Even with printer models that support both, it is recommended that only one of the functions be used for data definition tasks.
- The two functions differ only in that one function (this function) defines data in raster format, while the other (Function 84) defines data in column format. The domains and control information are identical.
- In cases where the key code specified by this function coincides with a key code being used by Function 84, a new data definition is created.
- ■ Use this function at the beginning of the line when the standard mode is selected.
- ■ This function is incompatible with macros, so make sure to avoid including it when defining macros.
- ■ In cases where there is insufficient capacity available for storing downloaded graphics data, this function cannot be used. Use Function 52 to confirm the available capacity in the downloaded graphics data area.
- ■ One option is to delete items of downloaded graphics data that were previously defined to the same key code.
- ■ The data for byte k of d1 ... dk is processed as a single item of defined downloaded graphics data. The defined data ( d ) specifies '1' for bits corresponding to dots that will be printed and '0' for bits corresponding to dots that will not be printed.
- ■ Downloaded graphics data is defined using the dot density set by Function 49.
- ■ Specify single data groups [ c d1 ... dk ] when monochrome is selected ( b = 1) as the color.
- ■ Specify b number of data groups [ c d1 ... dk ] when multiple colors are selected ( b ≠ 1). It is also important to specify different colors in units of data groups when specifying color ( c ).
- ■ Downloaded graphics data is printed using Function 85.
- ■ Note that it is not possible to create definitions for both downloaded graphics data (this command) and downloaded bit image data ( GS ✻ ). Downloaded bit image data definitions are deleted when this command is used.
- ■ For some models, downloaded graphics (this command) and user-defined characters ( ESC &amp; ) cannot be defined simultaneously.
- User-defined characters defined are deleted by using this command.
