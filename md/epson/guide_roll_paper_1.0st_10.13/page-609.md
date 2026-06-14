## **C O N F I D E N T I A L GS ( k** <Function 081> 

- [Name] PDF417: Print the symbol data in the symbol storage area 

- [Format] ASCII GS ( k pL pH cn fn m Hex 1D 28 6B 03 00 30 51 m Decimal 29 40 107 3 0 48 81 m 

- [Range] (pL + pH × 256) = 3 (pL = 3, pH = 0 ) cn = 48 fn = 81 

   - m = 48 

- [Description] Encodes and prints the PDF417 symbol data in the symbol storage area using the process of <Function 080>. 

- [Notes] ■ In standard mode, use this function when printer is “at the beginning of a line,” or “there is no data in the print buffer.” 

   - A symbol that size exceeds the print area cannot be printed. 

   - If there is any error described below in the data of the symbol storage area, it cannot be printed. 

      - There is no data (Function 080 is not processed). 

      - If [(number of columns × number of rows) < number of codeword] when auto processing is specified for number of columns and number of rows. 

      - Number of codeword exceeds 928 in the data area. 

   - The following data are added automatically by the encode processing. 

      - Start pattern and stop pattern 

      - Indicator codeword of left and right 

      - The descriptor of symbol length (the first codeword in the data area) 

      - The error correction codeword calculated by modulus 929 

      - Pad codeword 
