## **C O N F I D E N T I A L** 

## **GS ( N** _**p**_ L _**p**_ H _**fn m**_ <Function 50> 

[Name] Turn shading mode on/off 

[Format] ASCII GS ( N pL pH fn m a Hex 1D 28 4E 03 00 32 m a Decimal 29 40 78 3 0 50 m a [Range] (pL + pH × 256) = 3 (pL =3, pH =0) fn = 50 m = 0, 1, 48, 49 TM-J2000/J2100 **:** a **= 48** 

- [Default] m = 0, a = 48 

- [Default] Turns the character shadow mode on or off. 

|m|**Function**|
|---|---|
|0, 48|Character shadow mode is turned on.|
|1, 49|Character shadow mode is turned off.|



Prints the character shadow in the color specified by a as follows: 

|a|**Shadow color**|
|---|---|
|48|None (not print)|
|49|Color 1|
|50|Color 2|
|51|Color 3|



## [Notes] 

■ Even if underline mode is turned on, the shadow of the underline is not printed. 

■ In white/black reverse print mode, the color of the shadow specified by this function does not change. [Model-dependent variations] TM-J2000/J2100, TM-T90, TM-T88IV, TM-L90 
