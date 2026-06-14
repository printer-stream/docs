## **C O N F I D E N T I A L** 

## **GS ( E** _**pL pH fn y c1 c2[x d1...d(y**_ × _**x)] k**_ <Function 8> 

[Name] Define the data (column format) for the character code page 

[Format] ASCII GS ( E pL pH fn y c1 c2 [x d1...d(y × x)]k Hex 1D 28 45 pL pH 08 y c1 c2 [x d1...d(y × x)]k Decimal 29 40 69 pL pH 8 y c1 c2 [x d1...d(y × x)]k [Range] 5 ≤ (pL + pH × 256) ≤ 65535 (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 255) fn = 8 128 ≤ c1 ≤ d2 ≤ 255 

0 ≤ d ≤ 255 

k = c2 – c1 + 1 

|fn= 8<br>128≤ c1 ≤ d2 ≤255<br>0≤ d ≤255<br>k=c2–c1+ 1|||
|---|---|---|
|**Font No. (configuration)**|y|x|
|10 (9×17)|3|9|
|12 (12×24)|3|12|
|17 (8×16)|2|8|
|18 (10×24)|3|10|



[Description] Defines the character pattern (column format) for the character code page in the work area. 

- y specifies the number of bytes in the vertical direction. 

- c1 specifies the beginning character code for the definition, and c2 specifies the final code. 

- x specifies the number of dots in the horizontal direction from the left. 

- d specifies the defined data (column format). 

- k indicates the number of the defined data. k is an explanation parameter; therefore, it does not need to be transmitted. 

## [Notes] 

- This function works in user setting mode. 

■ Characters in Hexadecimal: 80H to FFH / in Decimal: 128 to 255 in ASCII code can be defined. 

■ If y, c1, c2, or x process a value out of the definition range, processing of this function is canceled. 
