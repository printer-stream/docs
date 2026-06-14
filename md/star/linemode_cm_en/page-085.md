**ESC GS + m [t1 nL1 nH1 d11 d12 … d1k] 1 [t2 nL2 nH2 d21 d22 … d2k] 2  [tm nLm nHm dm1 dm2 … dmk] m** 

[Name] Register macro 

[Code] ASCII ESC GS + m t1 nL1 nH1 d11 d12 .. d1k Hex. 1B 1D 2B m t1 nL1 nH1 d11 d12 .. d1k Decimal 27 29 43 m t1 nL1 nH1 d11 d12 .. d1k [Code] ASCII t2 nL2 nH2 d21 d22 .. d2k .. tm nLm nHm dm1 dm2 .. dmk .. Hex. t2 nL2 nH2 d21 d22 .. d2k .. tm nLm nHm dm1 dm2 .. dmk .. Decimal t2 nL2 nH2 d21 d22 .. d2k .. tm nLm nHm dm1 dm2 .. dmk .. [Defined Area] 1 ≤ m ≤ 9,  0 ≤ t ≤ 8 k = (nL + nH x 256), 0 ≤ k ≤ 7936 0 ≤ d ≤ 255 

[Initial Value] - - - [Function] This command registers macro data in the following macro registration regions. 

|Registration<br>Region|Registration<br>DataType|Registration<br>Block No.|Size (Bytes)|Details|
|---|---|---|---|---|
|Registration<br>Information|Initialization<br>Macro|0|2|Registration data type 0 x 0000 =<br>Initialization macro, 0xffff=No reg. data|
||||2|Registration data count|
||||4|Registration data address|
||||8|(Reserved)|
||Macro|1|2|Registration data type 0 x 0001 to 0x 0008<br>=macro, 0xffff=No reg. data|
||||2|Registration data count|
||||4|Registrationdata address|
||||8|(Reserved)|
|||**:**|||
|||8|2|Registration data type 0 x 0001 to 0 x<br>0008= macro, 0xffff = Noreg.data|
||||2|Registration data count|
||||4|Registration data address|
||||8|(Reserved)|
|Registration<br>Data|||7936|Registration Data|



- m specifies the registration black count. 

- t specifies the registration data type. 

||t||Registration Data Type|
|---|---|---|---|
||0||Initialization Macro|
|1 to 8|1 to 8|1 to 8|Macro(t is the macro number.)|



- (nL + nH x 256) specifies the data count to be registered. When (nL + nH x 256) = 0, the macro data specified by t is deleted. 

- d is the macro data to be registered. 

- After the macro data is written to the non-volatile memory, the printer is reset. 

- If the volume of all macros exceeds the capacity for registration, it is written to the non-volatile memory up to the data block that exceed the capacity and the command analysis is ended after that. 

- If there is unprinted data in the line buffer, this command is executed after the print data in the line buffer is printed. 

- When registering, all of the current macro regions are cleared, so if previous macro data is necessary, rewrite it. 

- When performing a Hex Dump, initialization macro region data is added in the same way as the current specifications. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-67 
