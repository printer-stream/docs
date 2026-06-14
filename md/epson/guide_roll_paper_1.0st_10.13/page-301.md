## **C O N F I D E N T I A L** 

## **GS D** _**m fn a kc1 kc2 b c d1...dk**_ <Function 83> 

EXECUTING + SETTING 

[Name] Define Windows BMP download graphics data. 

[Format] ASCII GS D m fn a kc1 kc2 b c d1...dk Hex 1D 44 m fn a kc1 kc2 b c d1...dk Decimal 29 68 m fn a kc1 kc2 b c d1...dk 

- [Range] m = 48, fn = 83, a = 48 

   - 32 ≤ kc1 ≤ 126 (20h ≤ **kc1** ≤ 7Eh) 

   - 32 ≤ kc2 ≤ 126 (20h ≤ **kc2** ≤ 7Eh) 

   - c = 49 

0 ≤ d ≤ 255 

TM-T20 **:** b **= 48** TM-T88V **:** b **= 48, 52** 

The value of k depends on the BMP file size. 

- [Description] Converts Windows BMP data to the specified tone and defines download graphics data (raster format) that corresponds to the key codes (kc1, kc2). 

      - b specifies the tone of data to define. 

   - b **Tone of data to define** 48 Monochrome (digital) 52 Multi-tone 

      - c specifies the color of data to define. 

|•|cspecifies the color of data t|
|---|---|
|c|**Color of data to define**|
|49|Color 1|



- d specifies the defined data (raster format). 
