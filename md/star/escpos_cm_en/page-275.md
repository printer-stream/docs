Rev.2.52 

## 4. Fourth Byte (Paper Detector Information) 

|Bit|Contents|Status|Status|Targeted Status n|Targeted Status n|Targeted Status n|Targeted Status n|Targeted Status n|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|Compatibility Per Model|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”|“1”|Bit7|Bit3|Bit2|Bit1|Bit0|TSP600|TSP700|TSP800|TUP900|TSP1000|TSP700II|TSP650|TUP500|TSP800II|FVP10|BSC10|TSP043|TSP650II|TSP650IISK|
|7|Fixed at “0”||||||||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|6|Black mark sensor<br>status|White<br>detection|Black<br>detection|○|||||○|○|○|x|x|x|x|x|x|x|x|x|x|x|
|5|Undefned (“0”)||||||||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|4|Fixed at “0”||||||||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|3|Undefned (“0”)||||||||-|-|-|-|-|-|-|-|-|-|Fixed at<br>“1”|Fixed at<br>“1”|-|-|
|2|Undefned (“0”)||||||||-|-|-|-|-|-|-|-|-|-|Fixed at<br>“1”|Fixed at<br>“1”|-|-|
|1|Presenter paper<br>status|Has<br>paper|Paper Out<br>(Recovered)||○||||x|x|x|○|x|x|x|○|x|x|Fixed at<br>“1”|Fixed at<br>“1”|x|x|
||Stack sensor paper<br>status|Has<br>paper|Paper Out||○||||x|x|x|x|○|x|x|x|x|x|||x|x|
||Hold print status<br>control|Paper<br>Out|Has paper||○||||x|x|x|x|x|x|x|x|x|x|||x|○|
|0|Undefned (“0”)||||||||-|-|-|-|-|-|-|-|-|-|Fixed at<br>“1”|Fixed at<br>“1”|-|-|



## Bit-6: This bit is set only when black marks are effective. 

ESC/POS Command Specifications 
