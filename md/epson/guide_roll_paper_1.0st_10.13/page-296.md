## **C O N F I D E N T I A L** 

- yL and yH specify the number of dots in the vertical direction as (yL + yH × 256). 

- d specifies the stored data (column format). 

- k indicates the number of the graphics data. k is an explanation parameter; therefore it does not need to be transmitted. 

## [Notes] 

- The functions used to store graphics data directly to the print buffer are this function and Function 112. Even with printer models that support both, it is recommended that only one of the functions be used for data definition tasks. 

- The two functions differ only in that one function (this function) defines data in raster format, while the other (Function 112) defines data in column format. 

- Use this function when the printer enters the “beginning of the line” or “except for graphic data, no data in print buffer” state during the standard mode. 

- This function is incompatible with macros, so make sure to avoid including it when defining macros. 

- Graphics data that exceeds the print area for one line will not be printed. 

- The scales for width and height of graphics are specified by (x, y). Therefore, in page mode with 90 ° or 270 ° clockwise-rotated graphics, the printer applies print area and dot density from [x: direction of paper feed, y: perpendicular to direction of paper feed]. 

- Settings for text effect (bold, underline, orientation) and font size do not affect the printing of the graphics data. 

- Print position does not change before and after this function is used. Overprinting of data of multiple colors can be performed by simply changing the selected color (c) and running this function again, but it is impossible to specify the same color to overprint. 

- Use Function 50 to print graphics after graphics data has been stored in the print buffer when the standard mode is selected. 

- The data for byte k of d1 ... dk is processed as a single item of defined graphics data. The defined data (d) specifies “1” for bits corresponding to dots that will be printed and “0” for bits corresponding to dots that will not be printed. 

- Graphics data is defined using the dot density set by Function 49. 

- During processing of this function, real time commands aren’t available. 
