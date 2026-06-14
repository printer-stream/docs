## **C O N F I D E N T I A L** 

## <Function 65> **FS ( E** _**pL pH fn m a n**_ ( _fn_ =65) 

EXECUTING COMMAND 

- [Name] Enable/disable top/bottom logo printing 

[Format] ASCII FS ( E pL pH fn m a n Hex 1C 28 45 pL pH fn m a n Decimal 28 40 69 pL pH fn m a n [Range] (pL + pH × 256) = 4  (pL= 4, pH = 0) fn = 65 

   - m = 2 

   - a = 48, 49 

   - n = 48, 49 

- [Default] n = 48 [when a = 48] 

   - n _=_ 48 [when a = 49] 

- [Description] Specifies top/bottom logo printing by a and enables or disables top/bottom logo printing by n. 

## ■ Top/bottom logo printing specified by a is as follows: 

|■Top|/bottom logo printing specified byais as foll|
|---|---|
|**a**|**Function**|
|48|Specifies top logo printing.|
|49|Specifies bottom logo printing.|



## ■ Enabling/disabling setting specified by n is as follows: 

|■Ena|bling/disabling setting specified bynis as foll|
|---|---|
|**n**|**Function**|
|48|Enables.|
|49|Disables.|



## [Notes] 

- Volatile memory is used as the storage area for set values ( **n** ). 

- This command is used when changing the setting of “Logo printing enabled” set with **FS ( E** <Function 64> to Disabled temporarily. 
