## **C O N F I D E N T I A L** 

## <Function 62> **FS ( E** _**pL pH fn m kc1 kc2 a n**_ ( _fn_ =62) 

SETTING COMMAND 

- [Name] Set top logo printing 

- [Format] ASCII FS ( E pL pH fn m kc1 kc2 a n Hex 1C 28 45 pL pH fn m kc1 kc2 a n Decimal 28 40 69 pL pH fn m kc1 kc2 a n 

- [Range] (pL + pH × 256) = 6  (pL = 6, pH = 0) fn = 62 

   - m = 2 

   - 32 ≤ kc1 ≤ 126 

   - 32 ≤ kc2 ≤ 126 

   - 48 ≤ a ≤ 50 

   - 0 ≤ n ≤ 255 

- [Description] Sets top logo key code, justification, and number of lines to be removed after top logo printing. 

   - Associates key codes (kc1 _,_ kc2) of NV graphics to be printed as a top logo. 

   - a specifies justification for top logo printing. 

|**a**|**Function**|
|---|---|
|48|Specifies left justification.|
|49|Specifies centering.|
|50|Specifies right justification.|



- n specifies the number of lines to be removed after top logo printing. 

[Notes] 

- NV memory is used as the storage area for set values of top logo printing. 
