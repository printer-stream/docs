## **C O N F I D E N T I A L GS ( k** <Function 281> 

- [Name] MaxiCode: Print the symbol data in the symbol storage area 

- [Format] ASCII GS ( k pL pH cn fn m Hex 1D 28 6B 03 00 32 51 m Decimal 29 40 107 3 0 50 81 m 

- [Range] (pL + pHpL + pHL + pH + pHpHH × 256) = 3 (pL =pL =L == 3, pHH = 0 ) cn = 50 fn = 81 

- [Range] (pL + pHpL + pHL + pH + pHpHH × 256) = 3 (pL =pL =L == 3, pHH = 0 ) 

   - m = 48 

- [Description] Encodes and prints the MaxiCode symbol data in the symbol storage area using the process of <Function 280>. 

- [Notes] ■ In standard mode, use this function when printer is “at the beginning of a line,” or “there is no data in the print buffer.” 

   - If the symbol size exceeds the print area, the symbol cannot be printed. 

   - If there is any error described below in the data of the symbol storage area, it cannot be printed. 

      - There is no data (Function 180 is not processed). 

      - When using only numeric characters, the data is more than 138 characters. 

      - When using alphanumeric characters, the data is more than 93 characters. 

      - When Mode 2 is selected, the Primary Message includes all data except the following. 

|**Factor of Primary Message**|**Number of data**|**Character**|
|---|---|---|
|Postal code|1 ~ 9 byte|Numeric|
|ISO country code|1 ~ 3 byte|Numeric|
|Class of service code|1 ~ 3 byte|Numeric|
