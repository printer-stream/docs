## **C O N F I D E N T I A L** 

## **ESC a** 

SETTING COMMAND 

|**ESC a**||||
|---|---|---|---|
|[Name]|Select justification|||
|[Format]|ASCII|ESC a|n|
||Hex|1B<br>61|n|
||Decimal|27<br>97|n|
|[Range]|0≤  n ≤2, 48≤  n ≤||50|
|[Default]|n= 0|||



[Printers not featuring this command] None 

[Description] In standard mode, aligns all the data in one line to the selected layout, using n as follows: 

|n|**Justification**|
|---|---|
|0, 48|Left justification|
|1, 49|Centered|
|2, 50|Right justification|



## [Notes] 

- When standard mode is selected, this command is enabled only when processed at the beginning of the line in standard mode. 

- The justification has no effect in page mode. If this command is processed in page mode, an internal flag is activated, and this flag is enabled when the printer returns to standard mode. 

- This command executes justification in the print area set by GS L and GS W. 

- This command justifies printing data (such as characters, all graphics, bar codes, and two dimensionl codes) and space area set by HT, ESC $, and ESC \. 

- The settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off. 
