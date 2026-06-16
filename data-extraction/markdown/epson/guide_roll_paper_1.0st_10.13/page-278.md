## C O N F I D E N T I A L

- b specifies the number of colors for the defined data.
- xL and xH specify the number of dots in the horizontal direction as ( xL + xH × 256).
- yL and yH specify the number of dots in the vertical direction as ( yL + yH × 256).
- c specifies the color of the defined data.
- d specifies the defined data (raster format).
- k indicates the number of the definition data. k is an explanation parameter; therefore it does not need to be transmitted.
- ■ In cases where the specified key code already exists in memory, it will be necessary to overwrite the data.
- ■ Downloaded graphics indicate image data groups defined in the printer's internal volatile memory (RAM). Once the download graphics data have been defined, they are available until GS ( L &lt;Function 83&gt;, &lt;Function 84&gt; or ESC @ is executed. The download graphics data are lost when the power is turned off or the printer is reset.
- ■ The functions used to define download graphics data are this function and Function 83. Even with printer models that support both, it is recommended that only one of the functions be used for data definition tasks.
- The two functions differ only in that one function (this function) defines data in raster format, while the other (Function 83) defines data in column format. The domains and control information are identical.
- In cases where the key code specified by this function coincides with a key code being used by Function 83, a new data definition is created.
- ■ Use this function at the beginning of the line when the standard mode is selected.
- ■ This function is incompatible with macros, so make sure to avoid including it when defining macros.

|   c | Color specification   |
|-----|-----------------------|
|  49 | Color 1               |
|  50 | Color 2               |
|  51 | Color 3               |

## [Notes]
