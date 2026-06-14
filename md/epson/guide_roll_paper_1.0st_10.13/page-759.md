## **C O N F I D E N T I A L** 

- Changes the data of the user-defined code page that is copied into the work area by Function 7. 

- If data in the user-defined code pages is not copied into the work area, this function is not available. In this case, execute Function 7 first. 

- Definition data (d) specifies a bit printed to 1 and not printed to 0. The data to define a character is (y × x) bytes. 

- When defining the character of the Font No. 10 (configuration: 9 × 17), only the MSB can be used in the third byte for vertical direction. All bits can be used when defining characters of other fonts. 

- Definition data (d) defines the x dots pattern from the left side of the characters. When x is smaller than the number of dots composing the built-in character, any remaining dots on the right side are blank. 

- Deletes the character data defined in the same code. 

- Function 9 can also define character data. It is recommended that either of the functions be used, even if both functions are supported. 

   - Definition area and printing results are the same in both functions, although Function 8 processes the data in column format, and Function 9 processes the data in raster format. 

- The relation between the definition data and printing result is as follows. 

Example: Characters composed of 24 × 12 dots (y = 3, x = 12) 

|d1|d4|d7|...|d28|d31|d34|MSB<br>LSB<br>MSB<br>LSB<br>MSB<br>LSB|
|---|---|---|---|---|---|---|---|
|d2|d5|d8|...|d29|d32|d35||
|d3|d6|d9|...|d30|d33|d36||



[Model-dependent variations] 

## TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-P60, TM-U220 

## TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-P60, TM-U220 

**This printer doesn’t support this function.** 
