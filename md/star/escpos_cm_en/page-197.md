Rev.2.52 

## **ESC GS SUB DC1 m t1 t2** 

|**ESC GS SUB DC1 m t1 t2**|**ESC GS SUB DC1 m t1 t2**|
|---|---|
|Name<br>Specify snout operation mode<br>Code<br>ASCII<br>ESC GS SUB DC1 m t1 t2<br>Hex.<br>1B   1D  1A   11   m  t1  t2<br>Decimal<br>27   29  26   17   m  t1  t2<br>Defned Region<br>0≤m≤3 (48≤m≤51)<br>t1 = 0, t2 =0<br>Initial Value<br>MSW Setting<br>Function<br>Specifythe snout operation mode usingthe mparameter.||
|m|Snout Operating Mode|
|0,48|SnoutLEDoutput OFF|
|1, 49|Snout LED output ON (while printing, or during presenter opera-<br>tion)|
|2, 50|SnoutLEDoutput ON(during anerror)|
|3, 51|Snout LED output ON (while printing, or during presenter opera-<br>tionoranerror)|



This command is valid when a presenter is connected. 

When the snout is not connected, this command is prohibited from use. 

Reference ESC GS SUB DC2, ESC GS SUB DC3 

ESC/POS Command Specifications 

197 
