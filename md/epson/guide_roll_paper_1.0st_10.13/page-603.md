## **C O N F I D E N T I A L GS ( k** <Function 069> 

[Name] PDF417: Set the error correction level 

[Format] ASCII GS ( k pL pH cn fn m n Hex 1D 28 6B 04 00 30 45 m n Decimal 29 40 107 4 0 48 69 m n [Range] (pL + pH × 256) = 4 (pL = 4, pH =0) cn = 48 fn = 69 m = 48, 49 48 ≤ n ≤ 56 [m = 48] 1 ≤ n ≤ 40 [m = 49] 

- [Default] m = 49, n = 1 [ratio: 10%] 

- [Description] Sets the error correction level for PDF417. 

|m|**Function**|
|---|---|
|48|The error correction level is set by “level.”|
|49|The error correction level is set by “ratio.” The ratio is<br>[n ×10%].|



## [Notes] 

- Settings of this function affect the processing of Functions 081 and 082. 

- Error correction level is specified by either “level” or “ratio.” 

- Error correction level specified by “level” (m = 48) is as follows. The number of the error correction codeword is fixed regardless of the number of codewords in the data area. 

|n|**Function**|**Number of error correction codeword**|
|---|---|---|
|48|Error correction level 0|2|
|49|Error correction level 1|4|
|50|Error correction level 2|8|
