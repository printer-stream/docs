Rev.2.52 

## **GS c** 

Name Print counter Code ASCII GS c Hex. 1D 63 Decimal 29 99 

Function After expanding the current serial counter value as print data (a character string) to the print buffer, the printer counts up or counts down according to the count mode. 

- Details • The counter value expanded to the print buffer the printer prints by either the print instruction or by a print buffer full. 

   - The counter print mode is set by GS C 0. 

   - The counter mode is set by GS C 1, or GS C ;. 

   - In the count up mode, if the counter value specified by this command goes out of the counter operating range, specified by GSC1 or GSC;, it is forced to convert to the minimum value by the execution of this command. 

   - In the count down mode, if the counter value specified by this command goes out of the counter operating range, specified by GSC1 or GSC;, it is forced to convert to the maximum value by the execution of this command. 

Reference GS C 0, GS C 1, GS 2, GS C ; 

ESC/POS Command Specifications 

147 
