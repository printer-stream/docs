## **C O N F I D E N T I A L** 

|fn|**Function No.**|**Function name**|
|---|---|---|
|112|**Function 112**|Store the graphics data in the print buffer (raster format).|
|113|**Function 113**|Store the graphics data in the print buffer (column format).|



- pL, pH specifies (pL + pH × 256) as the number of bytes after pH (m, fn, and [parameters]). 

- p1, p2, p3, and p4 specify (p1 + p2 × 256 + p3 × 65536 + p4 × 16777216) as the number of bytes after pH (m, fn, and [parameters]). 

- Description of the [parameters] is described in each function. 

## ■ Differences between GS ( L and GS 8 L 

- All commands possess the same functions for “Graphics data processing.” 

- Specifications (conventions) concerning function code (fn) are identical, while only the parameters (pL, pH, p1, p2, p3, and p4) used to specify the parameter values from m differ. 

|**Command**|**Description**|
|---|---|
|GS ( L|Parameter value is 2 bytes less than that forGS 8 L.<br>Used to fix the parameter value.<br>Used when sending data divided into blocks.|
|GS 8 L|Possesses powerful range of expression.<br>Used for batch transfer of large volumes of data.|



- Be sure to use GS 8 L when the parameter value exceeds 65535 bytes for Functions 67, 68, 83, 84, 112, and 113. 

## [Recommended Functions] 

- This command is recommended for use when printing image data. 

- The image processing controlled using this command is referred to as the “Graphics function.” The name is important as it distinguishes it from conventional bit image functions. 
