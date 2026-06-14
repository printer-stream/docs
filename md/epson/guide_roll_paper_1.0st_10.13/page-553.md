## **C O N F I D E N T I A L** 

## <Function 60> **FS ( E** _**pL pH fn m c d1 d2 d3**_ ( _fn_ =60) 

EXECUTING COMMAND 

[Name] Cancel set values for top/bottom logo printing [Format] ASCII FS ( E pL pH fn   m c d1  d2  d3 Hex 1C 28 45 pL pH fn   m c d1  d2  d3 Decimal 28 40 69     pL pH fn   m c d1   d2   d3 

- [Range] (pL + pH × 256) = 6  (pL=6, pH=0) fn = 60 

   - m = 2 

   - c = 48, 49 

   - d1 = 67 (Character “C”) 

   - d2 = 76 (Character “L”) d3 = 82 (Character “R”) 

- [Description] Cancels set values for top/bottom logo printing by specifying c. 

|**c**|**Function**|
|---|---|
|48|Cancels set values for top logo printing.|
|49|Cancels set values for bottom logo printing.|



- After canceling set values for top/bottom logo printing, no settings remain for logo printing. 
