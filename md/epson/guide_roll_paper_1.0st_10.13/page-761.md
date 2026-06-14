## **C O N F I D E N T I A L** 

- If the data in the user-defined code pages is not copied into the work area, this function is not available. In this case, execute Function 7 first. 

- Definition data (d) specifies a bit printed to 1 and not printed to 0. The data to define a character is (x × y) bytes. 

- When defining the character of the Font No. 10 (configuration: 9 × 17), only the MSB can be used in the second byte for horizontal direction. When defining the character of the Font No. 12 (configuration: 12 × 24), only the upper four bits can be used in the second byte for horizontal direction. All bits can be used when defining characters of other fonts. 

- Definition data (d) defines the y dots pattern from the top of the characters. When y is smaller than the number of dots composing the built-in character, any remaining dots below are blank. 

- Deletes the character data defined in the same code. 

- Function 8 can also define character data. It is recommended that either of the functions be used even if both functions are supported. 

   - Definition area and printing results are the same in both functions, although Function 8 processes the data in column format, and Function 9 processes the data in raster format. 

- The relation between the definition data and printing result is as follows. 

Example: Characters composed of 24 × 12 dots (x = 2, y = 24) 

The second bytes in the horizontal position use 4 bits of the MSB. 

|d1|d2|
|---|---|
|d3|d4|
|:|:|
|d45|d46|
|d47|d48|



MSB    LSB MSB    LSB 

[Model-dependent variations] 

## TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-U220 

## TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-U220 

**This printer doesn’t support this function.** 
