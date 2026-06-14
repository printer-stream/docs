**ESC GS x S 3 n** 

[Name] Set PDF417 module aspect ratio [Code] ASCII ESC GS x S 3 n Hex. 1B 1D 78 53 33 n Decimal 27 29 120 83 51 n [Defined Area] 1 ≤ n ≤ 10 [Initial Value] n = 3 [Function] Parameter details • n: Sets the module aspect ratio (asp). The module Y direction size (x-dim x asp) is set using this command. It is recommended that 2 ≤ n when specifying using this command. When using with n = 1, check by actual use. 

**ESC GS x D nL nH d1 d2 … dk** 

[Name] Set PDF417 bar code data [Code] ASCII ESC GS x D nL nH d1 d2 … dk Hex. 1B 1D 78 44 nL nH d1 d2 … dk Decimal 27 29 120 68 nL nH d1 d2 … dk [Defined Area] 0 ≤ nL ≤ 255, 0 ≤ nH ≤ 255 1 ≤ (nL + nH x 256) ≤ 1024 0 ≤ d ≤ 255 1 ≤ k ≤ 1024 [Initial Value] --[Function] Parameter details • nL + nH x 256 : Bar code data count • dk : Bar code data (Maximum 1024 data) When [nL + nH x 256] is outside of the definition, data of [nL + nH x 256] bytes is discarded. 

|**ESC GS x P**|**ESC GS x P**|**ESC GS x P**||
|---|---|---|---|
|[Name]|Print PDF417 bar code|||
|[Code]|ASCII|ESC<br>GS<br>x|P|
||Hex.|1B<br>1D<br>78|50|
||Decimal|Decimal<br>27<br>29<br>120|80|
|[Defined Area]||---||
|[Initial Value]||---||
|[Function]|[Function]|Prints the bar code data.|Prints the bar code data.|
|||If there is unprinted data in the line buffer, this command is executed after printing that data in the|If there is unprinted data in the line buffer, this command is executed after printing that data in the|
|||line buffer. Therefore, it is not possible to print with other data in the same line (characters, bit||
|||images, bar codes).||
|||Also, this command is ignored if the following errors occur.||
|||• When an error is generated when generating a bar code, due to the combination of the bar code||
|||setting commands||
|||• When the bar code data that is generated exceeds the printable size of PDF417||
|||• When the print data exceeds the currently set print region||
|||When a bar code is printed, always verify it by actual use.||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-123 
