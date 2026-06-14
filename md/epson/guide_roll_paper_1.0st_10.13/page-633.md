## **C O N F I D E N T I A L** 

- When mode 3 is selected, the Primary Message includes all data except the following. 

|**Factor of Primary Message**|**Number of data**|**Character**|
|---|---|---|
|Postal code|1 ~ 6 byte|Code set A|
|ISO country code|1 ~ 3 byte|Numeric|
|Class of service code|1 ~ 3 byte|Numeric|



- When using Mode 2 or 3, execute the process as listed below: 

   - (RS, GS indicates control code of MaxiCode (RS = 1EH, GS = 1DH). “yy” indicates numeric data of 2 byte.) 

   - a) When the top of symbol data is “[)>” RS “01” GS “yy”, these 9 bytes of data are treated as header 

      - Next data of the header is treated as Primary Message. 

      - When printing, header is set to top of Secondary Message. 

   - b) When the top of symbol data is not “[)>” RS “01” GS “yy”, the data is treated as Primary Message. 

   - c) In Primary Message, GS separate message into Postal code and ISO country code and Class of service. This GS is disregarded. 

   - d) In Primary Message, it does not check each code. 

      - (ex: specified Postal code and correct Postal code. etc.) 

   - e) All data of Secondary message is treated as symbol data. (In Secondary Message, GS is treated as symbol data.) 

- In mode 4, 5 and 6, all of the data in the symbol storage area is treated as Primary Message and Secondary Message. It does not check each code. 

- MaxiCode employs the Reed-Solomon Error Detection and Correction algorithm for error correction codeword. 

- The following data are added automatically by the encode processing. 

   - Finder Pattern 

   - Orientation Pattern 

   - Error correction codewords 

   - Mode indicator 

   - Pad codeword 
