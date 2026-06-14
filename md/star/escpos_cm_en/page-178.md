Rev.2.52 

## **GS ( M pL pH n m (Function Code: n = 3, 51)** 

Name Set black mark adjustment value auto-load when powering on Code ASCII GS ( M pL pH n m Hex. 1D 28 4D pL pH n m Decimal 29 40 77 pL pH n m 

Defined Region (pL+pHx256) = 2, pL = 2, pH = 0 n = 3, 51 1 ≤ m ≤ 3, 49 ≤ m ≤ 51 

Function Validates/invalidates the black mark adjustment value auto-load when powering on. 

After saving the setting to the non-volatile memory, the printer is reset. 

|Function|n = 3, 51<br>1≤m≤3, 49≤m≤51<br>Validates/invalidates the black mark adjustment value auto-load when powering on.<br>After saving the setting to the non-volatile memory, the printer is reset.|
|---|---|
|m|Function|
|0|Auto-load function invalid|
|1|Auto-loads the 1stadjustment value of the non-volatile memorywhenpoweringon.|
|2|Auto-loads the 2ndadjustment value of the non-volatile memorywhenpoweringon.|
|3|Auto-loads the 3rdadjustment value of the non-volatile memorywhenpoweringon.|



Consider the life of the non-volatile memory and avoid over-use of this command. Reference GS ( F 

ESC/POS Command Specifications 

178 
