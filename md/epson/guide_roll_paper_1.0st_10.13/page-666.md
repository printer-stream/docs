## **C O N F I D E N T I A L** 

- Automatically adds a separator to the line element and 2D composite element. 

- The quiet zone is not included in the printing data. Be sure to include the quiet zone when using this function. 

## [Notes for EAN8, EAN13, and UPC-A] 

- The data shown below is added automatically in encoding. 

   - Modular check character (1 character) 

   - Guard bar 

## [Notes for UPC-E (0 omitted [6 digit] version) 

   - Calculates the modular check character automatically. The modular check character is data for deciding the bar pattern, and is not included in the print data. 

   - Adds the guard bar automatically for encoding. 

- [Notes for UPC-E (0 not omitted [11 digit] version)] 

   - Calculates the modular check character automatically. The modular check character is data for deciding the bar pattern, and is not included in the print data. 

   - A shortened 6-digit code (D1 to D6) generated from the (d2...d11) data in accordance with the table below is printed. 

|■A shortened 6-digit code (D1 to D6) generated from the (d2...d11)<br>below is printed.|■A shortened 6-digit code (D1 to D6) generated from the (d2...d11)<br>below is printed.|■A shortened 6-digit code (D1 to D6) generated from the (d2...d11)<br>below is printed.|■A shortened 6-digit code (D1 to D6) generated from the (d2...d11)<br>below is printed.|■A shortened 6-digit code (D1 to D6) generated from the (d2...d11)<br>below is printed.|■A shortened 6-digit code (D1 to D6) generated from the (d2...d11)<br>below is printed.|■A shortened 6-digit code (D1 to D6) generated from the (d2...d11)<br>below is printed.|■A shortened 6-digit code (D1 to D6) generated from the (d2...d11)<br>below is printed.|■A shortened 6-digit code (D1 to D6) generated from the (d2...d11)<br>below is printed.|■A shortened 6-digit code (D1 to D6) generated from the (d2...d11)<br>below is printed.|data in accordance with the table|data in accordance with the table|data in accordance with the table|data in accordance with the table|data in accordance with the table|data in accordance with the table|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Data of transmitted by host PC**||||||||||**Printing data**<br>**_D1_**<br>**_D2_**<br>**_D3_**<br>**_D4_**<br>**_D5_**<br>**_D6_**||||||
|**_d2_**|**_d3_**|**_d4_**|**_d5_**|**_d6_**|**_d7_**|**_d8_**|**_d9_**|**_d10_**|**_d11_**|||||||
|0~9|0~9|0|0|0|-|-|0~9|0~9|0~9|**_d2_**|**_d3_**|**_d9_**|**_d10_**|**_d11_**|0|
|0~9|0~9|1|0|0|-|-|0~9|0~9|0~9|**_d2_**|**_d3_**|**_d9_**|**_d10_**|**_d11_**|1|
|0~9|0~9|2|0|0|-|-|0~9|0~9|0~9|**_d2_**|**_d3_**|**_d9_**|**_d10_**|**_d11_**|2|
|0~9|0~9|3~9|0|0|-|-|-|0~9|0~9|**_d2_**|**_d3_**|**_d4_**|**_d10_**|**_d11_**|3|
|0~9|0~9|0~9|1~9|0|-|-|-|-|0~9|**_d2_**|**_d3_**|**_d4_**|**_d5_**|**_d11_**|4|
|0~9|0~9|0~9|0~9|1~9|-|-|-|-|5~9|**_d2_**|**_d3_**|**_d4_**|**_d5_**|**_d6_**|**_d11_**|



- Specify 0 at indicated data by "-" in the table. 

- When 1 ≤ d6 ≤ 9, be sure to specify (5 ≤ d11 ≤ 9). 
