Rev.2.52 

## **GS ! n** 

Name 

Select character size 

Code ASCII GS ! n Hex. 1D 21 n Decimal 29 33 n 0 ≤ n ≤ 255 Defined Region 

However, 1 ≤ vertical direction magnification ratio ≤ 8, 1 ≤ horizontal direction magnification ratio ≤ 8 

n = 0 

Initial Value n = 0 Function Specifies the character size (magnification ratio in the vertical and horizontal directions). 

|Bit|Function<br>|“0”|“1”|
|---|---|---|---|
|7|Specifes horizontal direction<br>magnifcation ratio<br>|(See table below)||
|6||||
|5||||
|4||||
|3|Specifes vertical direction<br>magnifcation ratio|(See table below)||
|2||||
|1||||
|0||||



<Horizontal Direction Magnification Ratio Specification> <Vertical Direction Magnification Ratio Specification> 

|Bit-7|Bit-6|Bit-5|Bit-4|Hor. Dir.<br>Mag. Ratio||Bit-3|Bit-2|Bit-1|Bit-0|Hor. Dir.<br>Mag. Ratio|
|---|---|---|---|---|---|---|---|---|---|---|
|0|0|0|0|1||0|0|0|0|1|
|0|0|0|1|2||0|0|0|1|2|
|0|0|1|0|3||0|0|1|0|3|
|0|0|1|1|4||0|0|1|1|4|
|0|1|0|0|5||0|1|0|0|5|
|0|1|0|1|6||0|1|0|1|6|
|0|1|1|0|7||0|1|1|0|7|
|0|1|1|1|8<br>||0|1|1|1|8<br>|
|1|0|0|0|Undefned<br>||1|0|0|0|Undefned<br>|
|1|0|0|1|Undefned<br>||1|0|0|1|Undefned<br>|
|1|0|1|0|Undefned<br>||1|0|1|0|Undefned<br>|
|1|0|1|1|Undefned<br>||1|0|1|1|Undefned<br>|
|1|1|0|0|Undefned<br>||1|1|0|0|Undefned<br>|
|1|1|0|1|Undefned<br>||1|1|0|1|Undefned<br>|
|1|1|1|0|Undefned<br>||1|1|1|0|Undefned<br>|
|1|1|1|1|Undefned||1|1|1|1|Undefned|



ESC/POS Command Specifications 

86 
