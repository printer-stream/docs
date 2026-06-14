## **C O N F I D E N T I A L** 

- The graphics functions provided here maintain upward compatibility with conventional bit image processing. 

|processing.||
|---|---|
|**Graphics type**|**Corresponding bit image command**(*1)|
|NV graphics|FS p, FS q|
|Download graphics|GS✻, GS /|
|Graphics|GS Q 0, GS v 0|



- (*1) These commands are supported by some of the printer models but will not be supported by future models. 

- The various graphics functions (of this command), more user-friendly than conventional bit image functions, offer the following advantages. 

   - Definition of multiple items of logo mark and insignia data (with most functions). 

   - Management of data using key codes. 

   - Deletion of and redefinition of data per key code. 

   - Color coding of image-data. 

   - Definition of image-data in both raster and column formats. 

   - Confirmation of available capacity in domain. 

   - Continuous processing possible (without a software reset when a command has been processed). 

- The following three types of graphics functions are included. 

   - NV graphics [Functions 48, 51, 64, 65, 66, 67, 68, and 69] Stores data in non-volatile memory. Defined data is retained when power is turned off. There is a limit on the number of times that non-volatile memory can be written to. 

   - Download graphics [Functions 52, 80, 81, 82, 83, 84, and 85] Stores data in volatile memory (RAM). 

Defined data is lost when the ESC @ command is executed, the system is reset, or power is turned off. 
