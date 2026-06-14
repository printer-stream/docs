## **C O N F I D E N T I A L** 

## **GS ( E** _**pL pH fn a**_ <Function 16> 

[Name] Transmit conditions for USB interface communication [Format] ASCII GS ( E pL  pH  fn  a Hex 1D 28 45 pL  pH  fn  a Decimal 29 40 69 pL  pH  fn  a [Range] (pL + pH × 256) = 2  (pL = 2, pH = 0) fn = 16 

   - a = 1 

- [Description] 

- Transmits the set value for USB interface communication specified by a. 

|a|**Configuration item**|
|---|---|
|1|Class|



## ■ Transmit data is as follows: 

|■Transmit data is as follows:||||
|---|---|---|---|
|**Transmit data**|**Hex**|**Decimal **|**Data**|
|Header|37H|55|1 byte|
|Identifier|52H|82|1 byte|
|Type of configuration item|30H–39H|48 – 57|1– 2 byte|
|Separator|1FH|31|1 byte|
|Set value|30H–39H|48 – 57|1 byte|
|NUL|00H|0|1 byte|



## [Model-dependent variations] 

TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V,  TM-T70, TM-L90, TM-P60, TM-U220 

## TM-J2000/J2100, TM-T90, TM-T88IV, TM-T70, TM-L90, TM-P60, TM-U220 

**This function is not supported.** 

TM-T20, TM-T88V **The printer supports this function.** 
