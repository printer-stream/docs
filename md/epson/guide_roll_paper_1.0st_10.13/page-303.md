## **C O N F I D E N T I A L** 

[Description] Defines the NV bit image in the NV graphics area. 

- n specifies the number of defined NV bit images. 

- xL, xH specifies (xL + xH × 256) bytes in the horizontal direction for the NV bit image you defined. 

- yL, yH specifies (yL + yH × 256) bytes in the vertical direction for the NV bit image you defined. 

- d specifies the definition data for the NV bit image (column format). 

- k indicates the number of the definition data. k is an explanation parameter; therefore it does not need to be transmitted. 

## [Recommended Functions] 

This function is supported only by some printer models and may not be supported by future models. It is recommended that NV graphics function (GS ( L GS 8 L: <Function 51> and <Function 64> ~ <Function 69>) be used instead of FS q because the NV graphics function offers the following additional features: 

- Multiple logo data and mark data can be specified (except for some models). 

- Data can be controlled by key code. 

- Redefining or deleting is possible for each key code. 

- Color can be specified for the definition data. 

- Data can be defined by raster format. 

- The remaining capacity of the definition area can be confirmed. 

- Continuous processing possible (without a software reset when a command has been processed). 

## [Notes] 

- NV bit image means a bit image which is defined in a non-volatile memory. The NV bit image defined is effective until the next NV bit image is defined. 

- In standard mode, this command is effective only when processed at the beginning of the line. 

- If this command is processed while a macro is being defined, the printer cancels macro definition and starts processing this command. At this time, the macro becomes undefined. 

- k bytes data of d1...dk is processed as a defined data of a NV bit image. The defined data (d) specifies a bit printed to 1 and not printed to 0. 

- All NV bit images previously defined are canceled. 
