## C O N F I D E N T I A L

|   50 | Color 2   |
|------|-----------|
|   51 | Color 3   |
|   52 | Color 4   |

- xL and xH specify the number of dots in the horizontal direction as ( xL + xH × 256).
- yL and yH specify the number of dots in the vertical direction as ( yL + yH × 256).
- d specifies the stored data (raster format).
- k indicates the number of the graphics data. k is an explanation parameter; therefore it does not need to be transmitted.
- ■ The functions used to store graphics data directly to the print buffer are this function and Function 113. Even with printer models that support both, it is recommended that only one of the functions be used for data definition tasks.
- The two functions differ only in that one function (this function) defines data in raster format, while the other (Function 113) defines data in column format.
- ■ Use this function when the printer enters the 'beginning of the line' or 'except for graphic data, no data in print buffer' state during the standard mode.
- ■ This function is incompatible with macros, so make sure to avoid including it when defining macros.
- ■ NV graphics data that exceeds the print area for one line will not be printed.
- ■ The scales for width and height of graphics are specified by ( x , y ). Therefore, in page mode with 90 ° or 270 ° clockwise-rotated graphics, the printer applies print area and dot density from [ x : direction of paper feed, y : perpendicular to direction of paper feed].
- ■ Settings for text effect (bold, underline, orientation) and font size do not affect the printing of the NV graphics data.
- ■ Print position does not change before and after this function is used. Overprinting of data of multiple colors can be performed by simply changing the selected color ( c ) and running this function again, but it is not possible to specify the same color to overprint.
- ■ Use Function 50 to print graphics after graphics data has been stored in the print buffer when the standard mode is selected.

## [Notes]
