## **C O N F I D E N T I A L** 

## **GS** ✻ 

SETTING COMMAND 

[Name] Define downloaded bit image [Format] ASCII GS ✻ x y d1 _**...**_ d _**(**_ x × y × _**8**_ **)** Hex 1D 2A x y d1 _**...**_ d _**(**_ x × y × _**8**_ **)** Decimal 29 42 x y d1 _**...**_ d _**(**_ x × y × _**8)**_ [Range] TM-J2000/J2100 **: 1** ≤ x ≤ **255 1** ≤ y ≤ **255 (1** ≤ x × y ≤ **3072) 0** ≤ d ≤ **255** k **=** x × y × **8** TM-T90: **1** ≤ x ≤ **255 (1** ≤ x × y ≤ **1536) 1** ≤ y ≤ **48 (1** ≤ x × y ≤ **1536) [Except for Japanese model] 1** ≤ y ≤ **46 (1** ≤ x × y ≤ **1536) [Japanese model] 0** ≤ d ≤ **255** k **=** x × y × **8** TM-T20, TM-T88IV, TM-T88V, TM-T70 **: 1** ≤ x ≤ **255 1** ≤ y ≤ **48 (1** ≤ x × y ≤ **1536) 0** ≤ d ≤ **255** k **=** x × y × **8** TM-L90: **1** ≤ x ≤ **255 1** ≤ y ≤ **46 (1** ≤ x × y ≤ **1536) 0** ≤ d ≤ **255** k **=** x × y × **8** 

[Default] None 

[Printers not featuring this command] TM-P60, TM-U230, TM-U220 

[Description] Defines the downloaded bit image in the downloaded graphic area. 

- x specifies the number of bytes in horizontal direction as x bytes. 

- y specifies the number of bytes in vertical direction as y bytes. 

- d defines the bit image data (column format). 
