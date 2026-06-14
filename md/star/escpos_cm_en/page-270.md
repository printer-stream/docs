Rev.2.52 

## **6-2-3 DLE EOT Status** 

## 1. Printer Status (n=1) 

||Contents|Status|Status|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”|“1”|TSP600|TSP700|TSP800|TUP900|TSP1000|TSP700II|TSP650|TSP500|TSO800II|FVP10|BSC10|TSP043|TSP650II|TSP650IISK|
|7|Fixed at “0”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|6|Undefned(“0”)|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|5|Undefned (“0”)|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|4|Fixed at “1”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|3|ON LINE/OFFLINE<br>Status|ONLINE|OFFLINE|○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|2|Drawer kick connector<br>pin #3|“L”|“H”|○|○|○|x|x|○|○|○|○|○|○|○|○|○|
||Presenter Cover|Closed|Open|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|1|Fixed at “1”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|0|Fixed at “0”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|



Bit-2: Drawer kick connector #3 pin status is allocated for models not equipped with a presenter; presenter cover status is allocated to those models equipped with a presenter.  TUP900 is provided with a presenter, but this bit is invalid because it does not have a presenter cover. 

## 2. Offline Cause Status (n=2) 

|Bit|Contents|Status|Status|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”|“1”|TSP600|TSP700|TSP800|TUP900|TSP1000|TSP700II|TSP650|TUP500|TSP800II|FVP10|BSC10|TSP043|TSP650II|TSP650IISK|
|7|Fixed at “0”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|6|Error|No error|Error|○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|5|Printing stops because<br>ofpaper out|None|Print<br>stopped|○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|4|Fixed at “1”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|3|Paper SW input|No SW<br>Input|SW Input|○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|2|Cover Status|Closed|Open|○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|1|Fixed at “1”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|0|Fixed at “0”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|



## Bit-6:  Indicates this error is non-recoverable. 

## Bit-5:  Bit-5 = “1” (Print stopped) when printing stops because there is no paper. TSP600/TSP700/TSP800 

When the printer is Busy in the Paper-end state and there is data in the receive buffer, this bit is set. While processing this command,  this command is included in the receive buffer. 

ESC/POS Command Specifications 
