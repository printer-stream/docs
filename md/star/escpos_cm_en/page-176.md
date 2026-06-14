Rev.2.52 

## **GS ( M pL pH n m (Function Code: n = 1, 49)** 

Name Save black mark adjustment value Code ASCII GS ( M pL pH n m Hex. 1D 28 4D pL pH n m Decimal 29 40 77 pL pH n m 

Defined Region (pL+pHx256) = 2, pL = 2, pH = 0 n = 1, 49 

1 ≤ m ≤ 3, 49 ≤ m ≤ 51 

Function • Saves the black mark adjustment value set by the GS (F command to the mth region in the volatile memory. 

After saving to a non-volatile memory, the printer is reset. 

|Function|n = 1, 49<br>1≤m≤3, 49≤m≤51<br>• Saves the black mark adjustment value set by the GS (F command to the mth regio<br>volatile memory.<br>After saving to a non-volatile memory, the printer is reset.|
|---|---|
|m|Function|
|1|Saves the adjustment value to the 1stsavingregion of the non-volatile memory.|
|2|Saves the adjustment value to the 2ndsavingregion of the non-volatile memory.|
|3|Saves the adjustment value to the 3rdsavingregion of the non-volatile memory.|



Reference 

Consider the life of the non-volatile memory and avoid over-use of this command. GS ( F 

ESC/POS Command Specifications 

176 
