## **C O N F I D E N T I A L** 

   - When processing Function 081 or 082, the setting values of Functions 065 to 070 are used. If the printable area is not large enough, the symbol may not be printed. 

   - Executing Function 081 after executing Function 080 repeatedly prints the same symbol. 

   - By using Functions 065 to 070 combined with Function 081, the same symbol data d1...dk is printed differently. 

   - By using Function 082, the symbol size printed by Function 081 is available. 

- [Notes for process of QR Code symbol (when cn = 49)] 

   - The symbol data specified by Function 180 d1...dk is stored in the printer and is printed by Function 181. 

   - When processing Function 181 or 182, the setting values of Functions 165, 167, 169 are used. If the printable area is not enough, the symbol may not be printed. 

   - Executing Function 181 after executing Function 180 repeatedly prints the same symbol. 

   - By using Functions 165, 167, 169 combined with Function 181, the same symbol data d1...dk is printed differently. 

   - By using Function 182, the symbol size printed by Function 181 is available. 

- [Notes for process of MaxiCode symbol (when specify cn = 50)] 

   - The symbol data specified by Function 280 d1...dk is stored in the printer and is printed by Function 281. 

   - When processing Function 281 or 282, the setting values of Function 265 are used. If the printable area is not enough, the symbol may not be printed. 

   - Executing Function 281 after executing Function 280 repeatedly prints the same symbol. 

   - By using Functions 265 combined with Function 281, the same symbol data d1...dk is printed differently. 

   - By using Function 282, the symbol size printed by Function 281 is available. 

[Notes for 2-dimensional GS1 DataBar processing (when cn = 51 is specified)] 

- The 2-dimensional GS1 DataBar symbol data specified by <Function 380> of this command (d1...dk) is temporarily stored in the storage area of the printer and is printed by <Function 381>. 

- The setting value of <Function 367> is used when processing <Function 381> and <Function 382> of this command. Furthermore, the setting value of <Function 371> is used when processing GS1 DataBar Expanded Stacked. If the printing area is narrow, it may not be possible to print the symbol. 
