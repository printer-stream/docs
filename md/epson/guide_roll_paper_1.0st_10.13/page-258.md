## **C O N F I D E N T I A L** 

## **GS ( L** _**pL pH m fn kc1 kc2 x y** <_ Function 69> 

- [Name] Print the specified NV graphics data. 

[Format] ASCII GS ( L pL pH m fn kc1 kc2 x y Hex 1D 28 4C 06 00 30 45 kc1 kc2 x y Decimal 29 40 76 6 0 48 69 kc1 kc2 x y [Range] (pL + pH × 256) = 6 (pL = 6, pH = 0) 

   - m = 48 

   - fn = 69 

   - 32 ≤ kc1 ≤ 126 

   - 32 ≤ kc2 ≤ 126 

   - TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60 : x = **1** , **2** , y = **1** , **2** 

- [Description] Prints the NV graphics data defined by the key codes (kc1 and kc2). 

      - Users have the option of specifying horizontal (times x) × vertical (times y) size settings for the selected data. 

- [Notes] 

- This function is used to print NV graphics data defined using Functions 67 and 68 of this command. 

- The printer only prints when NV graphics data corresponding to the specified key code is present. 

- Use this function when the printer enters the “beginning of the line” or “no data in print buffer” state during standard mode. 

- Note that during page mode, printing operations will not be performed simply because image data has been stored to the print buffer. 

- NV graphics data that exceeds the print area for one line will not be printed. 

- The scales for width and height of graphics are specified by (x, y). Therefore, in page mode with 90 ° or 270 ° clockwise-rotated graphics, the printer applies print area and dot density from [x: direction of paper feed, y: perpendicular to direction of paper feed]. 

- Settings for text effect (bold, underline, orientation, etc. except for upside-down) and font size do not affect the printing of the NV graphics data. 
