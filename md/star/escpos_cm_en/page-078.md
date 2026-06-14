Rev.2.52 

## **FS g 1 m a1 a2 a3 a4 nL nH d1 ... dk** 

Name Write data to user NV memory 

Code ASCII FS g 1 m a1 a2 a3 a4 nL nH  d1...dk Hex. 1C 67 31 m a1 a2 a3 a4 nL nH  d1...dk Decimal 28 103 49 m a1 a2 a3 a4 nL nH  d1...dk 

m = 0 Defined Region 

0 ≤ {a1+ (a2×256) + (a3 × 65536) + (a4×16777216) } ≤ 1023 

1 ≤ {nL+ (nH×256) } ≤ 1024 32 ≤ d ≤ 255 k = {nL+ (nH×256) } Function Stores data in the user NV memory. 

   - m is fixed at 0. 

   - a1, a2, a3 and a4 specify the data storage addresses {a1 + (a2 x 256) + (a3 x 65536) + (a4 x 16777216)}. 

   - nL and nH specify the storage data count in byes of {nL+ (nH x 256)}. 

   - d specifies the stored data. 

- Details • The user NV memory is a storage region dedicated for character data that is ensured on a non-volatile memory. 

   - This command is effective only when input at the top of the line when standard mode is being used. 

   - When in page mode, this command is invalid. 

   - When processing this command while defining a macro, the macro definition is terminated and the command commences with processing. 

   - This command is ignored and subsequent data is processed as normal data if the argument (m), storage starting address (a1, a2, a3, a4), and the storage data count (nL, nH) are out of the definition, or if [{the storage starting address (a1, a2, a3, a4) + storage data count (nL, nH)}  ≥ 1024. 

   - This command is completed when the storage data (d) out of the definition is processed, and subsequent data is processed as normal data.  At this time, data that has already been processed is stored in memory. 

   - The data storage process executes an overwrite. 

Therefore, data that is already stored in the region is erased. 

- A memory or gate array R/W error occurs when a writing error occurs. 

- Data in the user NV memory can be read using FS g 2 (Read user NV memory data). 

- User NV memory data is not initialized with the following. 

- a. ESC@ : Initialize printer 

- b. FS q: Define NV bit image 

- c. When the printer is reset or the power is turned off 

ESC/POS Command Specifications 

78 
