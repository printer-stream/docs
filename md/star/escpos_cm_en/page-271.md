Rev.2.52 

## 3. Error Cause Status (n=3) 

|3.|Error Cause Status|(n=3)|(n=3)|||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Bit|Contents|Status||CompatibilityPer Model||||||||||||||
|||“0”|“1”|TSP600|TSP700|TSP800|TUP900|TSP1000|TSP700II|TSP650|TUP500|TSP800II|FVP10|BSC10|TSP043|TSP650II|TSP650IISK|
|7|Fixed at “0”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|6|Auto-recovery Error|No<br>error|Error|○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|5|Non-recoverable Error|No<br>error|Error|○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|4|Fixed at “1”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|3|Auto-cutter error|No<br>error|Error|○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|2|Black mark error|No<br>error|Error|○|○|○|x|○|○|x|x|○|○|○|○|×|×|
||Mechanical Error|No<br>error|Error|x|x|x|○|x|x|x|○|x|x|x|x|×|×|
|1|Fixed at “1”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|0|Fixed at “0”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|



- Bit-2:  Black mark error status is allocated for models not equipped with a presenter; mechanical error status is allocated to those models equipped with a presenter. Black mark error status is set only when the black mark is enabled. 

A mechanical error on models provided with a presenter represents a paper jam in the presenter and black mark errors. 

## 4. Continuous Paper Detector Status (n=4) 

|Bit|Contents|Status|Status|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”|“1”|TSP600|TSP700|TSP800|TUP900|TSP1000|TSP700II|TSP650|TUP500|TSP800II|FVP10|BSC10|TSP043|TSP650II|TSP650IISK|
|7|Fixed at “0”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|6|Paper out sensor|Has<br>paper|Paper<br>Out|○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|5|Paper out sensor|Has<br>paper|Paper<br>Out|○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|4|Fixed at “1”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|3|Near-end Sensor|Has<br>paper|Paper<br>Out|○|○|○|○|○|○|○|○|○|○|○|○|○|x|
|2|Near-end Sensor|Has<br>paper|Paper<br>Out|○|○|○|○|○|○|○|○|○|○|○|○|○|x|
||Black mark sensor status|White<br>detection|Black<br>detection|○|○|○|x|x|○|-|x|○|x|x|x|-|-|
|1|Fixed at “1”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|0|Fixed at “0”|||-|-|-|-|-|-|-|-|-|-|-|-|-|-|



Bit-2: This bit functions as the status indicating the near end sensor when the black mark is disabled.  When using the black mark, it functions as the status to indicate the black mark sensor status. 

However, on TUP900/TSP1000/TUP500/FVP10, it functions as the status to indicate the near end sensor even when using black marks. 

ESC/POS Command Specifications 
