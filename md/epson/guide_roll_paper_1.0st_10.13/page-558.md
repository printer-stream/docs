## **C O N F I D E N T I A L** 

## <Function 63> **FS ( E** _**pL pH fn m kc1 kc2 a**_ ( _fn_ =63) 

SETTING COMMAND 

- [Name] Set bottom logo printing 

- [Format] ASCII FS ( E pL pH fn m kc1 kc2 a Hex 1C 28 45 pL pH fn m kc1 kc2 a Decimal 28 40 69 pL pH fn m kc1 kc2 a 

- [Range] (pL + pH × 256) = 5  (pL = 5, pH = 0) fn = 63 

   - m = 2 

   - 32 ≤ kc1 ≤ 126 

   - 32 ≤ kc2 ≤ 126 

   - 48 ≤ a ≤ 50 

- [Description] Sets bottom logo key code, and justification. 

   - Associates key codes (kc1 _,_ kc2) of NV graphics to be printed as a bottom logo. 

   - a specifies justification for bottom logo printing. 

|**a**|**Function**|
|---|---|
|48|Specifies left justification.|
|49|Specifies center justification|
|50|Specifies right justification.|



## [Notes] 

- NV memory is used as the storage area for set values of bottom logo printing. 
