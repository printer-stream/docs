## **C O N F I D E N T I A L** 

TM-T88V **:** b **= 1 (when** a **= 48) 1** ≤ b ≤ **4 (when** a **= 52)** 

- **1** ≤ **(** xL **+** xH × **256)** ≤ **8192 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **32) 1** ≤ **(** yL **+** yH × **256)** ≤ **2304 (0** ≤ yL ≤ **255, 0** ≤ yH ≤ **9)** c **= 49 (when** a **= 48) 49** ≤ c ≤ **52 (when** a **= 52)** 

Defines the downloaded graphics data (raster format) as a record specified by the key codes (kc1 and kc2) in the downloaded graphics area. 

- b specifies the number of colors for the defined data. 

- xL and xH specify the number of dots in the horizontal direction as (xL + xH × 256). 

- yL and yH specify the number of dots in the vertical direction as (yL + yH × 256). 

- c specifies the color of the defined data. 

|c|**Color specifications**|
|---|---|
|49|Color 1|
|50|Color 2|
|51|Color 3|
|52|Color 4|



   - d specifies the defined data (raster format). 

   - k indicates the number of the definition data. k is an explanation parameter; therefore it does not need to be transmitted. 

- In cases where the specified key code already exists in memory, it will be necessary to overwrite the data. 

## [Notes] 

- Downloaded graphics indicate image data groups defined in the printer’s internal volatile memory (RAM). Once the download graphics data have been defined, they are available until GS ( L <Function 83>, <Function 84> or ESC @ is executed. The download graphics data are lost when the power is turned off or the printer is reset. 
